# LitePolis
Infrastructure for E-democracy  
![](https://img.shields.io/badge/status-alpha_test-orange) ![](https://img.shields.io/badge/release-developer_facing-yellow) ![PyPI - Version](https://img.shields.io/pypi/v/litepolis)

## Overview

LitePolis is an advanced, Python-based infrastructure designed for building **customizable opinion collection systems**, extending beyond the capabilities of the original [Polis](https://github.com/compdemocracy/polis). It offers a **developer-friendly** environment focused on flexibility and power.

Built with a modular, microservice-like architecture, LitePolis is **distributed by default**, leveraging the [Ray framework](https://www.ray.io/) for inherent **auto-scaling** capabilities right out of the box. This ensures your applications can handle large groups and high traffic volumes efficiently.

The core of LitePolis is a central package manager that discovers and orchestrates various components – API Routers, Middleware, and UI Packages. This modularity allows developers and data scientists to easily build, deploy, and iterate on sophisticated data-driven e-democracy tools and other opinion-gathering applications.

[![Video about LitePolis](image_with_play_button(1).png)](https://www.canva.com/design/DAGkKYnWMIE/acGGYFVWpYpFA-t65YcyWw/watch?embed)

## Quick start
### 1. Install the LitePolis CLI

The `litepolis-cli` is your main tool for creating, managing, and deploying LitePolis packages.
  * Needs Python (3.12 recommended) and pip installed.

```bash
pip install litepolis
```

### 2. Explore Packages for Deployment

![Awesome-LitePolis scans GitHub everyday for available LitePolis packges (including work in progress repositories)](https://newjerseystyle.github.io/Awesome-LitePolis/)

### 3. Deploy
Add features you want in LitePolis

```bash
litepolis-cli deploy list-deps

# remove packages if you don't need default packages that provides Polis functionality
litepolis-cli deploy remove-deps litepolis-router-default

# add packages that you need
litepolis-cli deploy add-deps litepolis-router-simple-api

litepolis-cli deploy init-config

# setup password etc.
nano ~/.litepolis/config.conf

# start serving
litepolis-cli deploy serve
```

## Next Steps:

* Use StarRocks as database [WIP#todo]
* Deploy to Google cloud with autoscale [WIP#todo]