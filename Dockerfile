FROM python:3.7-alpine

RUN apk update && apk add gcc python3-dev musl-dev

ENV FLASK_APP main.py
ENV FLASK_CONFIG staging

RUN adduser -D flasky
USER flasky

WORKDIR /home/flasky

COPY requirements.txt requirements.txt

RUN python -m venv venv
RUN venv/bin/pip install -r requirements.txt

COPY app app
COPY main.py config.py boot.sh ./

# runtime configuration
EXPOSE 5000
ENTRYPOINT ["./boot.sh"]