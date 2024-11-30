import socket
import ipaddress
import json
import sys
from concurrent.futures import ThreadPoolExecutor

def check_port(ip, port):
    try:
        with socket.create_connection((ip, port), timeout=1) as s:
            return True
    except:
        return False

def gather_info(ip, port):
    status = check_port(ip, port)
    try:
        hostname = socket.gethostbyaddr(ip)[0] if status else "N/A"
    except socket.herror:
        hostname = "N/A"

    return {
        "ip": ip,
        "port": port,
        "status": "open" if status else "closed",
        "hostname": hostname,
    }

def scan_range(start_ip, end_ip, ports):
    results = []
    ip_range = ipaddress.summarize_address_range(
        ipaddress.IPv4Address(start_ip), ipaddress.IPv4Address(end_ip)
    )

    with ThreadPoolExecutor(max_workers=50) as executor:
        futures = []
        for ip_block in ip_range:
            for ip in ip_block:
                for port in ports:
                    futures.append(executor.submit(gather_info, str(ip), port))

        for future in futures:
            results.append(future.result())

    return results

def parse_issue_body(issue_body):
    # Parse IP range and ports from issue body
    start_ip = end_ip = None
    ports = []
    lines = issue_body.splitlines()

    for line in lines:
        if line.startswith("Start IP:"):
            start_ip = line.split(":")[1].strip()
        elif line.startswith("End IP:"):
            end_ip = line.split(":")[1].strip()
        elif line.startswith("Ports:"):
            ports = [int(p.strip()) for p in line.split(":")[1].split(",")]

    return start_ip, end_ip, ports

if __name__ == "__main__":
    issue_body = sys.argv[1]
    start_ip, end_ip, ports = parse_issue_body(issue_body)

    if start_ip and end_ip and ports:
        results = scan_range(start_ip, end_ip, ports)
        # Save results to a JSON file
        with open("scan_results.json", "w") as f:
            json.dump(results, f, indent=4)
    else:
        print("Invalid input. Ensure the issue body includes Start IP, End IP, and Ports.")
