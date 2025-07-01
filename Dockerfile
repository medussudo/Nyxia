# Engine 
FROM python:3.10-slim

# Working Directory
WORKDIR /app

# Copying files
COPY . .

RUN pip install --upgrade pip
RUN pip install "setuptools<58"

RUN pip install --no-cache-dir -r requirements.txt

# Command that runs the bot
CMD ["python3", "nyxia.py"]