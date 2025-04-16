#!/usr/bin/env python3

import argparse
import os
import json
import base64
from datetime import datetime
from rich import print
from rich.console import Console
from rich.table import Table

from backend.recon.nmap_runner import run_nmap_scan
from backend.ai.risk_engine import generate_risk_assessment
from backend.reports.report_generator import generate_report

LICENSE_CACHE_PATH = os.path.expanduser("~/.ai-sec-cli/license.lic")

console = Console()


def load_license():
    if not os.path.exists(LICENSE_CACHE_PATH):
        raise Exception("License not found. Run `--activate` first.")

    with open(LICENSE_CACHE_PATH, "r") as f:
        raw = base64.b64decode(f.read().encode())
        data = json.loads(raw)
        expiry = datetime.fromisoformat(data["payload"]["expires"])

        if datetime.utcnow() > expiry:
            raise Exception("❌ License expired.")
        return data["payload"]


def save_license(license_key: str):
    os.makedirs(os.path.dirname(LICENSE_CACHE_PATH), exist_ok=True)
    with open(LICENSE_CACHE_PATH, "w") as f:
        f.write(license_key.strip())
    print("[green]✅ License activated and saved locally.")


def run_local_scan(target: str, framework: str = "NIST CSF"):
    console.rule(f"[bold cyan]🔍 Starting Local Audit: {target}")

    # Recon
    recon_data = run_nmap_scan(target)
    console.print("[blue]Recon completed. Ports scanned:", len(recon_data["ports"]))

    # AI Risk Engine
    result = generate_risk_assessment(scan_data=recon_data, framework=framework)

    # Report
    path = generate_report(result, output_format="pdf")
    console.print(f"[green]📄 Report generated: {path}")

    # Summary Table
    table = Table(title="Risk Summary")
    table.add_column("Score", style="cyan")
    table.add_column("Severity", style="red")
    table.add_column("Summary", style="white")
    table.add_row(
        str(result["score"]),
        result["severity"],
        result["summary"][:80] + "..."
    )
    console.print(table)


def main():
    parser = argparse.ArgumentParser(description="AI Cybersecurity Toolkit CLI")
    parser.add_argument("--activate", metavar="LICENSE_KEY", help="Activate your license key")
    parser.add_argument("--scan", metavar="TARGET", help="Run full scan & report on domain or IP")
    parser.add_argument("--framework", default="NIST CSF", help="Compliance framework (default: NIST CSF)")
    args = parser.parse_args()

    try:
        if args.activate:
            save_license(args.activate)
            return

        # Check license
        _ = load_license()

        if args.scan:
            run_local_scan(args.scan, framework=args.framework)
        else:
            parser.print_help()

    except Exception as e:
        console.print(f"[bold red]❌ Error: {str(e)}")


if __name__ == "__main__":
    main()
