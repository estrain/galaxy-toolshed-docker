#!/bin/bash
set -e

echo "Rebuilding Tool Shed Whoosh index..."

cd /home/galaxy/galaxy
source .venv/bin/activate

python scripts/tool_shed/build_ts_whoosh_index.py \
    -c config/tool_shed.yml \
    --config-section tool_shed \
    -d

echo "Whoosh index rebuild complete at $(date)"

