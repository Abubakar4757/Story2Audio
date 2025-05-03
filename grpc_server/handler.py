# grpc_server/handler.py
from tts_engine.kokoro_tts import KokoroTTS

class TTSHandler:
    def __init__(self):
        self.tts = KokoroTTS()

    def generate_audio(self, text: str) -> bytes:
        output_path = "grpc_output.wav"
        self.tts.synthesize(text, output_path)

        with open(output_path, "rb") as f:
            audio_bytes = f.read()
        return audio_bytes
