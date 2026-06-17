
# cloud-native-observability-core 🚀

This is a production-ready microservices project to show how to connect scalable backend services with modern DevOps tools. I built a distributed setup using **Go (Golang)** for a high-concurrency agent and **Python (FastAPI)** for a central data hub, all containerized with **Docker**, automated via **GitHub Actions**, and configured for **Azure** using **Terraform**.

---

## How It Works (Architecture)

The system runs two main microservices:

1.  **Go Agent (`/go-backend`)**: Built with **Gin**. It acts as a lightweight telemetry agent that tracks runtime metrics, uptime, and active GoRoutines. It is optimized to run with almost zero overhead.
2.  **Python Central Core (`/`)**: Built with **FastAPI**. It aggregates data from the system, validates payloads using **Pydantic**, and provides clean REST endpoints along with self-generating Swagger documentation.

The infrastructure side handles the automation:
*   **Docker**: Uses multi-stage builds to keep production images tiny (based on Alpine Linux).
*   **GitHub Actions**: A CI pipeline that runs tests and validates Docker builds on every push/PR.
*   **Terraform**: Manages Azure cloud infrastructure (Resource Groups, App Service Plans, and Web Apps) as code.

---

## Features

*   **Multi-Language Backend**: Uses Python for easy data handling and Go for high-speed concurrent processing.
*   **Infrastructure as Code**: No manual configuration in the Azure console. Everything is defined in `.tf` files.
*   **Auto-Docs**: FastAPI automatically serves the OpenAPI schema at `/docs` for easy testing.
*   **Lightweight Images**: Pruned compiler dependencies out of the final Go image to minimize the cloud footprint.

---

---
---

## Local Setup

### Prerequisites
* Docker Desktop
* Python 3.10+ / Go 1.26+

### 1. Run the Python Backend (Port 8000)
Run these commands from the root directory of the project:

```bash
docker build -t cloud-native-api .
docker run -d -p 8000:8000 cloud-native-api 
```

* Check the live API docs here: [Local Swagger UI Documentation](http://localhost:8000/docs)

### 2. Run the Go Agent (Port 8080)
Open a new terminal and navigate to the Go service folder:

```bash
cd go-backend
docker build -t cloud-native-go-api .
docker run -d -p 8080:8080 cloud-native-go-api
```


* Check the live telemetry snapshot at: [Local Swagger UI Documentation](http://localhost:8080/api/v1/agent/snapshot)


## Cloud Deployment (Azure)
To initialize Terraform, check the infrastructure graphs, and preview the resources that will be created on Azure:

```bash
cd terraform
terraform init
terraform plan
```


## About Me
---

## About Me
---

## About Me
I hold two Master's degrees—one in **Statistics and Applications** and another in **Data Science**. While my academic foundation is deeply rooted in data, my true passion lies in cloud computing and infrastructure architecture. Because of this drive, I have spent immense hands-on effort mastering cloud tools, which allows me to confidently step into the world as a **Cloud and Backend Engineer**. 

I designed this pipeline to solve real-world problems with microservices, CI/CD, and Infrastructure as Code. My ultimate goal is to deploy these optimized setups in companies facing server bottlenecks, high-concurrency traffic, or infrastructure scaling challenges. I want to help teams stabilize their deployments, reduce cloud overhead, and achieve high system observability.

I have full work authorization, am open to relocation, and am ready for new full-time challenges!
