# LitePolis
Infrastructure for E-democracy  
![](https://img.shields.io/badge/status-alpha_test-orange) ![](https://img.shields.io/badge/release-developer_facing-yellow) ![PyPI - Version](https://img.shields.io/pypi/v/litepolis)

## Overview

LitePolis is an advanced, Python-based infrastructure designed for building **customizable opinion collection systems**, extending beyond the capabilities of the original [Polis](https://github.com/compdemocracy/polis). It offers a **developer-friendly** environment focused on flexibility and power.

Built with a modular, microservice-like architecture, LitePolis is **distributed by default**, leveraging the [Ray framework](https://www.ray.io/) for inherent **auto-scaling** capabilities right out of the box. This ensures your applications can handle large groups and high traffic volumes efficiently.

The core of LitePolis is a central package manager that discovers and orchestrates various components – API Routers, Middleware, and UI Packages. This modularity allows developers and data scientists to easily build, deploy, and iterate on sophisticated data-driven e-democracy tools and other opinion-gathering applications.

## Getting Started: Develop to Deploy LitePolis App in 7 Steps\!

This tutorial guides you through building and deploying a minimal LitePolis application, consisting of a simple API backend (a Router package).

**Prerequisites:**

  * Python (3.8+ recommended) and pip installed.
  * Git installed.
  * Access to a running Ray Cluster. For local development, you can start one easily:
    ```bash
    pip install ray[serve] # Install Ray with the Serve component
    ray start --head --dashboard-host 0.0.0.0 # Start a local single-node cluster
    # Access the Ray Dashboard at http://127.0.0.1:8265
    ```
    *(Refer to [Ray Cluster Setup Docs](https://docs.ray.io/en/latest/cluster/getting-started.html) for more advanced setups like multi-node or Kubernetes)*

### 1. Install the LitePolis CLI

The `litepolis-cli` is your main tool for creating, managing, and deploying LitePolis packages.

```bash
pip install litepolis
# Verify installation
litepolis --version
```

### 2. Create Your First API Router Package

API Routers handle backend logic and data requests. Let's create a simple "hello world" router.

```bash
# Use the CLI to bootstrap a new router package
litepolis create router litepolis-router-simple-api

# Navigate into the new directory
cd litepolis-router-simple-api
```

This command creates a standard Python package structure. Look inside `litepolis_router_simple_api/main.py` (or similar). It will contain boilerplate code using FastAPI. Let's make sure it has a basic endpoint:

```python
# litepolis_router_simple_api/main.py (ensure/modify it looks like this)
from fastapi import APIRouter

router = APIRouter()

@router.get("/hello")
async def read_root():
    return {"message": "Hello from my-simple-api!"}

# LitePolis package manager will discover this 'router' object
```

  * **(Optional) Explore:** Check out the [Example Router Package](https://github.com/NewJerseyStyle/LitePolis-router-example) for more complex examples, including database interactions ([Example DB Package](https://github.com/NewJerseyStyle/LitePolis-database-example)).

### 3. Prepare Your Packages for Deployment

For the LitePolis CLI to find your local packages during deployment, you often need to install them in "editable" mode.

```bash
# In the litepolis-router-simple-api directory:
pip install -e .
```

This makes your local package code importable by the LitePolis deployment process.

### 4. Deploy to Ray\!

Make sure your local Ray cluster is running (see Prerequisites). Now, use the LitePolis CLI to deploy your application based on the configuration file.

```bash
litepolis-cli deploy add-deps litepolis-router-simple-api
litepolis-cli deploy serve
```

## Next Steps:

  * Explore the [Example UI](https://github.com/NewJerseyStyle/LitePolis-ui-example) and [Example Router](https://github.com/NewJerseyStyle/LitePolis-router-example) repositories in more detail.
  * Try adding a **Middleware** package (`litepolis create middleware ...`) for things like logging or authentication.
  * Learn more about configuring **auto-scaling**, replicas, and other deployment options in your `deploy.yaml` or via CLI arguments (refer to LitePolis documentation).
  * Integrate a database using a dedicated router package (see the [Database Example](https://github.com/NewJerseyStyle/LitePolis-database-example)).

## Deployment & Maintenance Strengths

While the tutorial covers the *how*, remember the key *why*s for using LitePolis, especially for administrators:

  * **Default Auto-Scaling:** Ray Serve automatically scales API replicas based on traffic.
  * **Modular Feature Addition:** Add functionality by adding package dependencies and redeploying.
  * **Simplified Orchestration:** The `litepolis` tool manages component discovery and dependency resolution.
  * **Resilience:** Ray provides fault tolerance for running components.
  * **Cloud Native:** Runs effectively on Kubernetes and cloud platforms.