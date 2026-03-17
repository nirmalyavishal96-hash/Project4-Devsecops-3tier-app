# DevSecOps 3-Tier Application Pipeline 🚀

A production-style **DevSecOps project** implementing a complete CI/CD pipeline for a containerized **3-tier web application** using modern DevOps and security tools.

This project demonstrates how developers can securely build, scan, and deploy applications using **Docker, Jenkins, Trivy, Kubernetes, Helm, and ArgoCD**.

---

# 📌 Project Overview

This repository contains a **3-tier web application** consisting of:

* **Frontend** – React static UI
* **Backend** – Flask REST API
* **Database** – PostgreSQL

The application is containerized and integrated into a **DevSecOps pipeline** that automates:

* Build
* Security scanning
* Image publishing
* Deployment

---

# 🏗 Architecture

```
Developer
   │
   ▼
GitHub Repository
   │
   ▼
Jenkins CI Pipeline
   │
   ├── Build Docker Image
   ├── Trivy Security Scan
   └── Push Image to DockerHub
   │
   ▼
ArgoCD GitOps
   │
   ▼
Kubernetes Cluster (Helm Deployment)
   │
   ▼
3-Tier Application
```

---

# 🧱 Application Architecture

```
Client (Browser)
        │
        ▼
Frontend (React)
        │
        ▼
Backend API (Flask)
        │
        ▼
PostgreSQL Database
```

---

# 🛠 Tech Stack

| Category           | Tools Used             |
| ------------------ | ---------------------- |
| Application        | Flask, React           |
| Containerization   | Docker, Docker Compose |
| Security Scanning  | Trivy                  |
| CI/CD              | Jenkins                |
| Container Registry | DockerHub              |
| Infrastructure     | Kubernetes             |
| Package Manager    | Helm                   |
| GitOps Deployment  | ArgoCD                 |
| IaC                | Terraform              |
| Monitoring         | Prometheus + Grafana   |

---

# 📂 Project Structure

```
devsecops-3tier-app
│
├── app/                # Flask backend
├── static/             # React frontend
├── docker/             # Docker configuration
├── jenkins/            # Jenkins pipeline
├── helm/               # Helm charts
├── terraform/          # Infrastructure as Code
├── monitoring/         # Prometheus & Grafana
│
├── docker-compose.yml
├── requirements.txt
├── manage.py
└── README.md
```

---

# ⚙️ Local Development Setup

### Clone Repository

```
git clone https://github.com/<your-username>/Project4-Devsecops-3tier-app.git
cd Project4-Devsecops-3tier-app
```

---

### Run Application with Docker

```
docker compose up --build
```

Application will start at:

```
http://localhost:5000
```

---

# 🔐 Security Scanning with Trivy

The Docker image is scanned for vulnerabilities before deployment.

Run manually:

```
trivy image <dockerhub-username>/devsecops-flask-app:1.0
```

Example output:

```
CRITICAL: 0
HIGH: 0
MEDIUM: 1
LOW: 2
```

The pipeline blocks deployments if **HIGH or CRITICAL vulnerabilities** are detected.

---

# 🔄 CI/CD Pipeline (Jenkins)

Pipeline Stages:

```
1. Pull source code from GitHub
2. Build Docker image
3. Scan image using Trivy
4. Push image to DockerHub
5. Trigger deployment via GitOps
```

---

# ☸ Kubernetes Deployment

Application is deployed using **Helm charts** into a Kubernetes cluster.

Services exposed using:

```
Kubernetes Ingress Controller
```

---

# 📊 Monitoring

Monitoring stack includes:

* **Prometheus** – metrics collection
* **Grafana** – visualization dashboards

Logs can be aggregated using tools such as:

```
Loki + Grafana
```

---

# 🚀 Future Improvements

* Add automated **OWASP dependency scanning**
* Integrate **SonarQube code quality checks**
* Implement **automated rollback in ArgoCD**
* Add **Slack alerts for pipeline failures**

---

# 👨‍💻 Author

**Nirmalya Das**

DevOps / Cloud Engineer
Focus Areas:

* DevSecOps
* Kubernetes
* CI/CD Automation
* Cloud Infrastructure

---

# ⭐ If you found this project helpful

Give it a **star on GitHub** to support the project!
