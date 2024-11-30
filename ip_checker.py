import socket
import sys
import re

def check_port(ip, port):
    try:
        with socket.create_connection((ip, port), timeout=5) as s:
            return True
    except (socket.timeout, socket.error):
        return False

def parse_issue_body(issue_body):
    # Extract IP and port using regex
    match = re.search(r"IP:\s*([\d.]+)\s*PORT:\s*(\d+)", issue_body, re.IGNORECASE)
    if match:
        ip = match.group(1)
        port = int(match.group(2))
        return ip, port
    return None, None

if __name__ == "__main__":
    issue_body = sys.argv[1]  # Pass the issue body as an argument
    ip, port = parse_issue_body(issue_body)
    
    if ip and port:
        result = check_port(ip, port)
        status = "open" if result else "closed"
        print(f"Port {port} on {ip} is {status}.")
    else:
        print("Invalid input. Ensure the issue body includes 'IP: <ip> PORT: <port>'.")
