FROM python:3.11-slim

WORKDIR /app

COPY oop_inventory.py .

CMD ["python", "oop_inventory.py"]