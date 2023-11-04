FROM python:3.12-alpine3.18

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt 
RUN apk add --update --no-cache postgresql-client jpeg-dev
RUN apk add --update --no-cache --virtual .tmp-build-deps \
    gcc libc-dev linux-headers postgresql-dev musl-dev zlib zlib-dev
RUN pip install -r /requirements.txt
RUN apk del .tmp-build-deps

RUN mkdir /airbed
WORKDIR /airbed
COPY ./airbed /airbed

RUN mkdir -p /vol/web/media
RUN mkdir /vol/web/static
RUN adduser -D raymond
RUN chown -R raymond:raymond /vol/
RUN chmod -R 755 /vol/web
USER raymond