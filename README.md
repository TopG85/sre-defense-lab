# Mission-Critical SRE Lab

A simulated Site Reliability Engineering environment built to demonstrate high-availability, infrastructure-as-code, and automated self-healing principles required for defense-grade software pipelines.

## Project Architecture

- **Application:** Flask-based 'Mission Data Receiver' with artificial chaos/latency injection.
- **Infrastructure:** Containerised via Docker and orchestrated using Docker Compose.
- **Observability:** Metric tracking via Prometheus; performance visualization ready for Grafana.

## Technical Engineering Fixes

- **Infrastructure Traffic Routing:** Solved a localized host port conflict by re-routing application containers from Port 5000 to Port 5001.
- **Data Pipeline Activation:** Created and configured a custom `prometheus.yml` file utilizing internal Docker network gateways to bridge telemetry streams.
- **Timezone Sync Calibration:** Configured Grafana dashboard viewports to track browser time-clocks to prevent monitoring visibility lag.

## Current SRE Objectives

1. [x] Deploy infrastructure-as-code baseline (Docker/Compose).
2. [x] Configure Grafana dashboards to monitor latency (SLIs) and error budgets.
3. [x] Inject simulated load/chaos traffic to trigger service degradation (`load_generator.py`).
4. [x] Define automated container failover/recovery rules and scale microservice capacity dynamically.

## I Built

"I built a containerized Python data pipeline using Docker and automated its infrastructure orchestration using Docker Compose. To mirror a defense environment, I set up a Prometheus engine scraping internal network host gateways and wired it into a live Grafana dashboard to track service level indicators in real-time. Finally, I built a multi-threaded load-testing script to simulate a traffic attack, diagnosed port allocations under fire, and dynamically scaled the app instances to absorb the stress load."
