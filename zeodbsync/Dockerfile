FROM debian:latest

RUN apt update
RUN DEBIAN_FRONTEND=noninteractive TZ=Etc/UTC apt install \
    git \
    python3 \
    python3-pip \
    iproute2 \
    procps \
    tree -y

RUN pip3 install --break-system-packages Zope[wsgi]==5.9 -c https://zopefoundation.github.io/Zope/releases/5.9/constraints.txt

RUN pip3 install --break-system-packages zope.mkzeoinstance \
    psycopg2-binary \
    Products.PythonScripts \
    Products.ZSQLMethods \
    Products.SiteErrorLog \
    Products.StandardCacheManagers \
    Products.ExternalMethod \
    Products.MailHost \
    git+https://github.com/perfact/ZPsycopgDA \
    perfact-zodbsync \
    git+https://github.com/Klappson/docker-utils.git \
    Paste

COPY fs/ /

RUN chmod +x /usr/bin/StartZeodbSync
RUN printf '#!/bin/sh\nexit 0' > /usr/sbin/policy-rc.d 

WORKDIR /root
RUN mkwsgiinstance -u dockerzope:12345 -d wsgi
RUN mkzeoinstance zeo

ENTRYPOINT [ "StartZeodbSync" ]
