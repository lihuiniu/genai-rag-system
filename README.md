# GenAI RAG Text-Based System
This project implements an end-to-end, enterprise-grade GenAI RAG text system with hybrid search, access control, and observability:
- FastAPI + LangChain + LangGraph
- Milvus 2.6 with hybrid search: Vector Dense Search + Keywords search
- Redis 8.0 VectorSets for memory cache
- Git and Kafka-based document ingestion
- ACL enforcement before query
- Observability via OpenTelemetry + Prometheus
- Docker & Helm deployment ready

## Architecture Diagram
See `diagrams/architecture.md`


### Features

- ✅ Milvus 2.6 + Redis 8.0 VectorSet Hybrid Search
- ✅ FastAPI with ACL enforcement
- ✅ Kafka + Git Ingestion Pipeline
- ✅ Online & Offline Evaluation
- ✅ Prometheus + Grafana for Observability
- ✅ Helm chart for scalable deployment

### Run Locally

```bash
docker-compose up --build
```

### Run Evaluation

```bash
python eval/online_eval.py
```

### Deploy to K8s

```bash
helm install genai-rag ./helm
```bash

# Or upgrade if already installed
```bash
helm upgrade genai-rag ./helm
```bash

# Or Check Status
```bash
kubectl get pods
kubectl get svc
kubectl get hpa
```bash


# Verify Access
Port-forward FastAPI if no Ingress is used:
```bash
kubectl port-forward svc/genai-rag 8000:8000
```bash

Then access:

API Docs: http://localhost:8000/docs

Health Check: http://localhost:8000/health

# Uninstall
```bash
helm uninstall genai-rag
```bash