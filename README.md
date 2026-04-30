# LitePolis
Infrastructure for E-democracy  

![](https://img.shields.io/badge/status-beta_test-yellow) ![](https://img.shields.io/badge/release-developer_facing-yellow) ![PyPI - Version](https://img.shields.io/pypi/v/litepolis)

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
litepolis-cli deploy add-deps litepolis-router-example

# setup default config for packages in `~/.litepolis/config.conf`
litepolis-cli deploy init-config

# setup password etc.
nano ~/.litepolis/config.conf

# start serving
litepolis-cli deploy serve
# Or: start a local head node and serve in one go
litepolis-cli deploy local

# Or deploy to remote cluster
litepolis-cli deploy --cluster ray://<head-node-ip>:10001 serve
```

## For Developers
To build new package for the LitePolis ecosystem

```bash
# Create a new router package
litepolis-cli create router litepolis-router-myrouter

# Create a new database adapter
litepolis-cli create database litepolis-database-mydb

# Create a new middleware package
litepolis-cli create middleware litepolis-middleware-mymiddleware

# Create a new UI component
litepolis-cli create ui litepolis-ui-mypanel
```

Each command clones the appropriate template repo, renames everything to match your package name, and re-initializes git so you can push to your own repo.

After scaffolding:

```bash
cd litepolis-router-myrouter
git remote add origin YOUR_REPO_URL
git push -u origin main
```

### Package requirements

Each package must expose at module level:

- **`router`** — a FastAPI `APIRouter` instance
- **`prefix`** — the API path prefix string (e.g. `"v3"`)
- **`dependencies`** — list of FastAPI dependencies (can be `[]`)
- **`DEFAULT_CONFIG`** — a `dict[str, str]` of default config values (used by `init-config`)

For database, middleware, and UI packages, the scaffolded template will show the expected interface.

> 📚 See wiki:
> * [LitePolis Package Lifecycle](https://github.com/NewJerseyStyle/LitePolis/wiki/LitePolis-Package-Lifecycle)
> * [Tutorial: Creating New LitePolis Packages with litepolis‐cli](https://github.com/NewJerseyStyle/LitePolis/wiki/Tutorial:-Creating-New-LitePolis-Packages-with-litepolis%E2%80%90cli)

---

## CLI Reference

```
litepolis-cli deploy [OPTIONS] COMMAND

Options:
  --packages-file PATH   Path to packages.txt  [default: ~/.litepolis/packages.txt]
  --cluster TEXT         Ray cluster address   [default: auto]

Commands:
  add-deps      Add or update a package in packages.txt and install it
  remove-deps   Remove a package from packages.txt
  list-deps     Compare packages.txt with currently installed versions
  sync-deps     Install all packages in packages.txt to their pinned versions
  init-config   Generate ~/.litepolis/config.conf from installed packages
  serve         Start the LitePolis API server
  local         Start a local Ray head node and serve

litepolis-cli create COMMAND

Commands:
  router        Scaffold a new router package
  database      Scaffold a new database package
  middleware    Scaffold a new middleware package
  ui            Scaffold a new UI package
```

## Next Steps:

* Deploy to Google cloud with autoscale [WIP#todo]
