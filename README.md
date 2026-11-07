# Mission-Critical SRE Lab

A simulated Site Reliability Engineering environment built to demonstrate high-availability, infrastructure-as-code, and automated self-healing principles required for defense-grade software pipelines.

## Project Architecture

- **Application:** Flask-based 'Mission Data Receiver' with artificial chaos/latency injection.
- **Infrastructure:** Containerised via Docker and orchestrated using Docker Compose.
- **Observability:** Metric tracking via Prometheus; performance visualization ready for Grafana.

## Current SRE Objectives

1. [x] Deploy infrastructure-as-code baseline (Docker/Compose).
2. [ ] Inject simulated load/chaos traffic to trigger service degradation.
3. [ ] Configure Grafana dashboards to monitor latency (SLIs) and error budgets.
4. [ ] Define automated container failover/recovery rules to maintain uptime.
