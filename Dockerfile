#syntax:docker/dockerfile:1
 
FROM python:3.13-slim
 
WORKDIR app/

RUN apt-get update && apt-get install -y \
uvicorn

COPY . .

WORKDIR /app/src

RUN python3 -m venv venv

COPY requirements.txt requirements.txt

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 9000

CMD ["uvicorn", "main:app", "--reload", "--host", "0.0.0.0", "--port", "9000"]