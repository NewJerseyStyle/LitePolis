# LitePolis

LitePolis is a refactored version of [Polis](https://github.com/compdemocracy/polis),
built using Python and optimized for scalability and performance.
We've incorporated a data lakehouse using [StarRocks](https://www.starrocks.io/),
a powerful and scalable analytics engine,
and adopted a Model-View-Controller
([MVC architecture](https://en.wikipedia.org/wiki/Model%E2%80%93view%E2%80%93controller))
architecture to ensure seamless integration and flexibility.

**Scalability at its Core**

Our MVC architecture enables horizontal scaling at all three levels,
making it easy to add new features and support large-scale applications:

* **Controller**: Scale your application by developing and distributing client-side web or mobile applications using our RESTful API.
* **View**: Scale your views by horizontally scaling Docker instances and adding load balancing to your infrastructure.
* **Model**: Scale your data processing by adjusting the number of StarRocks instances using [Kubernetes](https://github.com/StarRocks/starrocks-kubernetes-operator/tree/main/examples/starrocks) on cloud infrastructure.

This flexible architecture allows you to focus on building your application, while we handle the scalability and performance.

## Getting started
Under development...
<!-- something about deployment and configuration -->
### Tryout
use all in one dockerfile
## Advanced usage
### Separate storage
https://www.starrocks.io/blog/four-simple-ways-to-deploy-starrocks
### Separate front end
disable `streamlit`
develop your own front end web/mobile/desktop application with RESTful API docs
### Product deployment
- MVC architecture
- Data lakehouse
  - https://www.starrocks.io/blog/four-simple-ways-to-deploy-starrocks
- scaling
  - scaling of UI
  - scaling of API server
  - scaling of database

## Developer manual
- [Features List](feature.md)
- [Server-side Architecture](architect.md)
- [Database implementation detail](database.md)
### Algorithms
- [Polis: Scaling Deliberation by Mapping High Dimensional Opinion Spaces](https://www.e-revistes.uji.es/index.php/recerca/article/download/5516/6558/28347) (DOI: http://dx.doi.org/10.6035/recerca.5516)
- [Algorithm of clustring, dimension reduction and more](https://compdemocracy.org/algorithms/)
- [Representative Comments ranking algorithm](https://compdemocracy.org/Representative-Comments/)
