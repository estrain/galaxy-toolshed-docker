#!/bin/bash
set -e

# Start cron for whoosh index
cron &

# Set working dir
cd /home/galaxy/galaxy

# Start Galaxy Tool Shed as galaxy user
echo "Starting Galaxy Tool Shed..."
sudo -u galaxy bash -c "
    source /home/galaxy/galaxy/.venv/bin/activate && \
    sh run_tool_shed.sh --daemon
"

# Start NGINX in foreground
echo "Starting NGINX..."
exec nginx -c /etc/nginx/nginx.conf -g 'daemon off;'

