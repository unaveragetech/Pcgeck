import json

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>IP Scan Report</title>
    <style>
        body {{ font-family: Arial, sans-serif; margin: 20px; }}
        table {{ width: 100%; border-collapse: collapse; margin-top: 20px; }}
        th, td {{ border: 1px solid #ccc; padding: 8px; text-align: left; }}
        th {{ background-color: #f4f4f4; }}
        tr:nth-child(even) {{ background-color: #f9f9f9; }}
    </style>
</head>
<body>
    <h1>IP Scan Report</h1>
    <table>
        <thead>
            <tr>
                <th>IP Address</th>
                <th>Port</th>
                <th>Status</th>
                <th>Hostname</th>
            </tr>
        </thead>
        <tbody>
            {rows}
        </tbody>
    </table>
</body>
</html>
"""


def generate_html(data):
    rows = ""
    for entry in data:
        rows += f"""
        <tr>
            <td>{entry['ip']}</td>
            <td>{entry['port']}</td>
            <td>{entry['status']}</td>
            <td>{entry['hostname']}</td>
        </tr>
        """
    return HTML_TEMPLATE.format(rows=rows)

if __name__ == "__main__":
    with open("scan_results.json", "r") as f:
        data = json.load(f)
    
    html_content = generate_html(data)
    with open("index.html", "w") as f:
        f.write(html_content)
