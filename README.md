# Compass1 — Docker Compose

This stack runs the **Wander** backend (Django) and **chatbot UI** (Vite) from published images.

## Prerequisites

- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/install/) v2+ (`docker compose`)

## Quick start

From this directory:

```bash
docker compose -f docker_compose.yml up -d
```

Then open:

| Service    | URL                     | Default host port |
| ---------- | ----------------------- | ----------------- |
| Chatbot UI | http://localhost:5173   | `5173`            |
| Backend    | http://localhost:8000   | `8000`            |

Stop and remove containers:

```bash
docker compose -f docker_compose.yml down
```

View logs:

```bash
docker compose -f docker_compose.yml logs -f
```

## Environment variables

Optional overrides (shell, `.env` in the same directory as the compose file, or `export` before `up`):

| Variable              | Default                         | Purpose                          |
| --------------------- | ------------------------------- | -------------------------------- |
| `BACKEND_IMAGE`       | `oholala/wander-backend:latest` | Backend container image          |
| `CHATBOT_UI_IMAGE`    | `oholala/wander-frontend:latest`| Frontend container image         |
| `BACKEND_PORT`        | `8000`                          | Host port mapped to backend      |
| `CHATBOT_UI_PORT`     | `5173`                          | Host port mapped to chatbot UI   |
| `DJANGO_SETTINGS_MODULE` | `api.settings`              | Django settings module           |
| `VITE_API_URL`        | `http://backend:8000`           | API base URL seen by the UI app  |

Example with custom ports:

```bash
BACKEND_PORT=8080 CHATBOT_UI_PORT=3000 docker compose -f docker_compose.yml up -d
```

### API URL from the browser

The default `VITE_API_URL` uses the Docker service name `backend`, which resolves **inside** the compose network. If the UI makes requests **from your browser** and those requests fail, point the UI at the host instead, for example:

```bash
VITE_API_URL=http://localhost:8000 docker compose -f docker_compose.yml up -d
```

(Use the same port you mapped for the backend, e.g. `8080` if you set `BACKEND_PORT=8080`.)

Whether you need this depends on how the frontend image is built (e.g. server-side proxy vs direct browser calls).

## File reference

- `docker_compose.yml` — defines `backend` and `chatbot-ui` services with `restart: unless-stopped`.
