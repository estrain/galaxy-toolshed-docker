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
```
### Setup Directory
Create a data folder and a certs folder in the galaxy-toolshed-docker folder. The data folder will persist and contains the uploaded tools along with a few other files. The certs folder should contain the keys defined config/ngninx.conf.

```bash
mkdir data certs
# Copy ssl keys and modify config/ngnix.conf if needed
docker-compose up --build
```
### Create Admin Account
Log into image, such as https://localhost, and register an account for admin@example.com. This will create an administration account and then you can create tool categories to begin uploading and hosting tool repositories.

### Tool Index
The tool index is built during start up.  If you add a tool you will either need to wait 5 minutes for the indexing cron job to run or go into the container and execute the commands below.

```bash
source .venv/bin/activate
python scripts/tool_shed/build_ts_whoosh_index.py -c config/tool_shed.yml --config-section tool_shed -d
```

