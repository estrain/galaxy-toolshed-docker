# Galaxy Tool Shed Docker (Galaxy 23.1)

This repository provides a ready-to-use Docker container for running the [Galaxy Tool Shed](https://galaxyproject.org/toolshed/) — a platform for hosting, sharing, and installing Galaxy tools. Hosting a local [toolshed](https://galaxyproject.org/toolshed/hosting-a-local-toolshed/) is not recommened but can be useful for testing and development.

Built on **Galaxy 23.1**, this container includes:
- Galaxy Tool Shed web app
- NGINX reverse proxy
- Persistent database, logs, and optional tool data
- Optional support for custom configuration and plugin overrides

---

## Quick Start

### Prerequisites
- Docker
- Docker Compose

### Clone and Run

```bash
git clone https://github.com/estrain/galaxy-toolshed-docker.git
cd galaxy-toolshed-docker
docker-compose up --build
```
### Create Admin Account
Log into image, such as http://localhost:9010, and register an account for admin@example.com. This will create an administration account and then you can create tool categories to begin uploading and hosting tool repositories.
