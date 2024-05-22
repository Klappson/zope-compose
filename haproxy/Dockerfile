FROM debian:latest

RUN apt update
RUN apt install haproxy \
    procps \
    curl \
    iproute2 -y

COPY fs/ /

ENTRYPOINT [ "StartHaProxy" ]
