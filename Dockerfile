FROM python:3.11-slim

WORKDIR /app

COPY . .

CMD ["python", "inventory_manager_with_classes.py"]