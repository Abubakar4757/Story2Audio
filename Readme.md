Story2Audio Generator

The Story2Audio Generator is a web-based application that transforms written stories into expressive audio using Kokoro TTS. The app uses gRPC for communication between the frontend and the backend, and allows users to enter a story in text form and listen to the generated audio.

🚀 Setup
Prerequisites
Before getting started, make sure you have the following installed:

Python 3.7+

pip (Python package manager)

gRPC & Protobuf libraries for Python

Streamlit for the web interface

1. Clone the repository
bash
Copy
Edit
git clone https://github.com/your-repository-url.git
cd your-repository
2. Install Dependencies To install all necessary dependencies, run:

bash
Copy
Edit
pip install -r requirements.txt
This will install the following:

grpcio – gRPC library for Python.

streamlit – Web framework for the user interface.

protobuf – For serializing the messages used in gRPC.

Kokoro TTS – Text-to-Speech engine (or any other TTS model you are using).

If Kokoro TTS or other model dependencies are not included, please follow their installation instructions.

🖥️ Usage
Starting the gRPC Server
First, start the gRPC server by running the following command in the grpc_server directory:

bash
Copy
Edit
python run_server.py
This starts a gRPC server listening on localhost:50051 to receive requests for audio generation.

Starting the Streamlit Web App
To launch the frontend interface, run the following command:

bash
Copy
Edit
streamlit run app.py
The web application will be available at http://localhost:8501. You can input your story, click "Generate Audio," and listen to the result.

🏗️ Architecture
Overview
The system consists of two main components:

gRPC Server (run_server.py):

Hosts the Story2AudioService that listens for gRPC requests.

Upon receiving a request, it processes the text and generates audio using the Kokoro TTS engine (or any chosen TTS model).

Sends the audio content back to the client in the form of a response.

Streamlit Web App (app.py):

A web-based interface that allows users to input their story.

Sends the story text to the gRPC server via a TextRequest message.

Receives the audio content and plays it back in the UI.

Communication Flow
Frontend (Streamlit)

The user enters a story in the text area and clicks "Generate Audio."

The frontend sends a gRPC request to the backend server with the story text.

Backend (gRPC Server)

The server processes the request, uses the Kokoro TTS engine (or any other TTS model), and generates audio.

The server returns the generated audio back to the frontend.

Frontend (Streamlit)

The frontend receives the audio content and plays it back to the user.

🔧 Model Sources
The TTS model used in this application is Kokoro TTS (or any other compatible model you are using for text-to-speech generation).

Kokoro TTS: You can refer to the official Kokoro TTS documentation for model installation and configuration instructions.

Other models can be substituted by replacing the TTS engine within the run_server.py script.

⚠️ Limitations
Text Length: Very long stories may result in processing delays or failures due to memory limitations or server constraints. It’s recommended to limit the text input to a few paragraphs.

Audio Quality: The quality of generated audio may vary depending on the TTS engine used. Kokoro TTS provides expressive speech synthesis, but the output may not always perfectly match human-like intonations or pronunciations.

Internet Connectivity: If using external TTS services, a stable internet connection is required to access the model API.

Error Handling: The app handles some basic errors, but there may still be edge cases where text input is not properly processed.

💡 Future Improvements
Enhanced Error Handling: Improve error detection and user-friendly messages.

Audio Customization: Add options for customizing voice styles (e.g., pitch, speed, accent).

Scalability: Optimize the backend for handling multiple simultaneous requests (e.g., using cloud deployment).

Save/Download Audio: Allow users to download the generated audio files.

📬 Contact
If you have any questions or feedback, feel free to reach out:

Email: abubakar4757@gmail.com


