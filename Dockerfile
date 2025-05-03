# Use a lightweight Python image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy only requirements first to leverage Docker cache
COPY requirements.txt .

# Upgrade pip and install dependencies early (cached if unchanged)
RUN pip install --upgrade pip && \
    pip install --default-timeout=100 --retries=10 --timeout=30 -r requirements.txt

# Now copy the rest of your project
COPY . .

# Make start.sh executable
RUN chmod +x start.sh

# Expose both ports
EXPOSE 50051 8501

# Start both servers
CMD ["./start.sh"]
