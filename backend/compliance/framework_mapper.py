def map_finding_to_controls(finding: str) -> dict:
    """
    Maps a specific issue to multiple frameworks (CIS v8, NIST CSF, PCI-DSS, ISO 27001).
    Args:
        finding (str): A vulnerability or misconfiguration string
    Returns:
        dict: Mapped controls per framework
    """
    mapping_db = {
        "tls_1_0_enabled": {
            "CIS": ["13.3"],
            "NIST": ["PR.IP-1"],
            "PCI": ["4.1"],
            "ISO": ["A.10.1.1"]
        },
        "rdp_port_open": {
            "CIS": ["9.2", "13.6"],
            "NIST": ["PR.AC-3"],
            "PCI": ["1.2.1"],
            "ISO": ["A.13.1.1"]
        },
        "outdated_cms": {
            "CIS": ["2.4"],
            "NIST": ["PR.IP-3"],
            "PCI": ["6.2"],
            "ISO": ["A.12.6.1"]
        },
        "default_credentials": {
            "CIS": ["4.1", "5.1"],
            "NIST": ["PR.AC-6"],
            "PCI": ["8.2.3"],
            "ISO": ["A.9.2.3"]
        }
    }

    key = normalize_finding(finding)
    return mapping_db.get(key, {
        "CIS": [],
        "NIST": [],
        "PCI": [],
        "ISO": []
    })


def normalize_finding(finding: str) -> str:
    """
    Normalize strings to match keys in mapping DB
    """
    if "tls 1.0" in finding.lower():
        return "tls_1_0_enabled"
    elif "rdp" in finding.lower():
        return "rdp_port_open"
    elif "wordpress 4" in finding.lower() or "drupal 7" in finding.lower():
        return "outdated_cms"
    elif "default credential" in finding.lower():
        return "default_credentials"
    else:
        return "unknown"
