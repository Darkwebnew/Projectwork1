<div align="center">

# 🛡️ WAF AI
### AI-Powered Advanced Web Application Firewall

[![License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.8+-green.svg)](https://www.python.org/)
[![Docker](https://img.shields.io/badge/Docker-Ready-blue.svg)](https://www.docker.com/)
[![AI](https://img.shields.io/badge/AI-TensorFlow%20%7C%20PyTorch-orange.svg)](https://www.tensorflow.org/)

**Enterprise-grade web security powered by advanced machine learning for real-time threat detection and intelligent response.**

[🚀 Quick Start](#-installation) • [📖 Documentation](API.md) • [🎯 Demo](#-demo) • [🤝 Contributing](#-contributing)

</div>

---

## 🌟 Project Overview

**WAF AI** is an intelligent Web Application Firewall (WAF) that leverages cutting-edge machine learning to protect web applications from sophisticated cyber threats. Built as a comprehensive Final Year Project, it seamlessly integrates traditional WAF capabilities with AI-driven threat intelligence to deliver superior, adaptive protection.

### 🎯 Why WAF AI?

Traditional firewalls rely on static rules—WAF AI learns, adapts, and evolves with emerging threats, providing proactive defense for modern web applications.

---

## ✨ Key Features

<table>
<tr>
<td width="50%">

### 🧠 **AI-Powered Threat Detection**
Advanced machine learning models identify attack patterns in real-time, adapting to new threat vectors automatically.

### ⚡ **Real-Time Protection**
Continuous traffic analysis with sub-millisecond anomaly detection ensures zero-delay response to threats.

### 🤖 **Automated Response**
Intelligent blocking, rate limiting, and threat mitigation execute automatically without manual intervention.

</td>
<td width="50%">

### 📊 **Comprehensive Logging**
Detailed audit trails with ELK Stack integration provide full visibility into security events and system performance.

### ⚖️ **Load Balancing**
Nginx-based intelligent request distribution ensures high availability and optimal performance under load.

### 🐳 **Scalable Architecture**
Docker-based containerized deployment enables seamless horizontal scaling and cloud-native operations.

</td>
</tr>
</table>

---

## 🏗️ Architecture

<div align="center">

![WAF AI Architecture](https://user-gen-media-assets.s3.amazonaws.com/seedream_images/56cde672-55dc-420b-b49b-a4aaea78efc6.png)

*Figure 1: End-to-end WAF AI system architecture showcasing microservices design, ML engine integration, real-time dashboard, and cloud deployment.*

</div>

### 🔧 Core Components

The WAF AI system employs a **microservices architecture** optimized for scalability, reliability, and performance:

| Component | Technology | Purpose |
|-----------|-----------|----------|
| **🌐 Load Balancer** | Nginx | Reverse proxy for intelligent traffic distribution and SSL termination |
| **🛡️ WAF Processing Nodes** | Python/Flask | Multiple instances providing high availability and request processing |
| **🧠 ML Engine** | TensorFlow/PyTorch | Real-time threat detection using trained neural network models |
| **💾 Database Layer** | MongoDB + Redis | Data persistence, caching, and session management |
| **📈 Monitoring & Analytics** | ELK Stack + Grafana | Real-time dashboards, alerting, and performance metrics |
| **🔌 API Gateway** | FastAPI | RESTful APIs for configuration, management, and integrations |
| **🐳 Container Orchestration** | Docker Compose | Service orchestration and deployment automation |

### 🔄 Request Flow

1. **Client Request** → Load Balancer receives incoming traffic
2. **Traffic Analysis** → WAF node inspects request headers, payload, and patterns
3. **ML Processing** → Machine learning engine evaluates threat probability
4. **Decision Engine** → Automated allow/block/challenge decision
5. **Response** → Protected application receives clean traffic only
6. **Logging** → All events logged for analytics and compliance

---

## 🚀 Installation

### 📋 Prerequisites

Before installation, ensure your system meets these requirements:

```bash
✓ Python 3.8 or higher
✓ Docker & Docker Compose
✓ Git
✓ 4GB+ RAM (8GB recommended)
✓ 10GB+ disk space
```

### 🔧 Setup Steps

#### 1️⃣ Clone the Repository

```bash
git clone https://github.com/Darkwebnew/CyberGuard-AI.git
cd CyberGuard-AI
```

#### 2️⃣ Configure Environment

```bash
# Copy environment template
cp .env.example .env

# Edit configuration (set API keys, database credentials, etc.)
nano .env
```

#### 3️⃣ Install Dependencies

```bash
# Create virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install required packages
pip install -r requirements.txt
```

#### 4️⃣ Initialize Database

```bash
# Run database migrations
python scripts/init_db.py

# Load ML models
python scripts/load_models.py
```

#### 5️⃣ Launch Services

**Option A: Docker Deployment (Recommended)**

```bash
# Build and start all services
docker-compose up -d

# Verify services are running
docker-compose ps
```

**Option B: Manual Deployment**

```bash
# Start the WAF server
python run_server.py

# In separate terminals:
python src/ml_engine.py    # ML processing
python src/monitor.py       # Monitoring dashboard
```

#### 6️⃣ Verify Installation

```bash
# Check system health
curl http://localhost:8080/health

# Access dashboard
Open browser: http://localhost:3000
```

### 🎯 Quick Start Script

```bash
# Automated setup (Linux/macOS)
chmod +x setup.sh
./setup.sh
```

---

## 🎬 Demo

### 💻 Sample Commands

**Test WAF Protection:**

```bash
# Normal request (should pass)
curl http://localhost:8080/api/test

# SQL injection attempt (should block)
curl "http://localhost:8080/api/test?id=1' OR '1'='1"

# XSS attempt (should block)
curl "http://localhost:8080/api/test?input=<script>alert('XSS')</script>"
```

**View Real-Time Analytics:**

```bash
# Access monitoring dashboard
open http://localhost:3000/dashboard

# View threat logs
curl http://localhost:8080/api/logs/threats
```

### 📸 Screenshots

<div align="center">

| Dashboard | Threat Detection | Analytics |
|-----------|-----------------|----------|
| ![Dashboard](https://github.com/Darkwebnew/CyberGuard-AI/blob/main/screenshot/04aca83db9e8432d8c7b484159382216.jpg) | ![Detection](https://github.com/Darkwebnew/CyberGuard-AI/blob/main/screenshot/a0111aa79d404077ae98925567a1c8cc.jpg) | ![Analytics](https://github.com/Darkwebnew/CyberGuard-AI/blob/main/screenshot/WhatsApp%20Image%202025-10-29%20at%2023.17.18_e04ecad6.jpg) |
| Real-time security monitoring | ML-powered threat identification | Comprehensive attack analytics |

</div>

> **Note:** Screenshots are located in the `/screenshot` directory. View them [here](screenshot/).

---

## 📂 Project Structure

```plaintext
CyberGuard-AI/
│
├── 📁 config/                  # Configuration files
│   ├── waf.yml                # WAF rules and policies
│   ├── ml_models.json         # ML model configurations
│   └── nginx.conf             # Load balancer settings
│
├── 📁 docker/                  # Docker configurations
│   ├── Dockerfile.waf         # WAF container
│   └── Dockerfile.ml          # ML engine container
│
├── 📁 models/                  # Pre-trained ML models
│   ├── threat_detector.h5     # Neural network model
│   └── anomaly_detector.pkl   # Anomaly detection model
│
├── 📁 screenshot/              # Application screenshots
│   ├── dashboard.png          # Main dashboard
│   ├── detection.png          # Threat detection view
│   └── analytics.png          # Analytics interface
│
├── 📁 scripts/                 # Utility scripts
│   ├── init_db.py            # Database initialization
│   ├── load_models.py        # Model loader
│   └── train_model.py        # ML training pipeline
│
├── 📁 src/                     # Source code
│   ├── api/                  # API endpoints
│   ├── core/                 # Core WAF logic
│   ├── ml/                   # Machine learning modules
│   ├── monitoring/           # Monitoring and logging
│   └── utils/                # Helper functions
│
├── 📁 tests/                   # Test suites
│   ├── test_api.py           # API tests
│   ├── test_ml.py            # ML model tests
│   └── test_integration.py   # Integration tests
│
├── 📄 .env.example             # Environment template
├── 📄 docker-compose.yml       # Docker orchestration
├── 📄 requirements.txt         # Python dependencies
├── 📄 run_server.py            # Main application entry
├── 📄 setup.sh                 # Automated setup script
├── 📄 API.md                   # API documentation
├── 📄 LICENSE                  # MIT License
└── 📄 README.md                # This file
```

---

## 🧪 Testing

### Run Test Suite

```bash
# Run all tests
pytest tests/ -v

# Run specific test categories
pytest tests/test_api.py          # API tests
pytest tests/test_ml.py           # ML tests
pytest tests/test_integration.py  # Integration tests

# Generate coverage report
pytest --cov=src --cov-report=html
```

---

## 📚 Documentation

- **[API Documentation](API.md)** - Complete API reference
- **[Quick Start Guide](QUICKSTART.md)** - Get started in 5 minutes
- **[Configuration Guide](config/README.md)** - Detailed configuration options
- **[ML Model Training](models/README.md)** - Train custom models

---

## 🤝 Contributing

We welcome contributions! Please see our **[Code of Conduct](CODE_OF_CONDUCT.md)** for guidelines.

### How to Contribute:

1. **Fork** the repository
2. **Create** a feature branch: `git checkout -b feature/AmazingFeature`
3. **Commit** your changes: `git commit -m 'Add AmazingFeature'`
4. **Push** to the branch: `git push origin feature/AmazingFeature`
5. **Open** a Pull Request

---

## 📄 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for complete details.

```
MIT License - Copyright (c) 2024 WAF AI Team

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software.
```

---

## 👥 Team

| Avatar | Name | Role | GitHub |
|--------|------|------|--------|
| <img src="https://avatars.githubusercontent.com/u/143114486?v=4" width="80" height="80" style="border-radius: 50%;"> | **Sriram V** | Project Lead & Developer | [![GitHub](https://img.shields.io/badge/GitHub-Profile-black?logo=github)](https://github.com/darkwebnew) |
| <img src="https://avatars.githubusercontent.com/u/133313653?v=4" width="80" height="80" style="border-radius: 50%;"> | **Surothaaman R** | Contributor | [![GitHub](https://img.shields.io/badge/GitHub-Profile-black?logo=github)](https://github.com/surothaaman) |
| <img src="https://avatars.githubusercontent.com/u/118916413?v=4" width="80" height="80" style="border-radius: 50%;"> | **Pavithra M** | Contributor | [![GitHub](https://img.shields.io/badge/GitHub-Profile-black?logo=github)](https://github.com/22008686) |

---

## 🙏 Acknowledgments

<div align="center">

### Special Thanks

**🎓 Academic Guidance**  
Ms.V.Swedha, Project Supervisor  
Saveetha Engineering College

**🔬 Research Foundations**  
Built upon research in adversarial ML, OWASP Top 10, and modern WAF architectures

**🛠️ Open Source Technologies**  
TensorFlow • PyTorch • Flask • Docker • Nginx • MongoDB • Redis • ELK Stack

**👥 Community**  
Thanks to all contributors and the cybersecurity research community

</div>

---

## 📞 Contact & Support

<div align="center">

**Project Maintainer:** [Darkwebnew](https://github.com/Darkwebnew)

**Issues:** [Report a bug or request a feature](https://github.com/Darkwebnew/CyberGuard-AI/issues)

**Discussions:** [Join the community discussion](https://github.com/Darkwebnew/CyberGuard-AI/discussions)

---

### ⭐ Star this repository if you find it useful!

**Made with ❤️ for the cybersecurity community**

</div>
