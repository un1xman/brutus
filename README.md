# Brutus
Lucius Junius Brutus is a famous Consul of the Roman Empire but here it is just a metric collector tool.With this tool you can collect consul's Prometheus metrics and
serve these with Custom Flask app 

### Requirments:
- Docker

### User Manual

```bash
 docker build --build-arg TOKEN='YOUR_CONSUL_AUTH_TOKEN' --build-arg URL="http://YOUR_CONSUL_ADDRESS/v1/agent/metrics?format=prometheus" -t brutus .
 docker run -itd --name brutus -p 5000:5000 brutus:latest
 ```