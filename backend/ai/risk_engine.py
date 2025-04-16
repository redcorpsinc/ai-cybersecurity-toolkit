import openai
import os
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_risk_assessment(scan_data: dict, framework: str = "NIST CSF 2.0") -> dict:
    """
    Analyze scan data and return a structured risk report using GPT-4.
    Args:
        scan_data (dict): Dictionary from recon module
        framework (str): Compliance mapping (NIST, CIS, PCI, ISO)
    Returns:
        dict: Risk score, summary, mapped framework controls, remediations
    """

    # Prompt construction
    prompt = f"""
You are a cybersecurity compliance analyst. Based on the following scan results, generate:
1. A risk score from 0 to 100
2. Severity classification (Low/Medium/High/Critical)
3. Top 3 vulnerabilities with remediation
4. Compliance mapping to {framework}
5. Executive summary (non-technical)

Scan Data:
{scan_data}

Respond in the following JSON format:
{{
    "score": <int>,
    "severity": "<str>",
    "summary": "<str>",
    "vulnerabilities": [
        {{
            "issue": "<str>",
            "recommendation": "<str>",
            "mapped_controls": ["<control1>", "<control2>"]
        }}
    ]
}}
"""

    try:
        completion = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a cybersecurity compliance expert."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.4
        )

        response_text = completion.choices[0].message.content
        return eval(response_text)  # Convert stringified JSON to dict

    except Exception as e:
        return {
            "error": str(e),
            "score": 0,
            "severity": "N/A",
            "summary": "Unable to process scan data",
            "vulnerabilities": []
        }
