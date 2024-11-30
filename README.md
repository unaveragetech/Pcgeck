
# IP Scanner and HTML Report Generator

This repository provides an automated solution to scan an IP range for open ports and generate an HTML report of the scan results. The results are stored in a JSON file and used to generate an HTML report that is updated every time a scan is performed. The system supports scanning specific IP addresses, port ranges, and generating detailed reports for network analysis.

## Overview

The IP Scanner checks for open ports on an IP address or range of IPs and can scan up to 65,535 ports. The results are logged in a JSON file (`scan_results.json`) and are automatically used to generate an HTML report (`index.html`). This report is updated whenever a new scan is triggered.

### Features:
- Scan specific IP ranges (single IP or range of IPs).
- Check multiple ports (individual ports or range of ports).
- Generate a detailed HTML report with scan results.
- Automatically update scan results and commit the changes to the repository.
- Option to scan **all ports** (from 1 to 65535) for an IP address.

## How It Works

1. **Issue Creation**:
   - Open an issue in this repository with the following structure in the body:

   ```txt
   Start IP: <start_ip>
   End IP: <end_ip>
   Ports: <port1>, <port2>, <port3>, ...
   ```

   Example:
   ```txt
   Start IP: 67.249.252.29
   End IP: 67.249.252.29
   Ports: 8080, 80, 443, 22
   ```

   This will trigger an action that:
   - Scans the specified IP range.
   - Checks the specified ports. You can specify individual ports (e.g., `80, 443`) or scan all ports (from 1 to 65535) by leaving the `Ports` field blank or specifying a range.

2. **Scan Process**:
   The system will run the IP scanner, checking each port on the specified IP range. If no ports are provided, all ports (1-65535) will be scanned. The results are saved in the `scan_results.json` file.

3. **HTML Report**:
   Once the scan completes, the results are used to generate an HTML report (`index.html`) that is committed back to the repository. The HTML report includes a summary of open ports and any relevant details about the scan.

4. **Results**:
   The generated HTML report will be available on the GitHub Pages site. The results are updated every time a new scan is triggered. You can access the most recent scan results using the link below.

## See the Results

You can view the latest scan results on the following link:

[See Scan Results](https://unaveragetech.github.io/Pcgeck/)

The report is updated automatically with each scan, and historical scan data is preserved in `scan_results.json` for analysis.

## Requirements

To run the system locally or on a GitHub Action, you need the following dependencies:

- Python 3.x
- `requests` (for making HTTP requests)
- `socket` (for checking open ports)
- `jq` (for handling JSON manipulation)
- `nmap` (optional, for scanning all ports)

These dependencies are listed in the `requirements.txt` file. You can install them by running:

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

## Running the System Locally

To run the scanner locally, follow these steps:

1. Clone the repository:

   ```bash
   git clone https://github.com/unaveragetech/Pcgeck.git
   cd Pcgeck
   ```

2. Install the required dependencies:

   ```bash
   python -m pip install --upgrade pip
   pip install -r requirements.txt
   ```

3. Run the IP scanner:

   To scan a specific IP range and port list, use the following command. For example:

   ```bash
   python ip_scanner.py "Start IP: 67.249.252.29\nEnd IP: 67.249.252.29\nPorts: 8080, 80, 443, 22"
   ```

   If you'd like to scan **all ports** (from 1 to 65535) for an IP, just omit the `Ports` field or specify a range like:

   ```bash
   python ip_scanner.py "Start IP: 67.249.252.29\nEnd IP: 67.249.252.29\nPorts:"
   ```

4. Generate the HTML report:

   After the scan completes, generate the HTML report:

   ```bash
   python generate_html.py
   ```

5. View the results in `index.html`:

   Open the generated `index.html` file in your web browser to see the results of the scan.

## Troubleshooting

- **Timeouts**: If the scanner takes too long to respond, try adjusting the `timeout` value in the script or scan fewer ports.
- **Permissions**: Ensure that you have permission to scan the target IPs or ports. Unauthorized scanning may violate network policies.
- **No Results**: If no open ports are found, ensure that the target IP is active and reachable.

