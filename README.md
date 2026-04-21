# Anonymous Submission — Reproducibility (Docker Compose)

This repository provides a containerized setup to reproduce the experimental system using Docker Compose.

Datasets are located in the `data/` directory, and configuration files are in `config/`.

## 📦 Prerequisites

* **Docker**
* **Docker Compose** (v2+, use `docker compose`)

### Install Docker

1. Download Docker Desktop from the official page: https://www.docker.com/products/docker-desktop/
2. Install Docker Desktop for your OS (macOS, Windows, or Linux).
3. Start Docker Desktop and wait until Docker is running.
4. Verify installation:

```bash
docker --version
docker compose version
```

## 🚀 Quick Start

From the root directory, run:

```bash
docker compose -f docker_compose.yml up -d
```

After startup, access the services:

| Service | URL | Default Port |
| :--- | :--- | :--- |
| **Frontend UI** | `http://localhost:5173` | `5173` |
| **Backend API** | `http://localhost:8000` | `8000` |

## 🛑 Stopping Services

```bash
docker compose -f docker_compose.yml down
```

## 📜 Viewing Logs

```bash
docker compose -f docker_compose.yml logs -f
```

## ⚙️ Configuration

Environment variables can be set via shell export, a `.env` file, or inline before execution.

| Variable | Default Value | Description |
| :--- | :--- | :--- |
| `BACKEND_IMAGE` | `backend:latest` | Backend container image |
| `CHATBOT_UI_IMAGE` | `frontend:latest`| Frontend container image |
| `BACKEND_PORT` | `8000` | Host port for backend |
| `CHATBOT_UI_PORT` | `5173` | Host port for frontend |
| `DJANGO_SETTINGS_MODULE`| `api.settings` | Backend configuration module |
| `VITE_API_URL` | `http://backend:8000`| API endpoint for frontend |

**Example (custom ports):**

```bash
BACKEND_PORT=8080 CHATBOT_UI_PORT=3000 docker compose -f docker_compose.yml up -d
```

## 🌐 API Configuration Note

> **Note:** By default, the frontend connects to `http://backend:8000`, which works internally inside the Docker network. 
> 
> If accessing from a local host browser and requests fail, explicitly map the URL:

```bash
VITE_API_URL=http://localhost:8000 docker compose -f docker_compose.yml up -d
```
*(Adjust the port in the URL if `BACKEND_PORT` was changed, e.g., to `8080`)*.

## 📁 Repository Structure

```text
.
├── data/                  # Datasets required for execution
├── config/                # System configuration files
└── docker_compose.yml     # Docker service definitions
```

## 🧪 Reproducibility Notes

* All required components are fully containerized.
* Default settings are mapped to reproduce the exact experimental setup.
* **Requirement:** Ensure all necessary datasets are populated in `data/` before executing the `up` command.

## 🔒 Anonymity Notice

This repository is strictly provided for **double-blind review**. All identifying information, author names, and institutional affiliations have been removed. They will be restored in the public release repository upon acceptance.