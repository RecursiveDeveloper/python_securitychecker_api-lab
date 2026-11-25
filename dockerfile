FROM python:3.12.16-slim

WORKDIR /app/

COPY app/requirements.txt .
RUN pip install -r requirements.txt

COPY app/ .

EXPOSE 5000/tcp

CMD ["python3", "server.py"]
