# Anonymous Submission — Reproducibility (Docker Compose)

This repository provides a containerized setup to reproduce the experimental system using Docker Compose.

Datasets are expected in `sc2026/datasets/` (mounted to `/app/data` in the backend container), and configuration files are in `config/`.

## 📦 Prerequisites

* **Docker**
* **Docker Compose** (v2+, use `docker compose`)

### Install Docker

1. Install Docker:
   - **macOS/Windows:** Install Docker Desktop: https://www.docker.com/products/docker-desktop/
   - **Linux:** Install Docker Engine: https://docs.docker.com/engine/install/
2. Start Docker before running any `docker` or `docker compose` command:
   - **macOS/Windows:** Open Docker Desktop and wait until it shows Docker is running.
   - **Linux:** Make sure the Docker daemon is running (for example: `sudo systemctl start docker`).
3. (Linux) Optional but recommended: enable Docker to start on boot: `sudo systemctl enable docker`.
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
| `BACKEND_IMAGE` | `oholala/compass-backend:latest` | Backend container image |
| `CHATBOT_UI_IMAGE` | `oholala/compass-frontend:latest`| Frontend container image |
| `BACKEND_PORT` | `8000` | Host port for backend |
| `CHATBOT_UI_PORT` | `5173` | Host port for frontend |
| `DJANGO_SETTINGS_MODULE`| `api.settings` | Backend configuration module |
| `VITE_API_URL` | `http://127.0.0.1:8000`| API endpoint for frontend |

**Example (custom ports):**

```bash
BACKEND_PORT=8080 CHATBOT_UI_PORT=3000 docker compose -f docker_compose.yml up -d
```

## 🌐 API Configuration Note

> **Note:** By default, the frontend connects to `http://127.0.0.1:8000`.
> 
> If accessing from a localhost browser and requests fail, explicitly map the URL:

```bash
VITE_API_URL=http://localhost:8000 docker compose -f docker_compose.yml up -d
```
*(Adjust the port in the URL if `BACKEND_PORT` was changed, e.g., to `8080`)*.

## 📁 Repository Structure

```text
.
├── sc2026/
│   ├── datasets/          # Datasets mounted to /app/data in backend
│   └── jsons/             # JSON inputs/outputs used by experiments
├── docker_compose.yml     # Docker service definitions
└── README.md              # Setup and usage instructions
```

## 🧪 Reproducibility Notes

* All required components are fully containerized.
* Default settings are mapped to reproduce the exact experimental setup.
* **Requirement:** Ensure all necessary datasets are populated in `sc2026/datasets/` before executing the `up` command.

## 🔒 Anonymity Notice

This repository is strictly provided for **double-blind review**. All identifying information, author names, and institutional affiliations have been removed. They will be restored in the public release repository upon acceptance.