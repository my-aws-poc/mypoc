FROM python:3.10

WORKDIR /

COPY mypoc mypoc
COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt --no-cache-dir

ENV FLASK_APP mypoc

ENTRYPOINT ["flask", "run", "--host=0.0.0.0", "--port=80"]
