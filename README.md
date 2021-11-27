News Fetcher
---

### Introduction

News Fetcher is a simple project with the following functionality:
 - Fetch latest news form APIs 
 - Validate the fetched news data
 - Print the result (news articles) after validation
 - Rerun the previous steps every 5 minutes using celery and celery beat 

### Technologies

News Fetcher uses a number of open source projects to work properly:

* [Python](https://www.python.org) - is a class-based, object-oriented programming language that is designed to have as few implementation dependencies as possible.
* [Pip](https://pypi.org/project/pip/) - is a package-management system written in Python used to install and manage software packages.
* [Celery](https://docs.celeryproject.org/) - Celery is an open source asynchronous task queue or job queue which is based on distributed message passing. While it supports scheduling, its focus is on operations in real time.
* [Flower](https://flower.readthedocs.io/) - Celery flower is a web based tool for monitoring and administrating Celery clusters.
* [Redis](https://redis.io/) - Redis is an in-memory data structure store, used as a distributed, in-memory key–value database, cache and message broker, with optional durability
* [Docker](https://www.docker.com/) - is a set of platform as a service (PaaS) products that use OS-level virtualization.
* [Docker Compose](https://docs.docker.com/compose/) - is a tool for running multi-container applications on Docker.

And of course News Fetcher itself is open source with a [public repository]()
 on GitHub.

### Install and run

```sh
$ Clone the repository `clone `
$ Go into the project folder and execute `docker-compose up --build`
$ The app should be up and running and fetching the news and print it every 5 mintutes in the console
```

### Flower
```sh
$ Open http://localhost:5000/
$ This Flower montroing tool to monitor the celery workers and see how many time the task runs and time of each run.
```

### Todos
 - Write test cases for New Fetcher
 - Store the news articles in the database