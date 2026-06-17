import time
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Dict

app = FastAPI(
    title="Cloud-Native Microservice Monitor",
    description="Production-ready API for tracking cluster infrastructure health.",
    version="1.0.0"
)

# InMemory database simulating cloud resource registry
metrics_db: Dict[str, dict] = {}

class ServiceMetric(BaseModel):
    service_name: str
    status: str  # UP, DOWN, DEGRADED
    cpu_usage_percent: float
    memory_usage_mb: float

@app.get("/", tags=["Root"])
def read_root():
    """
    Root endpoint verifying global API availability.
    """
    return {
        "status": "healthy",
        "timestamp": time.time(),
        "environment": "production-azure"
    }

@app.post("/api/v1/metrics", response_model=Dict[str, str], tags=["Telemetry"])
def register_metrics(metric: ServiceMetric):
    """
    Receives live telemetry metrics pushed from microservice agents (like the Go Agent).
    """
    if metric.cpu_usage_percent < 0 or metric.cpu_usage_percent > 100:
        raise HTTPException(status_code=400, detail="Invalid CPU utilization range.")
    
    metrics_db[metric.service_name] = {
        "status": metric.status,
        "cpu": f"{metric.cpu_usage_percent}%",
        "memory": f"{metric.memory_usage_mb} MB",
        "last_updated": time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime())
    }
    return {"message": f"Metrics successfully logged for {metric.service_name}"}

@app.get("/api/v1/dashboard", tags=["Monitoring"])
def get_dashboard():
    """
    Returns a unified executive health overview of all cluster services.
    """
    if not metrics_db:
        return {"cluster_status": "UNKNOWN", "active_services": 0, "nodes": {}}
    
    # Check if any critical service is down
    global_status = "HEALTHY"
    for svc, data in metrics_db.items():
        if data["status"] == "DOWN":
            global_status = "CRITICAL"
            break

    return {
        "cluster_status": global_status,
        "active_services": len(metrics_db),
        "nodes": metrics_db
    }