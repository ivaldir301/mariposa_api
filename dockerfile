#syntax:docker/dockerfile:1

FROM python:3.13-slim

WORKDIR app/

RUN apt-get update && apt-get install -y \
uvicorn

COPY . .

WORKDIR /app/src

COPY requirements.txt requirements.txt

RUN pip install --upgrade pip

RUN pip install -r requirements.txt

ENV PORT=8080

EXPOSE 8080

CMD ["uvicorn", "main:app", "--reload", "--host", "0.0.0.0", "--port", "8080"]
