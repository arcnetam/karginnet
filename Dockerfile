FROM python:3.11-slim

WORKDIR /app

COPY main.py .
COPY requirements.txt .

# Install any dependencies (if needed in the future)
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 2323

CMD ["python", "main.py"]
