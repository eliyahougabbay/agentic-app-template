# 🧠 Agent Template

A minimal, production-ready template for building **agentic applications** using [Pydantic AI](https://github.com/pydantic/pydantic-ai), with clean async architecture and full observability.

This template runs on:

- **FastAPI** – for async APIs and agent serving
- **Pydantic AI** – to structure agents, tools, and usage limits
- **PostgreSQL** – to persist conversations and data
- **Jaeger** – for distributed tracing (via OpenTelemetry)
- **Docker Compose** – to run everything locally


## ⚙️ Stack Overview

| Component   | Purpose                                                       |
|-------------|---------------------------------------------------------------|
| FastAPI     | Exposes the `/run-agent` and `/webhook` endpoints             |
| Pydantic AI | Agent framework with usage tracking                           |
| PostgreSQL  | Persists conversations and other data                         |
| Jaeger      | Debug and trace agents via distributed tracing                |
| Alembic     | Manages database migrations                                   |


## 🧩 Features

- Agent-first architecture powered by [Pydantic AI](https://github.com/pydantic/pydantic-ai):
  - Structured agent workflows with type-safe inputs/outputs
  - Built-in tool registration using `@agent.tool`
  - Request-level usage limits (e.g., max 5 LLM calls per run)
- Fully async, built on FastAPI
- Webhook support for delivering results externally
- Built-in tracing via Jaeger and OpenTelemetry


## 🚀 Getting Started

### 1. Create the `.env` file

At the root of the project, create a `.env` file and fill in your Azure OpenAI credentials:

```dotenv
AZURE_API_KEY=
AZURE_ENDPOINT=
AZURE_API_VERSION=
AZURE_MODEL_ID=
```

### 2. Start the application

Run the following command to build and start the application:

```bash
docker-compose up --build
```

This will start the following services:
- web (FastAPI server)
- postgres
- pgAdmin (PostgreSQL GUI)
- jaeger (tracing UI)

### 3. Access the Services

| Service      | URL                            |
|--------------|---------------------------------|
| API docs     | [http://localhost:8000/docs](http://localhost:8000/docs)     |
| pgAdmin      | [http://localhost:5050](http://localhost:5050)          |
| Jaeger       | [http://localhost:16686](http://localhost:16686)         |

> 🧠 pgAdmin login: `admin@example.com` / `admin`

### 4. Develop Inside the Container

To run shell commands inside the `web` container:

```bash
docker-compose exec web /bin/bash
```

### 5. Using the Template Effectively

- **Database migrations** with Alembic:
  ```bash
  alembic revision --autogenerate -m "your message"
  alembic upgrade head
  ```
- **Custom agent tools** can be added in `src/agents/` using the `@agent.tool` decorator.
- **Tracing** is enabled automatically via `logfire` and exported to Jaeger.
  You can view traces at [http://localhost:16686](http://localhost:16686).
- **Code linting & formatting:** I recommend using [Ruff](https://docs.astral.sh/ruff/) for fast linting and formatting during development.

This gives you an interactive shell inside your running app.  
Useful for debugging, running migrations, or launching ad-hoc scripts.

> ✅ The app uses `watchdog` to auto-reload on code changes inside the container.


## 🧪 Example API Usage

This template is currently designed as an API-first setup — you interact with the agent by sending HTTP requests to the FastAPI backend.

```bash
curl -X POST http://localhost:8000/run-agent \
  -H "Content-Type: application/json" \
  -d '{
    "query": "How do I start a company in France?",
    "callback_url": "http://localhost:8000/webhook"
  }'
```


## 📂 Project Structure

```text
.
├── Dockerfile
├── docker-compose.yaml
├── entrypoint.sh
├── pyproject.toml
├── requirements.txt
├── alembic/
├── src/
│   ├── main.py
│   ├── config.py
│   ├── agents/
│   ├── api/
│   ├── db/
│   ├── models/
│   ├── schemas/
│   └── services/
```

## 🔮 What's Next?

This template is designed to grow with you. In the future, you can easily add:

- A task queue with [Dramatiq](https://dramatiq.io/) for background workflows
- Redis (for caching or as a broker)
- Multi-agent routing and tool chaining
- JWT authentication or session management
- Admin dashboard or logs viewer
