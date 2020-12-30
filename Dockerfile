FROM tiangolo/uvicorn-gunicorn-fastapi

COPY ./app /app

# Wireguard interface configs go in /data/config
VOLUME /data/config

# Wireguard interface dir is /data/interface
VOLUME /data/interface
