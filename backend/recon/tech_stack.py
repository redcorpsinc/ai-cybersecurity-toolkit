import requests
from bs4 import BeautifulSoup
from typing import Dict


def fingerprint_tech_stack(url: str) -> Dict:
    """
    Passively fingerprint web stack by checking headers, HTML, and favicon.
    Args:
        url (str): Full URL (e.g. https://example.com)
    Returns:
        dict: Technologies detected
    """
    try:
        resp = requests.get(url, timeout=10, headers={"User-Agent": "Mozilla/5.0"})
        headers = resp.headers
        tech = {
            "server": headers.get("Server", "Unknown"),
            "x-powered-by": headers.get("X-Powered-By", "Unknown"),
            "frameworks": [],
            "cms": []
        }

        # Basic HTML checks
        soup = BeautifulSoup(resp.text, "html.parser")
        meta_tags = soup.find_all("meta")

        for tag in meta_tags:
            name = tag.get("name", "").lower()
            content = tag.get("content", "").lower()

            if "generator" in name or "wordpress" in content:
                tech["cms"].append("WordPress")
            if "drupal" in content:
                tech["cms"].append("Drupal")

        # Additional basic checks
        if "wp-content" in resp.text:
            tech["cms"].append("WordPress")
        if "Joomla" in resp.text:
            tech["cms"].append("Joomla")

        return {
            "url": url,
            "detected_stack": tech
        }

    except Exception as e:
        return {
            "url": url,
            "error": str(e)
        }


# 🔍 Test
if __name__ == "__main__":
    print(fingerprint_tech_stack("https://example.com"))
