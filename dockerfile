FROM python:3.11.0

WORKDIR /app

COPY ./requirements.txt /app

RUN apt-get update \
    && apt-get install gcc -y \
    && apt-get clean

RUN pip install -r ./requirements.txt && rm -rf /root/.cache/pip

COPY . /app/

CMD ["uvicorn","app.main:app","--host","0.0.0.0","--port","80"]