FROM alpine:latest
RUN apk add --no-cache netcat-openbsd

WORKDIR /app
ENV PATH="/app:${PATH}"
COPY run /app
RUN chmod 755 /app/*

# Wireguard interface configs go in /config
VOLUME /config

# Wireguard interface dir is /interface
VOLUME /interface

EXPOSE 80

CMD ["run"]
