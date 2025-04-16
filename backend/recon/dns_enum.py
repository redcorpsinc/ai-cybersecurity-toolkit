import dns.resolver
from typing import Dict


def enum_dns(domain: str) -> Dict:
    """
    Perform basic DNS enumeration: A, AAAA, MX, NS, TXT records.
    Returns:
        dict: DNS data
    """
    record_types = ['A', 'AAAA', 'MX', 'NS', 'TXT']
    results = {}

    for record_type in record_types:
        try:
            answers = dns.resolver.resolve(domain, record_type)
            results[record_type] = [r.to_text() for r in answers]
        except Exception as e:
            results[record_type] = f"Error: {str(e)}"

    return {
        "domain": domain,
        "dns_records": results
    }


# 🔍 Test
if __name__ == "__main__":
    print(enum_dns("example.com"))
