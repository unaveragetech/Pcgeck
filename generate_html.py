import json

HTML_TEMPLATE = """
<html><head><base href="/" /><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0"><title>IP Scan Report</title><style>
    body { 
        font-family: Arial, sans-serif; 
        margin: 20px;
        background: #f0f2f5;
    }
    .container {
        max-width: 1200px;
        margin: 0 auto;
        padding: 20px;
        background: white;
        border-radius: 8px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    h1 {
        color: #2c3e50;
        margin-bottom: 30px;
        border-bottom: 2px solid #3498db;
        padding-bottom: 10px;
    }
    table { 
        width: 100%; 
        border-collapse: collapse; 
        margin-top: 20px;
        background: white;
    }
    th, td { 
        border: 1px solid #dee2e6; 
        padding: 12px; 
        text-align: left; 
    }
    th { 
        background-color: #3498db; 
        color: white;
        font-weight: 500;
    }
    tr:nth-child(even) { 
        background-color: #f8f9fa; 
    }
    tr:hover {
        background-color: #e9ecef;
        transition: background-color 0.2s ease;
    }
    .status-cell {
        font-weight: bold;
    }
    .status-open {
        color: #2ecc71;
    }
    .status-closed {
        color: #e74c3c;
    }
    .ip-cell {
        font-family: monospace;
        font-size: 0.9em;
    }
    .refresh-button {
        padding: 10px 20px;
        background-color: #3498db;
        color: white;
        border: none;
        border-radius: 4px;
        cursor: pointer;
        margin-bottom: 20px;
    }
    .refresh-button:hover {
        background-color: #2980b9;
    }
    .timestamp {
        color: #7f8c8d;
        font-size: 0.9em;
        margin-bottom: 20px;
    }
    .loading {
        display: none;
        text-align: center;
        padding: 20px;
    }
    .spinner {
        width: 40px;
        height: 40px;
        margin: 0 auto;
        border: 4px solid #f3f3f3;
        border-top: 4px solid #3498db;
        border-radius: 50%;
        animation: spin 1s linear infinite;
    }
    @keyframes spin {
        0% { transform: rotate(0deg); }
        100% { transform: rotate(360deg); }
    }
</style></head>
<body>
    <div class="container">
        <h1>IP Scan Report</h1>
        <button class="refresh-button" onclick="refreshData()">Refresh Data</button>
        <div class="timestamp">Last updated: <span id="lastUpdate"></span></div>
        
        <div class="loading">
            <div class="spinner"></div>
            <p>Loading scan results...</p>
        </div>

        <table id="scanTable">
            <thead>
                <tr>
                    <th>IP Address</th>
                    <th>Port</th>
                    <th>Status</th>
                    <th>Hostname</th>
                </tr>
            </thead>
            <tbody id="tableBody">
            </tbody>
        </table>
    </div>

    <script>
        function updateTimestamp() {
            const now = new Date();
            document.getElementById('lastUpdate').textContent = now.toLocaleString();
        }

        function setLoading(isLoading) {
            document.querySelector('.loading').style.display = isLoading ? 'block' : 'none';
            document.getElementById('scanTable').style.display = isLoading ? 'none' : 'table';
        }

        function updateTable(data) {
            const tableBody = document.getElementById('tableBody');
            tableBody.innerHTML = '';
            
            data.forEach(entry => {
                const row = document.createElement('tr');
                row.innerHTML = `
                    <td class="ip-cell">${entry.ip}</td>
                    <td>${entry.port}</td>
                    <td class="status-cell ${entry.status.toLowerCase() === 'open' ? 'status-open' : 'status-closed'}">${entry.status}</td>
                    <td>${entry.hostname || 'N/A'}</td>
                `;
                tableBody.appendChild(row);
            });
        }

        async function refreshData() {
            try {
                setLoading(true);
                const response = await fetch('scan_results.json');
                if (!response.ok) throw new Error('Failed to fetch scan results');
                const data = await response.json();
                updateTable(data);
                updateTimestamp();
            } catch (error) {
                console.error('Error fetching scan results:', error);
                alert('Failed to load scan results. Please try again later.');
            } finally {
                setLoading(false);
            }
        }

        // Initial load
        window.addEventListener('load', () => {
            refreshData();
        });
    </script>
</body></html>
"""

def generate_html(data):
    rows = ""
    for entry in data:
        rows += f"""
        <tr>
            <td>{entry['ip']}</td>
            <td>{entry['port']}</td>
            <td>{entry['status']}</td>
            <td>{entry.get('hostname', 'N/A')}</td>
        </tr>
        """
    return HTML_TEMPLATE.format(rows=rows)

def main():
    # Load scan results from JSON
    with open('scan_results.json', 'r') as file:
        data = json.load(file)
    
    # Generate HTML content
    html_content = generate_html(data)
    
    # Write to index.html
    with open('index.html', 'w') as html_file:
        html_file.write(html_content)

if __name__ == "__main__":
    main()
