FROM python:3.8-alpine

LABEL maintainer="samedamci@disroot.org"

ENV TOKEN TOKEN

COPY requirements.txt /requirements.txt

RUN apk add --no-cache gcc musl-dev linux-headers libc-dev libffi-dev libressl-dev && \
	pip install -r requirements.txt && \
	mkdir /opt/bot &&\
	echo $TOKEN > /opt/bot/environment && \
	apk del gcc musl-dev linux-headers libc-dev libressl-dev

COPY . /opt/bot/

CMD cd /opt/bot/ && python3 main.py
