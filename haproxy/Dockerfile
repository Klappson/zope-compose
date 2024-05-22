FROM debian:latest

RUN apt update
RUN apt install haproxy \
    procps \
    iproute2 -y

COPY fs/ /

ENTRYPOINT [ "StartHaProxy" ]
