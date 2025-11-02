# 🔢 VLSM Calculator - Professional Tool

Advanced VLSM Calculator với tính năng đầy đủ: auto-calculation, visualization, export, và validation.

<div id="vlsm-calculator-app">
  <style>
    .vlsm-calc-container {
      max-width: 1400px;
      margin: 0 auto;
      font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }

    .vlsm-header {
      background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
      color: white;
      padding: 40px;
      border-radius: 20px;
      text-align: center;
      margin-bottom: 30px;
      box-shadow: 0 10px 40px rgba(102, 126, 234, 0.3);
    }

    .vlsm-header h1 {
      margin: 0 0 10px 0;
      font-size: 2.5em;
    }

    .vlsm-header p {
      margin: 0;
      opacity: 0.9;
      font-size: 1.1em;
    }

    .vlsm-section {
      background: white;
      padding: 30px;
      border-radius: 15px;
      box-shadow: 0 5px 25px rgba(0,0,0,0.08);
      margin-bottom: 30px;
    }

    .vlsm-section h3 {
      color: #667eea;
      margin-top: 0;
      display: flex;
      align-items: center;
      gap: 10px;
    }

    .input-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
      gap: 20px;
      margin: 20px 0;
    }

    .input-group {
      display: flex;
      flex-direction: column;
    }

    .input-group label {
      font-weight: 600;
      margin-bottom: 8px;
      color: #495057;
      font-size: 14px;
    }

    .input-field {
      padding: 12px 15px;
      border: 2px solid #e9ecef;
      border-radius: 8px;
      font-size: 16px;
      transition: all 0.3s;
    }

    .input-field:focus {
      outline: none;
      border-color: #667eea;
      box-shadow: 0 0 0 3px rgba(102, 126, 234, 0.1);
    }

    .requirement-item {
      display: flex;
      gap: 15px;
      margin: 15px 0;
      padding: 15px;
      background: #f8f9fa;
      border-radius: 10px;
      align-items: center;
      transition: all 0.3s;
    }

    .requirement-item:hover {
      background: #e9ecef;
      transform: translateX(5px);
    }

    .requirement-item input {
      flex: 1;
      padding: 10px;
      border: 2px solid #dee2e6;
      border-radius: 6px;
      font-size: 15px;
    }

    .requirement-item input:focus {
      outline: none;
      border-color: #667eea;
    }

    .btn {
      padding: 12px 30px;
      border: none;
      border-radius: 25px;
      font-weight: 600;
      cursor: pointer;
      transition: all 0.3s;
      font-size: 15px;
    }

    .btn-primary {
      background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
      color: white;
    }

    .btn-primary:hover {
      transform: translateY(-2px);
      box-shadow: 0 5px 15px rgba(102, 126, 234, 0.4);
    }

    .btn-success {
      background: #00d4aa;
      color: white;
    }

    .btn-danger {
      background: #ff6b6b;
      color: white;
      padding: 8px 15px;
      font-size: 14px;
    }

    .btn-secondary {
      background: #6c757d;
      color: white;
    }

    .btn-icon {
      padding: 10px 20px;
      display: inline-flex;
      align-items: center;
      gap: 8px;
    }

    .controls {
      display: flex;
      gap: 15px;
      margin: 20px 0;
      flex-wrap: wrap;
    }

    .result-table {
      width: 100%;
      border-collapse: collapse;
      margin: 20px 0;
      font-size: 14px;
    }

    .result-table th,
    .result-table td {
      padding: 15px;
      text-align: left;
      border-bottom: 1px solid #dee2e6;
    }

    .result-table th {
      background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
      color: white;
      font-weight: 600;
      position: sticky;
      top: 0;
      z-index: 10;
    }

    .result-table tbody tr {
      transition: all 0.3s;
    }

    .result-table tbody tr:hover {
      background: #f8f9ff;
      transform: scale(1.01);
    }

    .result-table td {
      font-family: 'Courier New', monospace;
    }

    .subnet-name {
      font-weight: 600;
      color: #495057;
      font-family: 'Segoe UI', sans-serif;
    }

    .stats-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
      gap: 20px;
      margin: 20px 0;
    }

    .stat-card {
      background: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%);
      padding: 20px;
      border-radius: 12px;
      border-left: 4px solid #667eea;
    }

    .stat-label {
      font-size: 14px;
      color: #6c757d;
      font-weight: 600;
      text-transform: uppercase;
      letter-spacing: 0.5px;
    }

    .stat-value {
      font-size: 28px;
      font-weight: bold;
      color: #212529;
      margin-top: 5px;
    }

    .alert {
      padding: 15px 20px;
      border-radius: 10px;
      margin: 15px 0;
      display: flex;
      align-items: center;
      gap: 10px;
    }

    .alert-success {
      background: #d4edda;
      border-left: 4px solid #28a745;
      color: #155724;
    }

    .alert-warning {
      background: #fff3cd;
      border-left: 4px solid #ffc107;
      color: #856404;
    }

    .alert-danger {
      background: #f8d7da;
      border-left: 4px solid #dc3545;
      color: #721c24;
    }

    .alert-info {
      background: #d1ecf1;
      border-left: 4px solid #17a2b8;
      color: #0c5460;
    }

    .diagram-container {
      background: #f8f9fa;
      padding: 30px;
      border-radius: 12px;
      margin: 20px 0;
      overflow-x: auto;
    }

    .subnet-block {
      background: white;
      border: 2px solid #667eea;
      border-radius: 8px;
      padding: 15px;
      margin: 10px 0;
      display: inline-block;
      min-width: 200px;
    }

    .subnet-block strong {
      color: #667eea;
    }

    .progress-bar {
      background: #e9ecef;
      height: 30px;
      border-radius: 15px;
      overflow: hidden;
      margin: 10px 0;
      position: relative;
    }

    .progress-fill {
      height: 100%;
      background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
      transition: width 0.5s;
      display: flex;
      align-items: center;
      justify-content: center;
      color: white;
      font-weight: 600;
      font-size: 14px;
    }

    .copy-btn {
      background: #667eea;
      color: white;
      border: none;
      padding: 8px 15px;
      border-radius: 6px;
      cursor: pointer;
      font-size: 13px;
      transition: all 0.3s;
    }

    .copy-btn:hover {
      background: #5568d3;
    }

    .template-btn {
      background: #f8f9fa;
      border: 2px solid #dee2e6;
      padding: 15px;
      border-radius: 10px;
      cursor: pointer;
      margin: 10px;
      transition: all 0.3s;
      text-align: left;
    }

    .template-btn:hover {
      background: #e9ecef;
      border-color: #667eea;
      transform: translateY(-2px);
    }

    .template-btn h4 {
      margin: 0 0 5px 0;
      color: #667eea;
    }

    .template-btn p {
      margin: 0;
      font-size: 13px;
      color: #6c757d;
    }

    @media (max-width: 768px) {
      .result-table {
        font-size: 12px;
      }
      
      .result-table th,
      .result-table td {
        padding: 10px 5px;
      }

      .vlsm-header h1 {
        font-size: 1.8em;
      }

      .requirement-item {
        flex-direction: column;
        align-items: stretch;
      }

      .controls {
        flex-direction: column;
      }

      .btn {
        width: 100%;
      }
    }

    .hidden {
      display: none;
    }
  </style>

  <div class="vlsm-calc-container">
    <!-- Header -->
    <div class="vlsm-header">
      <h1>🔢 VLSM Calculator Pro</h1>
      <p>Professional Variable Length Subnet Mask Calculator với Visualization & Export</p>
    </div>

    <!-- Quick Templates -->
    <div class="vlsm-section">
      <h3>⚡ Quick Templates</h3>
      <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 15px;">
        <div class="template-btn" onclick="loadTemplate('small')">
          <h4>🏢 Small Office</h4>
          <p>50-100 users, 2-3 departments</p>
        </div>
        <div class="template-btn" onclick="loadTemplate('medium')">
          <h4>🏬 Medium Business</h4>
          <p>200-500 users, multiple sites</p>
        </div>
        <div class="template-btn" onclick="loadTemplate('enterprise')">
          <h4>🏭 Enterprise</h4>
          <p>1000+ users, multi-site, datacenter</p>
        </div>
        <div class="template-btn" onclick="loadTemplate('isp')">
          <h4>🌐 ISP / Service Provider</h4>
          <p>Multiple customers, P2P links</p>
        </div>
      </div>
    </div>

    <!-- Input Section -->
    <div class="vlsm-section">
      <h3>📝 Network Configuration</h3>
      
      <div class="input-grid">
        <div class="input-group">
          <label>Base Network (CIDR notation):</label>
          <input type="text" class="input-field" id="base-network" 
                 placeholder="192.168.1.0/24" value="192.168.1.0/24">
          <small style="color: #6c757d; margin-top: 5px;">Example: 10.0.0.0/16, 172.16.0.0/12</small>
        </div>
      </div>

      <h4 style="margin-top: 30px;">Subnet Requirements:</h4>
      <div id="requirements-container">
        <div class="requirement-item">
          <input type="text" placeholder="Subnet name (e.g., LAN A)" value="LAN A">
          <input type="number" placeholder="Hosts needed" value="100" min="1">
          <button class="btn btn-danger" onclick="removeRequirement(this)">✖ Remove</button>
        </div>
      </div>

      <div class="controls">
        <button class="btn btn-success btn-icon" onclick="addRequirement()">
          ➕ Add Requirement
        </button>
        <button class="btn btn-secondary btn-icon" onclick="addMultipleP2P()">
          🔗 Add 5 P2P Links
        </button>
      </div>
    </div>

    <!-- Calculate Button -->
    <div class="vlsm-section">
      <div class="controls">
        <button class="btn btn-primary btn-icon" onclick="calculateVLSM()">
          🔢 Calculate VLSM
        </button>
        <button class="btn btn-secondary btn-icon" onclick="resetCalculator()">
          🔄 Reset All
        </button>
        <button class="btn btn-success btn-icon" onclick="exportResults()">
          📤 Export Results
        </button>
        <button class="btn btn-secondary btn-icon" onclick="copyToClipboard()">
          📋 Copy Table
        </button>
      </div>
    </div>

    <!-- Results Section -->
    <div id="results-section" class="hidden">
      <!-- Statistics -->
      <div class="vlsm-section">
        <h3>📊 Statistics</h3>
        <div class="stats-grid">
          <div class="stat-card">
            <div class="stat-label">Total Subnets</div>
            <div class="stat-value" id="stat-subnets">0</div>
          </div>
          <div class="stat-card">
            <div class="stat-label">Total Hosts</div>
            <div class="stat-value" id="stat-hosts">0</div>
          </div>
          <div class="stat-card">
            <div class="stat-label">Addresses Used</div>
            <div class="stat-value" id="stat-used">0</div>
          </div>
          <div class="stat-card">
            <div class="stat-label">Remaining</div>
            <div class="stat-value" id="stat-remaining">0</div>
          </div>
        </div>

        <div class="progress-bar">
          <div class="progress-fill" id="usage-bar" style="width: 0%">0%</div>
        </div>

        <div id="usage-alerts"></div>
      </div>

      <!-- Results Table -->
      <div class="vlsm-section">
        <h3>📋 VLSM Allocation Table</h3>
        <div style="overflow-x: auto;">
          <table class="result-table" id="results-table">
            <thead>
              <tr>
                <th>#</th>
                <th>Subnet Name</th>
                <th>Required</th>
                <th>CIDR</th>
                <th>Subnet Mask</th>
                <th>Network</th>
                <th>First Host</th>
                <th>Last Host</th>
                <th>Broadcast</th>
                <th>Usable</th>
              </tr>
            </thead>
            <tbody id="results-tbody">
            </tbody>
          </table>
        </div>
      </div>

      <!-- Network Diagram -->
      <div class="vlsm-section">
        <h3>🗺️ Network Visualization</h3>
        <div class="diagram-container" id="network-diagram">
        </div>
      </div>

      <!-- Summary -->
      <div class="vlsm-section">
        <h3>📝 Configuration Summary</h3>
        <div id="config-summary"></div>
      </div>
    </div>
  </div>

  <script>
    // Utility functions
    function ipToInt(ip) {
      return ip.split('.').reduce((acc, octet) => (acc << 8) + parseInt(octet), 0) >>> 0;
    }

    function intToIp(int) {
      return [
        (int >>> 24) & 255,
        (int >>> 16) & 255,
        (int >>> 8) & 255,
        int & 255
      ].join('.');
    }

    function cidrToMask(cidr) {
      const mask = ~((1 << (32 - cidr)) - 1);
      return intToIp(mask >>> 0);
    }

    function addRequirement() {
      const container = document.getElementById('requirements-container');
      const div = document.createElement('div');
      div.className = 'requirement-item';
      div.innerHTML = `
        <input type="text" placeholder="Subnet name">
        <input type="number" placeholder="Hosts needed" min="1">
        <button class="btn btn-danger" onclick="removeRequirement(this)">✖ Remove</button>
      `;
      container.appendChild(div);
    }

    function removeRequirement(btn) {
      btn.parentElement.remove();
    }

    function addMultipleP2P() {
      for (let i = 1; i <= 5; i++) {
        const container = document.getElementById('requirements-container');
        const div = document.createElement('div');
        div.className = 'requirement-item';
        div.innerHTML = `
          <input type="text" placeholder="Subnet name" value="WAN Link ${i}">
          <input type="number" placeholder="Hosts needed" value="2" min="1">
          <button class="btn btn-danger" onclick="removeRequirement(this)">✖ Remove</button>
        `;
        container.appendChild(div);
      }
    }

    function calculateVLSM() {
      const baseNetwork = document.getElementById('base-network').value.trim();
      
      // Parse base network
      const match = baseNetwork.match(/^(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\/(\d{1,2})$/);
      if (!match) {
        alert('❌ Invalid network format! Use: 192.168.1.0/24');
        return;
      }

      const baseIp = match[1];
      const baseCidr = parseInt(match[2]);

      // Get requirements
      const items = document.querySelectorAll('.requirement-item');
      const requirements = [];

      items.forEach(item => {
        const inputs = item.querySelectorAll('input');
        const name = inputs[0].value.trim();
        const hosts = parseInt(inputs[1].value);

        if (name && hosts > 0) {
          requirements.push({ name, hosts });
        }
      });

      if (requirements.length === 0) {
        alert('❌ Please add at least one requirement!');
        return;
      }

      // Sort descending
      requirements.sort((a, b) => b.hosts - a.hosts);

      // Calculate subnets
      const subnets = [];
      let currentIpInt = ipToInt(baseIp);
      const baseNetwork = (currentIpInt & (~((1 << (32 - baseCidr)) - 1) >>> 0)) >>> 0;
      const baseSize = Math.pow(2, 32 - baseCidr);

      currentIpInt = baseNetwork;

      for (const req of requirements) {
        // Calculate required prefix
        let hostBits = 0;
        let capacity = 0;

        for (let h = 1; h <= 32; h++) {
          capacity = Math.pow(2, h) - 2;
          if (capacity >= req.hosts) {
            hostBits = h;
            break;
          }
        }

        const cidr = 32 - hostBits;
        const maskInt = ~((1 << hostBits) - 1) >>> 0;
        const blockSize = Math.pow(2, hostBits);

        // Align to block boundary
        currentIpInt = (Math.floor(currentIpInt / blockSize) * blockSize) >>> 0;

        const networkInt = currentIpInt;
        const broadcastInt = (networkInt + blockSize - 1) >>> 0;
        const firstHostInt = networkInt + 1;
        const lastHostInt = broadcastInt - 1;

        subnets.push({
          name: req.name,
          requiredHosts: req.hosts,
          cidr: cidr,
          network: intToIp(networkInt),
          firstHost: intToIp(firstHostInt),
          lastHost: intToIp(lastHostInt),
          broadcast: intToIp(broadcastInt),
          usableHosts: capacity,
          mask: cidrToMask(cidr),
          blockSize: blockSize
        });

        currentIpInt = broadcastInt + 1;

        // Check overflow
        if (currentIpInt > baseNetwork + baseSize) {
          alert('⚠️ Not enough IP addresses in base network!');
          break;
        }
      }

      // Display results
      displayResults(subnets, baseNetwork, baseSize, baseIp, baseCidr);
    }

    function displayResults(subnets, baseNetwork, baseSize, baseIp, baseCidr) {
      // Show results section
      document.getElementById('results-section').classList.remove('hidden');

      // Statistics
      const totalUsed = subnets.reduce((acc, s) => acc + s.blockSize, 0);
      const remaining = baseSize - totalUsed;
      const usagePercent = ((totalUsed / baseSize) * 100).toFixed(2);

      document.getElementById('stat-subnets').textContent = subnets.length;
      document.getElementById('stat-hosts').textContent = subnets.reduce((a, s) => a + s.requiredHosts, 0).toLocaleString();
      document.getElementById('stat-used').textContent = totalUsed.toLocaleString();
      document.getElementById('stat-remaining').textContent = remaining.toLocaleString();

      const usageBar = document.getElementById('usage-bar');
      usageBar.style.width = usagePercent + '%';
      usageBar.textContent = usagePercent + '% Used';

      // Usage alerts
      const alertsDiv = document.getElementById('usage-alerts');
      alertsDiv.innerHTML = '';

      if (usagePercent > 90) {
        alertsDiv.innerHTML = '<div class="alert alert-danger">⚠️ High usage! Consider using larger base network.</div>';
      } else if (usagePercent > 70) {
        alertsDiv.innerHTML = '<div class="alert alert-warning">⚠️ Moderate usage. Plan for growth.</div>';
      } else {
        alertsDiv.innerHTML = '<div class="alert alert-success">✅ Good! Plenty of room for expansion.</div>';
      }

      // Results table
      const tbody = document.getElementById('results-tbody');
      tbody.innerHTML = '';

      subnets.forEach((subnet, index) => {
        const row = tbody.insertRow();
        row.innerHTML = `
          <td>${index + 1}</td>
          <td class="subnet-name">${subnet.name}</td>
          <td>${subnet.requiredHosts}</td>
          <td>/${subnet.cidr}</td>
          <td>${subnet.mask}</td>
          <td>${subnet.network}</td>
          <td>${subnet.firstHost}</td>
          <td>${subnet.lastHost}</td>
          <td>${subnet.broadcast}</td>
          <td>${subnet.usableHosts}</td>
        `;
      });

      // Network diagram
      const diagram = document.getElementById('network-diagram');
      let diagramHTML = `<div style="font-family: monospace; line-height: 1.8;">`;
      diagramHTML += `<strong>Base Network: ${baseIp}/${baseCidr}</strong><br><br>`;

      subnets.forEach((subnet, i) => {
        const percent = ((subnet.blockSize / baseSize) * 100).toFixed(1);
        diagramHTML += `
          <div class="subnet-block">
            <strong>${subnet.name}</strong><br>
            Network: ${subnet.network}/${subnet.cidr}<br>
            Range: ${subnet.firstHost} - ${subnet.lastHost}<br>
            Hosts: ${subnet.usableHosts} (${percent}% of total)
          </div>
        `;
      });

      diagramHTML += `</div>`;
      diagram.innerHTML = diagramHTML;

      // Configuration summary
      const summary = document.getElementById('config-summary');
      let summaryHTML = '<div style="font-family: monospace; line-height: 2;">';
      summaryHTML += `<strong>Router Configuration Example:</strong><br><br>`;

      subnets.slice(0, 5).forEach(subnet => {
        summaryHTML += `interface ${subnet.name.replace(/ /g, '')}<br>`;
        summaryHTML += ` ip address ${subnet.firstHost} ${subnet.mask}<br>`;
        summaryHTML += ` description ${subnet.name}<br><br>`;
      });

      summaryHTML += `</div>`;
      summary.innerHTML = summaryHTML;

      // Scroll to results
      document.getElementById('results-section').scrollIntoView({ behavior: 'smooth' });
    }

    function resetCalculator() {
      document.getElementById('base-network').value = '192.168.1.0/24';
      document.getElementById('requirements-container').innerHTML = `
        <div class="requirement-item">
          <input type="text" placeholder="Subnet name" value="LAN A">
          <input type="number" placeholder="Hosts needed" value="100" min="1">
          <button class="btn btn-danger" onclick="removeRequirement(this)">✖ Remove</button>
        </div>
      `;
      document.getElementById('results-section').classList.add('hidden');
    }

    function loadTemplate(type) {
      const templates = {
        small: {
          network: '192.168.1.0/24',
          requirements: [
            { name: 'Main Office', hosts: 50 },
            { name: 'Guest WiFi', hosts: 30 },
            { name: 'Servers', hosts: 10 },
            { name: 'Printers', hosts: 5 },
            { name: 'WAN Link', hosts: 2 }
          ]
        },
        medium: {
          network: '172.16.0.0/16',
          requirements: [
            { name: 'Sales', hosts: 200 },
            { name: 'Engineering', hosts: 150 },
            { name: 'HR', hosts: 50 },
            { name: 'Branch Office', hosts: 100 },
            { name: 'Datacenter', hosts: 30 },
            { name: 'Guest WiFi', hosts: 50 },
            { name: 'WAN Link 1', hosts: 2 },
            { name: 'WAN Link 2', hosts: 2 }
          ]
        },
        enterprise: {
          network: '10.0.0.0/16',
          requirements: [
            { name: 'HQ Sales', hosts: 500 },
            { name: 'HQ Engineering', hosts: 400 },
            { name: 'Branch A', hosts: 200 },
            { name: 'Branch B', hosts: 200 },
            { name: 'Branch C', hosts: 150 },
            { name: 'Datacenter Prod', hosts: 100 },
            { name: 'Datacenter Dev', hosts: 50 },
            { name: 'Guest WiFi HQ', hosts: 100 },
            { name: 'Management', hosts: 20 }
          ]
        },
        isp: {
          network: '203.0.113.0/24',
          requirements: [
            { name: 'Customer A', hosts: 62 },
            { name: 'Customer B', hosts: 30 },
            { name: 'Customer C', hosts: 14 },
            { name: 'Customer D', hosts: 6 },
            { name: 'P2P Link 1', hosts: 2 },
            { name: 'P2P Link 2', hosts: 2 },
            { name: 'P2P Link 3', hosts: 2 }
          ]
        }
      };

      const template = templates[type];
      document.getElementById('base-network').value = template.network;

      const container = document.getElementById('requirements-container');
      container.innerHTML = '';

      template.requirements.forEach(req => {
        const div = document.createElement('div');
        div.className = 'requirement-item';
        div.innerHTML = `
          <input type="text" value="${req.name}">
          <input type="number" value="${req.hosts}" min="1">
          <button class="btn btn-danger" onclick="removeRequirement(this)">✖ Remove</button>
        `;
        container.appendChild(div);
      });

      alert(`✅ Loaded "${type}" template!`);
    }

    function exportResults() {
      const table = document.getElementById('results-table');
      if (!table || table.rows.length <= 1) {
        alert('❌ No results to export! Calculate VLSM first.');
        return;
      }

      let csv = 'VLSM Calculation Results\n\n';
      
      // Add table data
      for (let row of table.rows) {
        let rowData = [];
        for (let cell of row.cells) {
          rowData.push(cell.textContent);
        }
        csv += rowData.join(',') + '\n';
      }

      // Download
      const blob = new Blob([csv], { type: 'text/csv' });
      const url = URL.createObjectURL(blob);
      const a = document.createElement('a');
      a.href = url;
            a.download = 'vlsm_results.csv';
      document.body.appendChild(a);
      a.click();
      document.body.removeChild(a);
      URL.revokeObjectURL(url);
    }

    function copyToClipboard() {
      const table = document.getElementById('results-table');
      if (!table || table.rows.length <= 1) {
        alert('❌ No results to copy! Calculate VLSM first.');
        return;
      }

      let text = '';
      for (let row of table.rows) {
        let rowData = [];
        for (let cell of row.cells) {
          rowData.push(cell.textContent);
        }
        text += rowData.join('\t') + '\n';
      }

      navigator.clipboard.writeText(text)
        .then(() => alert('📋 Copied table to clipboard!'))
        .catch(err => alert('⚠️ Failed to copy: ' + err));
    }
  </script>
</div>
