import subprocess
import json
import xml.etree.ElementTree as ET
from typing import List, Dict


def run_nmap_scan(target: str, ports: str = "1-1000") -> Dict:
    """
    Run an Nmap scan on the given target and return structured scan data.
    Args:
        target (str): IP or domain to scan
        ports (str): Port range
    Returns:
        dict: Structured JSON data
    """
    try:
        cmd = [
            "nmap",
            "-p", ports,
            "-sV",             # Service version detection
            "-T4",             # Faster timing
            "-oX", "-",        # Output as XML
            target
        ]
        result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        xml_output = result.stdout
        return parse_nmap_xml(xml_output)

    except Exception as e:
        return {"error": str(e)}


def parse_nmap_xml(xml_data: str) -> Dict:
    """
    Parse Nmap XML output and convert it into structured dict.
    """
    root = ET.fromstring(xml_data)
    parsed_result = {
        "target": root.find("host/address").attrib.get("addr", "unknown"),
        "ports": []
    }

    for port in root.findall(".//port"):
        port_id = port.attrib.get("portid")
        protocol = port.attrib.get("protocol")
        state = port.find("state").attrib.get("state")
        service = port.find("service").attrib.get("name", "unknown")
        version = port.find("service").attrib.get("version", "n/a")

        parsed_result["ports"].append({
            "port": port_id,
            "protocol": protocol,
            "state": state,
            "service": service,
            "version": version
        })

    return parsed_result
