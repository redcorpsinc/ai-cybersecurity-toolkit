def get_prompt_prefix(framework: str = "NIST CSF 2.0") -> str:
    """
    Return a compliance-specific prompt prefix for GPT audit context
    """
    framework = framework.lower()

    if "nist" in framework:
        return "You are performing a security audit based on NIST CSF 2.0. Map risks to categories like PR, DE, RS."
    elif "cis" in framework:
        return "You are using CIS Controls v8 to analyze risks. Map findings to relevant CIS control numbers."
    elif "pci" in framework:
        return "You are a PCI-DSS auditor. Identify risks related to credit card and payment systems (PCI v4.0)."
    elif "iso" in framework:
        return "You are applying ISO/IEC 27001 standards. Map each vulnerability to Annex A control objectives."
    else:
        return "You are performing a general cybersecurity risk assessment with best practices."



def get_framework_mapping_key(framework: str = "NIST") -> str:
    """
    Normalize framework name for compliance mapper
    """
    if "nist" in framework.lower():
        return "NIST"
    elif "cis" in framework.lower():
        return "CIS"
    elif "pci" in framework.lower():
        return "PCI"
    elif "iso" in framework.lower():
        return "ISO"
    else:
        return "GENERIC"
