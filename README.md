# LitePolis
![](https://img.shields.io/badge/status-under_development-red) ![](https://img.shields.io/badge/release-no_release-red)

Python port of [polis](https://github.com/compdemocracy/polis)
try to be data scientist friendly and easy to deploy
support horizontal scaling on cloud

## Getting started
Under development...
<!-- something about deployment and configuration -->

## Developer manual
### Tech stack
```mermaid
  title Containers
  graph TD;
      Streamlit-->FastAPI;
      FastAPI-->StarRock;
      StarRock-->*storage;
```
*storage: Such as Amazon S3, Google Cloud Storage, Azure Blob Storage, and other S3-compatible storage

Access control is provided by `Streamlit-Authenticator`
