FROM python:3.8-slim
USER root

COPY . /opt/test113/
WORKDIR /opt/test113/

RUN apt update && \
    apt install -y build-essential libssl-dev libffi-dev python3-dev cargo zlib1g-dev && \
    pip3 install --upgrade pip && \
    pip3 install -r /opt/test113/requirements.txt && \
    apt install -y openssl curl && \
    apt remove -y build-essential libssl-dev libffi-dev python3-dev cargo && \
    apt autoremove -y && \
    apt clean -y && \
    rm -f /etc/apt/sources.list && \
    rm -rf /var/lib/apt/lists/*

ENTRYPOINT ["/usr/bin/python3", "/opt/test113/test113"]
