````markdown
# Story2Audio

**Story2Audio** is an AI-powered application that converts written stories into engaging audio using a custom TTS (Text-to-Speech) pipeline. It wraps a Kokoro TTS model inside a gRPC microservice and exposes a simple frontend for generating and listening to audio stories.

---

## 🚀 Features

- Input a story via frontend (Gradio or Streamlit)
- Generate natural-sounding audio using Kokoro TTS
- Containerized using Docker for easy deployment
- Concurrent, microservice-based architecture

---

## 🛠️ Technologies Used

- Python 3.10
- gRPC
- Kokoro TTS
- Streamlit / Gradio (Frontend)
- Docker

---

## 📦 How to Run the App (Using Docker)

### 1. Clone the repository

```bash
git clone https://github.com/your-username/story2audio.git
cd story2audio
````

### 2. Build the Docker image

```bash
docker build -t story2audio-app .
```

> This step may take time depending on your internet speed as dependencies are installed inside the container.

### 3. Run the Docker container

```bash
docker run -p 50051:50051 -p 8501:8501 story2audio-app
```

* `50051`: gRPC service
* `8501`: Frontend interface (Streamlit or Gradio)

Once the container is running, open your browser and go to:

```
http://localhost:8501
```

---

## 🧪 Local Development (Optional)

If you're not using Docker and want to run locally:

### 1. Create a virtual environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 2. Install dependencies

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### 3. Start the app

```bash
chmod +x start.sh
./start.sh
```

---

## 📁 Project Structure (Simplified)

```
story2audio/
│
├── app/                  # Core application logic
├── start.sh              # Script to run gRPC and frontend
├── Dockerfile            # Docker configuration
├── requirements.txt      # Python dependencies
└── README.md             # Project info
```

---
