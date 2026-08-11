import sys
import csv

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

def parse_interface(filename):
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
    
def write_csv(interfaces, filename):
    fieldnames = ["interface", "ip", "method", "status", "protocol"]
    with open(filename, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(interfaces)


def main():
    if len(sys.argv) != 3:
        print("Usage: python3 parser.py <input_file> <output_file>")
        sys.exit(1)
    
    input_file = sys.argv[1]
    output_file = sys.argv[2]

    interfaces = parse_interface(input_file)
    write_csv(interfaces, output_file)
    print(f"Parsed {len(interfaces)} interfaces. CSV written to {output_file}")

if __name__ == "__main__":
    main()

