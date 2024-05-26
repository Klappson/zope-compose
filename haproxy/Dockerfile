FROM debian:latest

RUN apt update
RUN apt install haproxy \
    procps \
    curl \
    git \
    python3 \
    python3-pip \
    iproute2 -y

RUN pip3 install --break-system-packages git+https://github.com/Klappson/docker-utils.git

COPY fs/ /

ENTRYPOINT [ "StartHaProxy" ]
