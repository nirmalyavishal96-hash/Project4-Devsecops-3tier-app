# 🚀 DevSecOps 3-Tier Application on Kubernetes

![Kubernetes](https://img.shields.io/badge/Kubernetes-Deployment-blue)
![Jenkins](https://img.shields.io/badge/Jenkins-CI%2FCD-red)
![ArgoCD](https://img.shields.io/badge/ArgoCD-GitOps-orange)
![Prometheus](https://img.shields.io/badge/Monitoring-Prometheus-yellow)
![Grafana](https://img.shields.io/badge/Visualization-Grafana-orange)
![Trivy](https://img.shields.io/badge/Security-Trivy-green)

---

## 📌 Project Overview

This project demonstrates a **complete DevSecOps pipeline** by deploying a **3-tier application** on Kubernetes using industry-standard tools.

---

## 🏗️ Architecture

```
Frontend (Nginx)
        ↓
Backend (Flask API)
        ↓
Database (PostgreSQL)
```

---

## ⚙️ Tech Stack

| Category         | Tools                 |
| ---------------- | --------------------- |
| Frontend         | Nginx                 |
| Backend          | Flask                 |
| Database         | PostgreSQL            |
| Containerization | Docker                |
| Orchestration    | Kubernetes (Minikube) |
| CI/CD            | Jenkins               |
| GitOps           | ArgoCD                |
| Monitoring       | Prometheus            |
| Visualization    | Grafana               |
| Security         | Trivy                 |
| Alerting         | Alertmanager          |

---

## 🚀 Features

* CI/CD pipeline using Jenkins
* GitOps deployment using ArgoCD
* Container scanning using Trivy
* Monitoring with Prometheus & Grafana
* Alerting via Alertmanager
* Reverse proxy using Nginx

---

## 🛠️ Setup Instructions

### Start Minikube

```
minikube start
```

### Deploy PostgreSQL

```
kubectl apply -f k8s/postgres-deployment.yaml
kubectl apply -f k8s/postgres-service.yaml
```

### Deploy Backend

```
kubectl apply -f k8s/deployment.yaml
kubectl apply -f k8s/service.yaml
```

### Deploy Frontend

```
kubectl apply -f k8s/frontend-deployment.yaml
kubectl apply -f k8s/frontend-service.yaml
```

---

## 📸 Screenshots

* Jenkins Pipeline
* ArgoCD Sync
* Grafana Dashboard
* Prometheus Targets
* Alert Email
* Application UI

---

# 🐞 Troubleshooting & Debugging Journey (REAL ISSUES)

This project includes several real-world issues encountered and fixed:

---

### ❌ 1. Git Stuck on `git add .`

**Issue:** Git was hanging due to large/unnecessary files (node_modules, venv)
**Fix:** Cleaned repo and used `.gitignore`

---

### ❌ 2. CrashLoopBackOff in Kubernetes

**Issue:** Container was crashing continuously
**Root Cause:** Incorrect Docker CMD (`python app.py` missing)
**Fix:** Switched to:

```
flask run --host=0.0.0.0
```

---

### ❌ 3. Flask Not Accessible from Kubernetes

**Issue:** Service running but no response
**Fix:** Bound Flask to:

```
0.0.0.0 instead of 127.0.0.1
```

---

### ❌ 4. `/api/health` Returning 404

**Issue:** Endpoint not available
**Fix:** Added health route explicitly in Flask app

---

### ❌ 5. Minikube Browser Not Opening

**Issue:** `xdg-open` permission error
**Fix:** Used manual URL from:

```
minikube service <service> --url
```

---

### ❌ 6. Frontend Unable to Reach Backend

**Issue:** Using `localhost` and `flask-service` incorrectly
**Fix:** Implemented **Nginx reverse proxy**

---

### ❌ 7. Nginx Proxy Path Issue (Critical Bug)

**Issue:**

```
/api/health → /health (wrong routing)
```

**Fix:**

```
proxy_pass http://flask-service:5000/api/
```

---

### ❌ 8. Docker Image Not Updating

**Issue:** Kubernetes using cached image
**Fix:**

```
imagePullPolicy: Always
```

---

### ❌ 9. Wrong Docker Build Context

**Issue:** Used `docker build ..`
**Fix:** Built from correct folder:

```
docker build .
```

---

## 🔐 Security

* Trivy used for vulnerability scanning
* Secure CI pipeline implemented

---

## 📊 Monitoring

* Prometheus for metrics
* Grafana dashboards
* Alertmanager for email alerts

---

## 🎯 Outcome

This project demonstrates:

* Real-world DevSecOps pipeline
* Kubernetes production deployment
* Debugging real production issues
* Monitoring + security integration

---

## 👨‍💻 Author

**Nirmalya Das**
