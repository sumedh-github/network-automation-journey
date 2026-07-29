def parse_insterface(filename):
    interfaces = []
    with open(filename, "r") as f:
        for line in f:
            
            line = line.strip()
            if not line:
                continue
            
            field = line.split()
            interface = field[0]
            ip = field[1]
            protocol = field[-1]
            status = " ".join(field[3:-1])

            interfaces.append({
                "interface": interface,
                "ip": ip,
                "protocol": protocol,
                "status": status,
            })
        return interfaces
            



if __name__ == "__main__":
    results = parse_insterface("sample_interfaces.txt")
    for entry in results:
        print(entry)