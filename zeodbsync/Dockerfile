FROM ubuntu:latest

RUN apt update
RUN apt install git python3 python3-pip tree -y

RUN pip3 install zope zope.mkzeoinstance \
    git+https://github.com/perfact/zodbsync

COPY fs/ /

RUN chmod +x /usr/bin/StartZeodbSync
RUN printf '#!/bin/sh\nexit 0' > /usr/sbin/policy-rc.d 

WORKDIR /root
RUN mkwsgiinstance -u dockerzope:12345 -d wsgi
RUN mkzeoinstance zeo

ENTRYPOINT [ "StartZeodbSync" ]