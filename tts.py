from TTS.api import TTS
import os

tts = TTS("tts_models/te/indic/vits")

def speak(text):
    os.makedirs("audio", exist_ok=True)
    output_file = "audio/output.wav"
    tts.tts_to_file(text=text, file_path=output_file)

    if os.name == "nt":
        os.system(f"start {output_file}")
    else:
        os.system(f"aplay {output_file}")
