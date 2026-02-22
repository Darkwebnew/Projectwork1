<div align="center">

# 🛡️ WAF AI
### AI-Powered Advanced Web Application Firewall

[![Python 3.8+](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=flat&logo=fastapi)](https://fastapi.tiangolo.com/)
[![Docker](https://img.shields.io/badge/Docker-Ready-blue.svg)](https://www.docker.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Tests](https://img.shields.io/badge/Tests-Passing-green.svg)](tests/)
[![ML](https://img.shields.io/badge/ML-scikit--learn-orange.svg)](https://scikit-learn.org/)

**Enterprise-grade web application security powered by machine learning — automatically detecting threats and deploying protective nginx rules in real-time.**

[🚀 Quick Start](#-quick-start) • [📖 API Docs](#-api-documentation) • [🏗️ Architecture](#-architecture) • [📸 Screenshots](#-screenshots) • [🧪 Testing](#-testing)

</div>

---

## 🌟 Project Overview

**WAF AI** is an intelligent, self-adapting Web Application Firewall built as a Final Year Project at Saveetha Engineering College. It combines traditional WAF capabilities with machine learning to deliver real-time threat detection, automated rule generation, and seamless multi-node nginx deployment — all managed through a professional control panel.

> **Supervisor:** Ms. V. Swedha, Saveetha Engineering College  
> **Academic Year:** 2024–2025

### 🎯 Problem Statement

Traditional firewalls rely on static, manually maintained rules that cannot adapt to evolving attack patterns. WAF AI addresses this by learning from live traffic, classifying threats using ML models, and autonomously deploying updated protection rules — eliminating the need for constant human intervention.

---

## ✨ Key Features

| Feature | Description |
|---------|-------------|
| 🧠 **AI Threat Detection** | Dual-model ML: Isolation Forest (anomaly) + Random Forest (classification) |
| ⚡ **Real-Time Processing** | Sub-second detection with continuous nginx traffic analysis |
| 🤖 **Automated Rule Generation** | ML predictions automatically converted to nginx WAF rules |
| 🌐 **Multi-Node Orchestration** | SSH-based rule deployment across nginx clusters |
| 🎛️ **Control Panel** | Professional web UI for complete system management |
| 🔒 **RBAC Authentication** | JWT-based auth with Admin / Operator / Viewer roles |
| 📊 **Full Observability** | Prometheus metrics, Grafana dashboards, Loki log aggregation |
| 🐳 **Docker-Ready** | Full Docker Compose stack with 8+ services |
| 🧪 **Comprehensive Tests** | 9 test suites covering unit, integration, API, E2E, performance, and security |

---

## 🏗️ Architecture

<div align="center">

![WAF AI Architecture](screenshot/Architecture%20Diagram.png)

*End-to-end system architecture: traffic ingestion → ML analysis → rule generation → nginx deployment*

</div>

### 🧩 System Components

| Component | File | Technology | Purpose |
|-----------|------|-----------|---------|
| 🌐 **Traffic Collector** | `src/traffic_collector.py` | Python, asyncio | HTTP traffic ingestion & feature extraction |
| 🧠 **ML Engine** | `src/ml_engine.py` | scikit-learn | Anomaly detection & threat classification |
| ⚙️ **WAF Rule Generator** | `src/waf_rule_generator.py` | Custom engine | Converts ML predictions to nginx rules |
| 🚀 **Nginx Manager** | `src/nginx_manager.py` | SSH, nginx | Multi-node config deployment |
| 🔌 **API Server** | `src/main.py` | FastAPI | RESTful API + WebSockets |
| 🎛️ **Control Panel** | `docker/control-panel/` | HTML5/CSS3/JS | Web-based management interface |
| 🔐 **Auth & RBAC** | `src/auth.py` | JWT | Role-based access control |
| 📊 **Metrics** | `src/metrics.py` | Prometheus | System observability |

### 🔄 Request Processing Flow

```
Client Request
     │
     ▼
Nginx Load Balancer (ports 8081, 8082)
     │
     ▼
Traffic Collector → Feature Extraction (15+ features)
     │
     ▼
ML Engine → Isolation Forest + Random Forest
     │
     ▼
Decision: ALLOW / BLOCK / RATE-LIMIT
     │
     ▼
WAF Rule Generator → Nginx Config Syntax
     │
     ▼
Nginx Manager → SSH Deploy to All Nodes
     │
     ▼
Grafana + Prometheus + Loki → Monitoring
```

---

## 📸 Screenshots

<div align="center">

| Control Panel Dashboard | Threat Detection View |
|------------------------|----------------------|
| ![Dashboard](screenshot/WAF%20AI%20Control%20Panel%20Dashboard%20–%20First%20Half.jpg) | ![Threats](screenshot/WAF%20AI%20Control%20Panel%20–%20Threat%20Detection%20View.jpg) |

| Traffic Monitoring | WAF Rules Management |
|--------------------|---------------------|
| ![Traffic](screenshot/WAF%20AI%20Control%20Panel%20–%20Traffic%20Monitoring%20%26%20Control.jpg) | ![Rules](screenshot/WAF%20AI%20Control%20Panel%20–%20WAF%20Rules%20Management.jpg) |

| ML Engine Status | Grafana – Threat Metrics |
|-----------------|--------------------------|
| ![ML](screenshot/WAF%20AI%20Control%20Panel%20–%20Machine%20Learning%20Engine.jpg) | ![Grafana](screenshot/Grafana%20–%20Threat%20Detection%20Metrics%20Dashboard.jpg) |

| Grafana – Traffic Analytics | Prometheus Health |
|-----------------------------|------------------|
| ![GrafanaTraffic](screenshot/Grafana%20–%20Traffic%20Analytics%20Dashboard.jpg) | ![Prometheus](screenshot/Prometheus%20–%20WAF%20API%20Target%20Health%20Status.jpg) |

| Docker Containers Running | VS Code – Source Code |
|--------------------------|----------------------|
| ![Docker](screenshot/Docker%20Desktop%20–%20Running%20WAF%20AI%20Containers.jpg) | ![VSCode](screenshot/Visual%20Studio%20Code%20–%20WAF%20AI%20Project%20Source%20Code.jpg) |

</div>

---

## 📂 Project Structure

```plaintext
Projectwork1/
│
├── 📁 config/                          # Configuration files
│   ├── waf_ai_config.json             # Main system configuration
│   ├── nginx_nodes_docker.json        # Docker nginx nodes config
│   └── nginx_nodes_example.json       # Example nodes template
│
├── 📁 docker/                          # Docker service definitions
│   ├── control-panel/                 # Web UI container
│   │   ├── Dockerfile
│   │   ├── control-panel.html         # Main UI
│   │   └── nginx.conf                 # Proxy config
│   ├── grafana/provisioning/          # Grafana dashboards & datasources
│   │   └── dashboards/
│   │       └── master-waf-dashboard.json
│   ├── nginx-node-1/                  # Test nginx node 1 (port 8081)
│   ├── nginx-node-2/                  # Test nginx node 2 (port 8082)
│   ├── prometheus/prometheus.yml      # Prometheus scrape config
│   ├── loki/loki-config.yml           # Log aggregation
│   ├── promtail/                      # Log shipping agents
│   ├── log-server/                    # Centralized log server
│   └── traffic-generator/             # Simulated traffic for testing
│
├── 📁 src/                             # Core application source
│   ├── main.py                        # FastAPI server (25+ endpoints)
│   ├── ml_engine.py                   # Isolation Forest + Random Forest
│   ├── traffic_collector.py           # Traffic ingestion pipeline
│   ├── waf_rule_generator.py          # Rule generation engine
│   ├── nginx_manager.py               # Multi-node deployment
│   ├── auth.py                        # JWT + RBAC
│   ├── metrics.py                     # Prometheus metrics
│   ├── config.py                      # Configuration management
│   ├── security_middleware.py         # Request validation
│   ├── error_handling.py              # Error management
│   ├── validation.py                  # Input validation
│   └── training_data_generator.py    # ML training data generation
│
├── 📁 tests/                           # Test suites
│   ├── conftest.py                    # Shared fixtures
│   ├── test_ml_engine.py              # ML model tests
│   ├── test_traffic_collector.py      # Traffic tests
│   ├── test_waf_rule_generator.py     # Rule generation tests
│   ├── test_nginx_manager.py          # Deployment tests
│   ├── test_auth.py                   # Auth & RBAC tests
│   ├── test_api_integration.py        # API endpoint tests
│   ├── test_e2e_integration.py        # End-to-end workflow
│   ├── test_performance.py            # Load testing
│   └── test_status_endpoints.py      # Health check tests
│
├── 📁 models/
│   └── waf_model.joblib               # Pre-trained ML model
│
├── 📁 scripts/
│   ├── bootstrap.py                   # First-run setup
│   ├── quick_start.py                 # Quick launch helper
│   ├── verify-system.py              # System health verification
│   └── start-waf-system.sh           # Full stack startup script
│
├── 📁 documents/                       # Academic documents
│   ├── REPORT.pdf                     # Full project report
│   ├── FINAL PPT.pdf                  # Presentation slides
│   ├── IEEE_Conference_WAF_AI.pdf     # IEEE conference paper
│   └── IEEE_Journal_Paper_WAF_AI.pdf  # IEEE journal paper
│
├── 📁 screenshot/                      # System screenshots (16 images)
├── 📄 docker-compose.yml              # Full stack orchestration
├── 📄 requirements.txt                # Python dependencies
├── 📄 test-requirements.txt           # Test dependencies
├── 📄 run_server.py                   # Application entry point
├── 📄 cli.py                          # Command-line interface
├── 📄 setup.sh                        # Automated setup script
├── 📄 pytest.ini                      # Test configuration
├── 📄 API.md                          # Full API reference
├── 📄 QUICKSTART.md                   # 5-minute setup guide
└── 📄 README.md                       # This file
```

---

## 🛠️ Installation

### 📋 Prerequisites

```
✓ Python 3.8+
✓ Docker & Docker Compose
✓ Git
✓ 4GB+ RAM (8GB recommended)
✓ 10GB+ disk space
```

### 🐳 Option 1: Docker Compose (Recommended)

```bash
# Clone the repository
git clone https://github.com/Darkwebnew/Projectwork1.git
cd Projectwork1

# Start the full stack (8 services)
docker-compose up -d

# Verify all containers are running
docker-compose ps

# Check system health
curl http://localhost:8000/health
```

**Services launched:**

| Service | Port | Purpose |
|---------|------|---------|
| WAF AI API | 8000 | Core API server |
| Control Panel | 8090 | Web management UI |
| Redis | 6379 | Session & cache store |
| Prometheus | 9090 | Metrics collection |
| Grafana | 3080 | Visualization dashboards |
| Loki | 3100 | Log aggregation |
| Nginx Node 1 | 8081 | Test nginx node |
| Nginx Node 2 | 8082 | Test nginx node |

### 🐍 Option 2: Local Development

```bash
# Clone and enter project
git clone https://github.com/Darkwebnew/Projectwork1.git
cd Projectwork1

# Create and activate virtual environment
python -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
pip install -r test-requirements.txt   # For testing

# Configure environment
cp .env.example .env
# Edit .env with your settings

# Start Redis (required)
redis-server

# Bootstrap first-run setup
python scripts/bootstrap.py

# Launch the API server
python run_server.py
```

### ⚡ Quick Start Script

```bash
# Automated one-command setup (Linux/macOS)
chmod +x setup.sh && ./setup.sh

# Or use the Python quick start helper
python scripts/quick_start.py

# Verify everything is working
python scripts/verify-system.py
```

---

## 🚀 Quick Start

### Step 1 — Authenticate

```bash
# Get your JWT token
TOKEN=$(curl -s -X POST "http://localhost:8000/auth/login" \
  -H "Content-Type: application/json" \
  -d '{"username":"admin","password":"admin123"}' | jq -r '.access_token')
```

> ⚠️ **Security Note:** Change the default admin password immediately in production via `WAF_ADMIN_PASSWORD` environment variable.

### Step 2 — Train the ML Model

```bash
# Train with sample data
curl -X POST "http://localhost:8000/api/training/start" \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  -d @data/sample_training_data.json

# Or use the CLI
python cli.py train \
  --training-data data/sample_training_data.json \
  --model-output models/waf_model.joblib
```

### Step 3 — Start Traffic Monitoring

```bash
# Start traffic collection from nginx nodes
curl -X POST "http://localhost:8000/api/traffic/start-collection" \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  -d '["http://localhost:8081", "http://localhost:8082"]'

# Start real-time threat processing
curl -X POST "http://localhost:8000/api/processing/start" \
  -H "Authorization: Bearer $TOKEN"
```

### Step 4 — View Threats & Deploy Rules

```bash
# View detected threats
curl "http://localhost:8000/api/threats?limit=10" \
  -H "Authorization: Bearer $TOKEN" | jq

# Deploy WAF rules to all nodes
curl -X POST "http://localhost:8000/api/rules/deploy" \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"node_ids": ["nginx-node-1", "nginx-node-2"], "force_deployment": false}'
```

### Step 5 — Access Dashboards

| Dashboard | URL | Credentials |
|-----------|-----|-------------|
| 🎛️ Control Panel | http://localhost:8090 | — |
| 📖 API Docs (Swagger) | http://localhost:8000/docs | — |
| 📊 Grafana | http://localhost:3080 | admin / waf-admin |
| 🔍 Prometheus | http://localhost:9090 | — |

---

## 🎛️ Control Panel

The WAF AI Control Panel is a professional, single-page web application containerized with nginx. It provides complete system management without touching the CLI.

**Six management sections:**

- **Traffic Control** — Start/stop collection, view request rates
- **ML Engine** — One-click training, model accuracy, status
- **Threat Detection** — Start/stop analysis, live detection counts
- **WAF Rules** — Generate, deploy, expire, and clean up rules
- **System Health** — Component health, uptime, memory usage
- **Master Control** — Start/stop/restart the entire system at once

Real-time status refreshes every 30 seconds. Fully responsive across desktop, tablet, and mobile.

---

## 📖 API Documentation

Full interactive API docs are available at **http://localhost:8000/docs** (Swagger UI) and **http://localhost:8000/redoc**.

### Authentication

```bash
# Login
curl -X POST "http://localhost:8000/auth/login" \
  -H "Content-Type: application/json" \
  -d '{"username": "admin", "password": "your_password"}'

# Response: { "access_token": "eyJ...", "token_type": "bearer" }
```

**Roles:** Admin (full access) · Operator (training, deployment, rules) · Viewer (read-only)

### Core Endpoints

| Category | Method | Endpoint | Role |
|----------|--------|----------|------|
| **Auth** | POST | `/auth/login` | Public |
| | POST | `/auth/users` | Admin |
| **Nodes** | POST | `/api/nodes/add` | Admin |
| | GET | `/api/nodes/status` | Viewer |
| **ML** | POST | `/api/training/start` | Operator |
| | GET | `/api/ml/model-info` | Viewer |
| | POST | `/api/ml/predict` | Operator |
| **Traffic** | POST | `/api/traffic/start-collection` | Operator |
| | GET | `/api/traffic/stats` | Viewer |
| **Rules** | GET | `/api/rules` | Viewer |
| | POST | `/api/rules/deploy` | Admin |
| | POST | `/api/rules/rollback` | Admin |
| **Threats** | GET | `/api/threats` | Viewer |
| | GET | `/api/threats/stats` | Viewer |
| | POST | `/api/threats/whitelist` | Admin |
| **Health** | GET | `/health` | Public |
| | GET | `/api/stats` | Viewer |
| | GET | `/metrics` | Viewer |

See [API.md](API.md) for complete request/response schemas.

---

## ⚙️ Configuration

### Environment Variables

```bash
# Server
WAF_API_HOST=0.0.0.0
WAF_API_PORT=8000

# Security (required — change in production)
WAF_JWT_SECRET=your-256-bit-secret-key
WAF_ADMIN_PASSWORD=secure-admin-password

# Redis
REDIS_URL=redis://localhost:6379

# ML Engine
WAF_THREAT_THRESHOLD=-0.5
WAF_CONFIDENCE_THRESHOLD=0.8
WAF_MODEL_PATH=models/waf_model.joblib

# Nginx Management
WAF_SSH_KEY_PATH=~/.ssh/nginx_key
WAF_NGINX_RELOAD_CMD=sudo systemctl reload nginx
```

Full configuration reference in `config/waf_ai_config.json`.

---

## 🧪 Testing

WAF AI includes 9 dedicated test files covering every system layer.

```bash
# Install test dependencies
pip install -r test-requirements.txt

# Run the full test suite
pytest tests/ -v

# Run by category
pytest tests/test_ml_engine.py          # ML model accuracy
pytest tests/test_traffic_collector.py  # Data ingestion
pytest tests/test_waf_rule_generator.py # Rule generation
pytest tests/test_nginx_manager.py      # Deployment
pytest tests/test_auth.py              # Auth & RBAC
pytest tests/test_api_integration.py   # API endpoints
pytest tests/test_e2e_integration.py   # End-to-end workflow
pytest tests/test_performance.py       # Load & stress testing
pytest tests/test_status_endpoints.py  # Health checks

# With coverage report
pytest tests/ --cov=src --cov-report=html --cov-report=term-missing

# Parallel execution
pytest tests/ -n auto
```

### Coverage Summary

| Module | Coverage |
|--------|----------|
| ML Engine | 95% |
| Traffic Collector | 92% |
| Authentication | 90% |
| WAF Rule Generator | 88% |
| API Integration | 85% |
| Nginx Manager | 80% |

---

## 🔒 Security

### Production Checklist

- Change all default credentials before deployment
- Set a 256-bit random `WAF_JWT_SECRET`
- Enable HTTPS/TLS (`WAF_USE_HTTPS=true`)
- Restrict management port access via firewall
- Use dedicated SSH keys for nginx nodes
- Enable rate limiting (`WAF_RATE_LIMIT_REQUESTS`)

### SSH Key Setup for Nginx Nodes

```bash
# Generate dedicated key
ssh-keygen -t ed25519 -f ~/.ssh/nginx_waf_key -N ""

# Set permissions
chmod 600 ~/.ssh/nginx_waf_key
```

### Emergency Procedures

```bash
# Emergency shutdown
curl -X POST "http://localhost:8000/api/security/emergency-shutdown" \
  -H "Authorization: Bearer $ADMIN_TOKEN"

# Rollback all nginx configs
python cli.py rollback --all-nodes --emergency

# Block an IP range
curl -X POST "http://localhost:8000/api/security/block-ip-range" \
  -H "Authorization: Bearer $ADMIN_TOKEN" \
  -d '{"cidr": "192.168.1.0/24", "reason": "security_incident"}'
```

---

## 📊 Monitoring & Observability

The full monitoring stack is included in Docker Compose:

| Service | Port | Purpose |
|---------|------|---------|
| Grafana | 3080 | Dashboards & alerting |
| Prometheus | 9090 | Metrics collection |
| Loki | 3100 | Log aggregation |
| Promtail | — | Log shipping from nginx nodes |

Pre-built Grafana dashboard at `docker/grafana/provisioning/dashboards/master-waf-dashboard.json` covers threat detection rate, traffic volume, ML inference time, nginx node health, and rule deployment history.

---

## 🔧 CLI Reference

```bash
# Train ML model
python cli.py train --training-data data/requests.json --labels data/labels.json

# Check cluster status
python cli.py status --nodes-config config/nginx_nodes.json

# Collect traffic
python cli.py collect --nodes-config config/nginx_nodes.json --duration 3600

# Generate and deploy rules
python cli.py generate-rules --threats-file data/threats.json --output rules/new.conf
python cli.py deploy --nodes-config config/nginx_nodes.json --rules-file rules/waf_rules.conf

# Security audit
python cli.py security audit-configs --all-nodes
```

---

## 📚 Research & Documentation

This project is backed by peer-reviewed research available in the `documents/` folder:

- 📄 **IEEE Conference Paper** — WAF AI threat detection methodology
- 📰 **IEEE Journal Paper** — Extended ML-based WAF research
- 📋 **Full Project Report** — System design, implementation & results
- 🎓 **Presentation Slides** — Project defense presentation

---

## 👥 Team

| Name | Role | GitHub |
|------|------|--------|
| **Sriram V** | Project Lead & Developer | [@darkwebnew](https://github.com/darkwebnew) |
| **Surothaaman R** | Contributor | [@surothaaman](https://github.com/surothaaman) |
| **Pavithra M** | Contributor | [@22008686](https://github.com/22008686) |

**Academic Supervisor:** Ms. V. Swedha  
**Institution:** Saveetha Engineering College

---

## 🤝 Contributing

1. Fork the repository
2. Create your branch: `git checkout -b feature/YourFeature`
3. Write tests for your changes
4. Ensure all checks pass: `pytest tests/ && black src/ && flake8 src/`
5. Commit: `git commit -m 'Add YourFeature'`
6. Push and open a Pull Request

Please read [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) before contributing.

---

## 📄 License

This project is licensed under the **MIT License** — see [LICENSE](LICENSE) for details.

---

## 🙏 Acknowledgments

- **scikit-learn** — ML algorithms (Isolation Forest, Random Forest)
- **FastAPI** — High-performance async API framework
- **nginx** — Robust web server & reverse proxy
- **Prometheus & Grafana** — Industry-standard observability stack
- **Docker** — Containerization and deployment
- **pytest** — Comprehensive testing framework
- **Saveetha Engineering College** — Academic support and guidance
- **OWASP** — Security research and Top 10 threat classifications

---

<div align="center">

**⭐ Star this repository if you find it useful!**

Made with ❤️ for the cybersecurity community  
[Report Issues](https://github.com/Darkwebnew/Projectwork1/issues) · [Request Features](https://github.com/Darkwebnew/Projectwork1/issues) · [API Docs](API.md)

</div>
