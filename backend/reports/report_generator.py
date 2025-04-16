from jinja2 import Environment, FileSystemLoader
from weasyprint import HTML
import os
from datetime import datetime
import hashlib
import json

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TEMPLATE_DIR = os.path.join(BASE_DIR, "templates")
OUTPUT_DIR = os.path.join(BASE_DIR, "output")

env = Environment(loader=FileSystemLoader(TEMPLATE_DIR))


def generate_report(data: dict, output_format: str = "pdf", filename: str = None) -> str:
    """
    Generates an audit report in HTML or PDF format.
    Args:
        data (dict): risk engine output
        output_format (str): 'pdf' or 'html'
        filename (str): optional filename
    Returns:
        str: Path to the generated report
    """
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    # Hash for traceability
    raw_json = json.dumps(data, sort_keys=True).encode()
    report_hash = hashlib.sha256(raw_json).hexdigest()[:10]

    # Templating
    template = env.get_template("report_template.html")
    rendered_html = template.render(
        report=data,
        date=datetime.utcnow().strftime("%Y-%m-%d %H:%M UTC"),
        hash=report_hash,
        version="1.0.0",
        framework=data.get("framework", "NIST CSF"),
    )

    # Output path
    filename = filename or f"security_report_{report_hash}"
    out_path = os.path.join(OUTPUT_DIR, f"{filename}.{output_format}")

    # Export logic
    if output_format == "html":
        with open(out_path, "w") as f:
            f.write(rendered_html)
    elif output_format == "pdf":
        HTML(string=rendered_html).write_pdf(out_path)

    return out_path
