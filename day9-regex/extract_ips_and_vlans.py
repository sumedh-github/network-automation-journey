import re

def extract_ips_and_vlans(filename):
    ip_pattern = r"\b(?:\d{1,3}\.){3}\d{1,3}\b"
    vlan_pattern = r"vlan (\d+)"

    results = []

    with open(filename, "r") as f:
        for line in f:
            line = line.strip()

            ip_match = re.search(ip_pattern, line)
            if ip_match:
                results.append({"type": "ip", "value": ip_match.group(), "line": line})

            vlan_match = re.search(vlan_pattern, line)
            if vlan_match:
                results.append({"type": "vlan", "value": vlan_match.group(1), "line": line})

    return results


if __name__ == "__main__":
    findings = extract_ips_and_vlans("sample_config.txt")
    for item in findings:
        print(item)

