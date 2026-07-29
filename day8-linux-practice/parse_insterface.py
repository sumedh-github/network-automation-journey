def parse_line(line):
    field = line.split()
    try:
        interface = field[0]
        ip = field[1]
        protocol = field[-1]
        status = " ".join(field[3:-1])

        return{
            "interface": interface,
            "ip": ip,
            "protocol": protocol,
            "status": status,
        }
    
    except IndexError as e:
        print(f"Skipping malformed line: '{line}' — {e}")
        return None

def parse_insterface(filename):
    interfaces = []
    with open(filename, "r") as f:
        for line in f:
            
            line = line.strip()
            if not line:
                continue
            
            parsed_line = parse_line(line)
            if parsed_line is not None:
                interfaces.append(parsed_line)

            
        return interfaces
            



if __name__ == "__main__":
    results = parse_insterface("sample_interfaces.txt")
    for entry in results:
        print(entry)