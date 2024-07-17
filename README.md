# KubePing

KubePing is a web application designed to check the accessibility of external endpoints from all nodes in a Kubernetes cluster quickly and comfortably. It works by utilizing the [from-node-exporter](https://github.com/teymurgahramanov/from-node-exporter) API.

<img src="kubeping.png" alt="drawing" width="600"/>

## Prerequisites

- Kubernetes cluster
- [from-node-exporter](https://github.com/teymurgahramanov/from-node-exporter) (version >0.3.0) installed and running in the same namespace as KubePing

## Installation

### Step 1: Install `from-node-exporter`

Ensure that [from-node-exporter](https://github.com/teymurgahramanov/from-node-exporter) is installed and running in your cluster with version greater than 0.3.0.

### Step 2: Install KubePing
```bash
git clone https://github.com/teymurgahramanov/kubeping
# Set values
helm install kubeping kubeping/chart --namespace <your-namespace>
```