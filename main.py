from stt import listen_telugu
from tts import speak_telugu
from planner import plan
from executor import execute
from evaluator import evaluate
from memory import memory, update_memory

def extract(text):
    if "వయస్సు" in text:
        update_memory("age", int(''.join(filter(str.isdigit,text))))
    if "ఆదాయం" in text:
        update_memory("income", int(''.join(filter(str.isdigit,text))))
    if "రాష్ట్రం" in text:
        update_memory("state", text)

speak_telugu("ప్రభుత్వ పథకాల సహాయకుడికి స్వాగతం")

while True:
    t = listen_telugu()
    if not t:
        speak_telugu("మళ్లీ చెప్పండి")
        continue
    extract(t)
    action = plan(memory)
    if action=="ASK_AGE":
        speak_telugu("మీ వయస్సు ఎంత?")
    elif action=="ASK_INCOME":
        speak_telugu("మీ ఆదాయం ఎంత?")
    elif action=="ASK_STATE":
        speak_telugu("మీ రాష్ట్రం పేరు చెప్పండి")
    else:
        res = execute(action,memory)
        if evaluate(res)=="SUCCESS":
            speak_telugu("మీకు అర్హమైన పథకాలు")
            for r in res: speak_telugu(r)
        else:
            speak_telugu("పథకం దొరకలేదు")
        break
