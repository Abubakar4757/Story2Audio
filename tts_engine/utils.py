# tts_engine/utils.py

import os

def is_valid_text(text: str) -> bool:
    return isinstance(text, str) and len(text.strip()) > 0

def file_exists(path: str) -> bool:
    return os.path.isfile(path)
