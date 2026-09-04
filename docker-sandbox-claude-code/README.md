# Docker, Cognee, and Claude Code: Memory Sandbox Setup

## Prerequisites

- Docker Desktop running
- A Cognee Cloud tenant (URL + API key)

## 1. Configure credentials

`.env` in this directory:

```
COGNEE_BASE_URL=https://your-tenant.aws.cognee.ai
COGNEE_API_KEY=your-api-key
```

## 2. Build the sandbox image

```bash
docker build -f Dockerfile.sandbox -t cognee-sandbox .
```

A stateless `python:3.12-slim` container with just the `cognee` package — no local LLM, no local graph DB.

## 3. Store and recall memory

Each `docker run` is a fresh, disposable container with no shared state
between runs — only Cognee Cloud connects them.

```bash
# store facts/data using remember() function
docker run --rm --env-file .env cognee-sandbox remember

# recall, in a separate container, with your own question
docker run --rm --env-file .env cognee-sandbox recall "your question here"

# both in one process
docker run --rm --env-file .env cognee-sandbox both
```
<img width="1416" height="770" alt="Screenshot 2026-09-04 at 20 22 48" src="https://github.com/user-attachments/assets/5bf5e319-875e-457b-89ef-6461e423751f" />

`remember()`/`recall()` route to Cognee Cloud over HTTPS. 

## 4. Connect Claude Code to the same memory

Install the plugin:

```bash
claude plugin marketplace add topoteretes/cognee-integrations
claude plugin install cognee-memory@cognee
```

Point it at the same tenant:

```bash
mkdir -p ~/.cognee
cat >> ~/.cognee/.env <<'EOF'
COGNEE_BASE_URL="https://your-tenant.aws.cognee.ai"
COGNEE_API_KEY="your-api-key"
EOF
```
<img width="1408" height="213" alt="Screenshot 2026-09-04 at 20 19 35" src="https://github.com/user-attachments/assets/93513515-1fc1-43fb-b2dc-1d77dc125623" />

Launch `claude` — you should see "Cognee Memory Connected". The plugin reads/writes the same `agent_sessions` dataset (via session hooks, no manual API calls), so anything the sandbox stored is recallable inside Claude Code, and anything Claude Code learns syncs back on `/exit`.

<img width="798" height="599" alt="Screenshot 2026-09-04 at 20 20 17" src="https://github.com/user-attachments/assets/bff8aa0c-78c2-4afc-a476-3c930467047f" />
