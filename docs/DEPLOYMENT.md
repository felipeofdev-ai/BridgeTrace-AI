# Deployment Guide

## Docker Deployment

### Build Image
```bash
docker build -t bridgetrace-ai:2.0.0 .
```

### Run Container
```bash
docker run -d \
  -p 8000:8000 \
  -e DATABASE_URL=postgresql://user:pass@host:5432/db \
  -e REDIS_URL=redis://host:6379/0 \
  --name bridgetrace-api \
  bridgetrace-ai:2.0.0
```

## Docker Compose

```bash
# Start all services
docker-compose up -d

# View logs
docker-compose logs -f api

# Stop services
docker-compose down
```

## Kubernetes

### Deploy
```bash
kubectl apply -f k8s/namespace.yaml
kubectl apply -f k8s/configmap.yaml
kubectl apply -f k8s/secrets.yaml
kubectl apply -f k8s/deployment.yaml
kubectl apply -f k8s/service.yaml
kubectl apply -f k8s/ingress.yaml
```

### Scale
```bash
kubectl scale deployment bridgetrace-api --replicas=3
```

## Cloud Platforms

### AWS ECS
1. Build and push image to ECR
2. Create task definition
3. Create ECS service
4. Configure load balancer

### Google Cloud Run
```bash
gcloud run deploy bridgetrace-ai \
  --image gcr.io/PROJECT/bridgetrace-ai:2.0.0 \
  --platform managed \
  --region us-central1 \
  --allow-unauthenticated
```

### Azure Container Instances
```bash
az container create \
  --resource-group bridgetrace \
  --name bridgetrace-api \
  --image bridgetrace-ai:2.0.0 \
  --dns-name-label bridgetrace \
  --ports 8000
```

## Environment Variables

Required:
- `DATABASE_URL`: PostgreSQL connection string
- `SECRET_KEY`: JWT secret key
- `REDIS_URL`: Redis connection string

Optional:
- `LOG_LEVEL`: Logging level (default: INFO)
- `OPENAI_API_KEY`: OpenAI API key for AI features
- `MAX_TRACE_HOPS`: Maximum trace hops (default: 10)

## Health Checks

Configure health checks:
- Liveness: `/api/v2/health/live`
- Readiness: `/api/v2/health/ready`

## Monitoring

- Metrics: `/metrics` (Prometheus format)
- Logs: stdout/stderr (JSON format)
- Tracing: OpenTelemetry compatible

## Security Checklist

- [ ] Change default SECRET_KEY
- [ ] Enable HTTPS/TLS
- [ ] Configure firewall rules
- [ ] Set up authentication
- [ ] Enable audit logging
- [ ] Regular security updates
- [ ] Backup strategy
