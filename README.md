# LitePolis
Infrastructure for E-democracy  
![](https://img.shields.io/badge/status-alpha_test-orange) ![](https://img.shields.io/badge/release-developer_facing-yellow) ![PyPI - Version](https://img.shields.io/pypi/v/litepolis)

## Overview

LitePolis is an advanced, Python-based infrastructure designed for building **customizable opinion collection systems**, extending beyond the capabilities of the original [Polis](https://github.com/compdemocracy/polis). It offers a **developer-friendly** environment focused on flexibility and power.

Built with a modular, microservice-like architecture, LitePolis is **distributed by default**, leveraging the [Ray framework](https://www.ray.io/) for inherent **auto-scaling** capabilities right out of the box. This ensures your applications can handle large groups and high traffic volumes efficiently.

The core of LitePolis is a central package manager that discovers and orchestrates various components – API Routers, Middleware, and UI Packages. This modularity allows developers and data scientists to easily build, deploy, and iterate on sophisticated data-driven e-democracy tools and other opinion-gathering applications.

[![Video about LitePolis](image_with_play_button(1).png)](https://www.canva.com/design/DAGkKYnWMIE/acGGYFVWpYpFA-t65YcyWw/watch?embed)

## Who Is This For?

- **Deployers** — you want to run a Polis-like system with minimal setup
- **Developers** — you want to build custom routers, middleware, or database adapters as LitePolis packages

---

## Quick Start (Deployers)

### 1. Install

Requires Python 3.12+ and pip.

```bash
pip install litepolis
```

### 2. Set up your package list

LitePolis uses a `packages.txt` file (like `requirements.txt`) to declare which packages your deployment needs. The default location is `~/.litepolis/packages.txt`.

A minimal Polis-compatible deployment looks like:

```
litepolis-database-default==0.1.0
litepolis-router-default==0.1.0
```

To add or remove packages from this list via CLI:

```bash
# Add a package (automatically records the installed version)
litepolis-cli deploy add-deps litepolis-router-default

# Add a specific version
litepolis-cli deploy add-deps litepolis-router-default==1.0.0

# Remove a package
litepolis-cli deploy remove-deps litepolis-router-default

# See what's declared vs what's installed
litepolis-cli deploy list-deps
```

You can also edit `~/.litepolis/packages.txt` directly — it's plain text, one `package==version` per line, with `#` comments supported.

### 3. Install all declared packages

```bash
litepolis-cli deploy sync-deps
```

This reads your `packages.txt` and installs everything to the pinned versions. Run this after editing the file manually or when setting up on a new machine.

### 4. Generate config

```bash
litepolis-cli deploy init-config
```

This reads your installed packages, collects their default config values, and writes them to `~/.litepolis/config.conf`. Then edit the file to set secrets, database paths, etc.:

```bash
nano ~/.litepolis/config.conf
```

### 5. Serve

```bash
# Start serving (connects to an existing Ray cluster or starts one)
litepolis-cli deploy serve

# Or: start a local Ray head node and serve in one step
litepolis-cli deploy local
```

The API will be available at `http://localhost:8000/api/v3/` by default.

### Custom packages file location

If you manage multiple deployments or want to keep your packages file elsewhere:

```bash
litepolis-cli deploy --packages-file ./my-deployment.txt serve
```

### Connecting to a Ray cluster

```bash
litepolis-cli deploy --cluster ray://<head-node-ip>:10001 serve
```

---

## Browsing Available Packages

The [Awesome LitePolis](https://newjerseystyle.github.io/Awesome-LitePolis/) directory is scanned daily from GitHub and lists available routers, databases, middleware, and UI packages (including works in progress).

---

## Quick Start (Package Developers)

LitePolis packages follow a strict naming convention:

| Type | Name pattern | Example |
|---|---|---|
| Router | `litepolis-router-*` | `litepolis-router-default` |
| Database | `litepolis-database-*` | `litepolis-database-default` |
| Middleware | `litepolis-middleware-*` | `litepolis-middleware-auth` |
| UI | `litepolis-ui-*` | `litepolis-ui-admin` |

### Scaffold a new package

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

---

## Future developments

- StarRocks database backend
- Google Cloud deployment with autoscale

---

## Related

- [litepolis-router-default](https://github.com/NewJerseyStyle/LitePolis-router-default) — default Polis-compatible API router
- [litepolis-database-default](https://github.com/NewJerseyStyle/LitePolis-database-default) — default Polis-compatible database layer
- [Awesome LitePolis](https://newjerseystyle.github.io/Awesome-LitePolis/) — package directory
