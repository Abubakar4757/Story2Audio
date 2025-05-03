# tts_engine/kokoro_tts.py

from kokoro import KPipeline
import numpy as np
import soundfile as sf

class KokoroTTS:
    def __init__(self, voice='af_heart', lang_code='a', speed=1):
        self.pipeline = KPipeline(lang_code=lang_code)
        self.voice = voice
        self.speed = speed

    def synthesize(self, text: str, output_path: str = 'output.wav') -> str:
        generator = self.pipeline(text, voice=self.voice, speed=self.speed, split_pattern=None)

        all_audio = []
        for i, (gs, ps, audio) in enumerate(generator):
            print(f"Segment {i}: {gs} -> {ps}")
            all_audio.append(audio)

        final_audio = np.concatenate(all_audio)
        sf.write(output_path, final_audio, 24000)
        return output_path
