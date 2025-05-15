# syntax=docker/dockerfile:1.4

FROM ubuntu:20.04

LABEL maintainer="Errol Strain <estrain@gmail.com>"
LABEL version="23.1-toolshed"
LABEL description="Docker image for hosting Galaxy Tool Shed (Galaxy 23.1)"

ENV DEBIAN_FRONTEND=noninteractive

# Install system dependencies
RUN apt-get update && apt-get install -y \
    python3 \
    python3-venv \
    python3-pip \
    git \
    nginx \
    net-tools \
    vim \
    curl \
    make \
    build-essential \
    libffi-dev \
    libssl-dev \
    libpq-dev \
    zlib1g-dev \
    libbz2-dev \
    libreadline-dev \
    libsqlite3-dev \
    sudo \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Install Node.js 16 and Yarn
RUN curl -fsSL https://deb.nodesource.com/setup_16.x | bash - \
    && apt-get update \
    && apt-get install -y nodejs \
    && npm install -g yarn@1.22.19 \
    && node -v && yarn -v

# Create galaxy user with sudo access
RUN useradd -m -u 1001 -s /bin/bash galaxy && \
    usermod -aG sudo galaxy && \
    echo "galaxy ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers

# Clone Galaxy 23.1
USER galaxy
RUN git clone -b release_23.1 https://github.com/galaxyproject/galaxy.git /home/galaxy/galaxy

# Use bash shell for subsequent RUN commands
SHELL ["/bin/bash", "-c"]

# Switch to galaxy user
USER galaxy
WORKDIR /home/galaxy/galaxy

# Clean up .git
RUN rm -Rf .git

# Setup nginx temp directory
RUN mkdir -p /home/galaxy/nginx_temp && \
    chown -R galaxy:galaxy /home/galaxy/nginx_temp

# Create virtual environment and install Python dependencies
RUN python3 -m venv .venv && \
    source .venv/bin/activate && \
    pip install --upgrade pip && \
    pip install -r requirements.txt

# Build JavaScript client (required for Tool Shed UI)
RUN source .venv/bin/activate && make client

# Expose Tool Shed HTTP port
EXPOSE 80 
EXPOSE 443 

# Switch to root to copy config and setup nginx
USER root

# Copy configuration files
COPY config/nginx.conf /etc/nginx/nginx.conf
COPY config/galaxy.yml /home/galaxy/galaxy/config/galaxy.yml
COPY config/tool_shed.yml /home/galaxy/galaxy/config/tool_shed.yml

# Set config file ownership
RUN chown galaxy:galaxy /home/galaxy/galaxy/config/galaxy.yml
RUN chown galaxy:galaxy /home/galaxy/galaxy/config/tool_shed.yml

# Setup logging
RUN mkdir -p /home/galaxy/galaxy/logs && \
    touch /home/galaxy/galaxy/logs/nginx.error.log /home/galaxy/galaxy/logs/nginx.access.log && \
    chown -R galaxy:galaxy /home/galaxy/galaxy/logs && \
    ln -sf /home/galaxy/galaxy/logs/nginx.error.log /var/log/nginx/error.log && \
    ln -sf /home/galaxy/galaxy/logs/nginx.access.log /var/log/nginx/access.log

# Copy startup script
COPY scripts/start.sh /usr/local/bin/start.sh
RUN chmod +x /usr/local/bin/start.sh

# Default command
ENTRYPOINT ["/usr/local/bin/start.sh"]

