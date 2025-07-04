from fastapi import APIRouter, HTTPException, Body
from recon.nmap_runner import run_nmap_scan
from ai.risk_engine import generate_risk_assessment
from reports.report_generator import generate_report
from recon.dns_enum import enum_dns
from recon.tech_stack import fingerprint_tech_stack

router = APIRouter()

@router.post("/",
    summary="Run Scan + Generate Report",
    description="""
    Submit a domain or IP to perform a full cybersecurity risk audit:
    - Nmap + tech stack recon
    - GPT-based risk scoring
    - Compliance mapping
    - PDF/HTML report generation

    Returns summary, score, and report path.
    """,
    response_description="Scan result + risk score + path to generated report"
)
async def scan_and_audit(
    payload: dict = Body(..., example={"target": "example.com", "framework": "NIST CSF"})
):
    """
    Full scan pipeline: recon → AI audit → compliance mapping → report generation.
    """
    try:
        target = payload["target"]
        framework = payload.get("framework", "NIST CSF")

        # Step 1: Recon
        recon_data = run_nmap_scan(target)

        # Optional extra recon
        dns_data = enum_dns(target)
        tech_stack = fingerprint_tech_stack(f"https://{target}")

        # Step 2: GPT risk engine
        ai_result = generate_risk_assessment(
            scan_data=recon_data,
            dns_data=dns_data,
            tech_stack=tech_stack,
            framework=framework
        )
        ai_result["target"] = target
        ai_result["framework"] = framework

        # Step 3: Report generation
        report_path = generate_report(ai_result, output_format="pdf")

        return {
            "success": True,
            "target": target,
            "framework": framework,
            "risk_score": ai_result.get("score"),
            "summary": ai_result.get("summary"),
            "report_path": report_path
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
