<!DOCTYPE html>
<html>
<head>
  <title>Protocol Upgrade Monitor</title>
  <link rel="stylesheet" href="/static/style.css">
</head>
<body>
  <h1>🔧 Protocol Upgrade Monitor</h1>
  <form method="post">
    <!-- form inputs from earlier version -->
    <input type="submit" value="Analyze">
  </form>
  {% if submitted %}
  <div class="dashboard">
    <div class="panel left">
      <h2>🌐 Network Monitoring</h2>
      <!-- ... -->
    </div>
    <div class="panel center">
      <h2>📅 Timeline & Risk</h2>
      <p><strong>Risk Score:</strong> {{ risk_score|round(2) }}</p>
    </div>
    <div class="panel right">
      <h2>📊 Execution Guidance</h2>
      <!-- ... -->
    </div>
  </div>
  {% endif %}
</body>
</html>