# Docker Sandbox + Cognee Brain + Strands Agents Harness

Build a company brain for your Agent Harness using Cognee for memory, Strands Agents for the Harness, and Docker Sandboxes for isolated execution.

- [agent.py](agent.py) — Strands agent: `remember`/`recall` (Cognee) + `market_data`/`price_alert` (yfinance)
- [flow.md](flow.md) — architecture

## Prerequisites

- [Docker Sandboxes](https://docs.docker.com/ai/sandboxes/install/) (`sbx`)
- A Cognee Cloud tenant (URL + API key) and an Anthropic API key

## Installation & Setup

Install [Docker Sandboxes](https://docs.docker.com/ai/sandboxes/install/) and run all commands from this project directory.

```bash
brew install docker/tap/sbx
sbx version
```

Copy the env template and fill in your Cognee tenant (URL, API key, dataset) and Anthropic API key.

```bash
cp -n .env.example .env
```

## Set the network policy and start Sandbox

Set the global network policy (`Balanced`), then allow your Cognee tenant and Yahoo Finance.

```bash
sbx policy init balanced
sbx policy allow network '*.aws.cognee.ai,query1.finance.yahoo.com,query2.finance.yahoo.com,fc.yahoo.com'
```

Start the Claude Code sandbox and `/login`, then install dependencies with `uv`.

```bash
sbx run --name cognee-agent claude "$PWD"
sbx exec -w "$PWD" cognee-agent bash -lc 'uv venv .venv; uv pip install --python .venv/bin/python -r requirements.txt'
```

## Run the Agent Harness

1. Pull a live market snapshot to confirm the finance tool works.

```bash
sbx exec -w "$PWD" cognee-agent .venv/bin/python agent.py ask 'Use market_data for AAPL and report its last price and 52-week high.'
```

2. Save an investment thesis to Cognee Brain memory (to remember)

```bash
sbx exec -w "$PWD" cognee-agent .venv/bin/python agent.py ask 'Remember my confirmed AAPL watchlist: buy target $320, trim target $345, thesis is the iPhone upgrade cycle is largely priced in above $345.'
```

3. A fresh process recalls those targets and checks them against a live price — memory + finance together.

```bash
sbx exec -w "$PWD" cognee-agent .venv/bin/python agent.py ask 'Recall my AAPL watchlist targets, then use price_alert to check AAPL against them and give me a buy/trim/hold call.'
```

4. Read from Memory (recall)

> Note: 

- Read the stored memory directly, no model. `recall` is a plain memory lookup (no LLM, no tokens); 
- `ask` runs the agent, which reasons and calls tools like `recall` and `price_alert` on its own.

```bash
sbx exec -w "$PWD" cognee-agent .venv/bin/python agent.py recall 'AAPL watchlist buy and trim targets'
```

5. Optional: Use Claude Code to ask the question

Now just talk to Claude Code in the sandbox — it reads/writes this memory on its own, on your subscription (no API key).

```text
Am I near my AAPL watchlist targets?
```
