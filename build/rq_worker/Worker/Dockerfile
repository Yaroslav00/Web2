FROM python:3-alpine
RUN apk update && apk add --no-cache python3-dev  supervisor
RUN pip3 install --upgrade pip

WORKDIR /app
RUN pip3 install redis rq
COPY . .

CMD ["/usr/bin/supervisord", "-c", "supervisord.conf"]