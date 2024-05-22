FROM debian:latest

RUN apt update
RUN DEBIAN_FRONTEND=noninteractive TZ=Etc/UTC apt install \
        python3 \
        python3-pip \
        git \
        iproute2 \
        procps \
        tree -y

RUN pip3 install --break-system-packages Zope[wsgi]==5.9 -c https://zopefoundation.github.io/Zope/releases/5.9/constraints.txt

RUN pip3 install --break-system-packages psycopg2-binary \
    Products.PythonScripts \
    Products.ZSQLMethods \
    Products.SiteErrorLog \
    Products.StandardCacheManagers \
    Products.ExternalMethod \
    Products.MailHost \
    git+https://github.com/perfact/ZPsycopgDA \
    git+https://github.com/Klappson/docker-utils.git \
    zope.mkzeoinstance \
    Paste

COPY fs/ /

RUN pip3 install --break-system-packages /root/zopemods

WORKDIR /root
RUN mkwsgiinstance -u dockerzope:12345 -d wsgi

ENTRYPOINT [ "StartZope" ]