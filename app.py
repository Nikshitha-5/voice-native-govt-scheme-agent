from record_audio import record_audio
from stt import speech_to_text
from agent import agent_process
from tts import speak

def run_app():
    print("🎤 Telugu Voice Government Scheme Agent Started")

    record_audio("input.wav", duration=5)

    user_text = speech_to_text("input.wav")
    print("🗣 User:", user_text)

    response = agent_process(user_text)
    print("🤖 Agent:", response)

    speak(response)

if __name__ == "__main__":
    run_app()
