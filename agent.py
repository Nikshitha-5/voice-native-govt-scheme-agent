from memory import load_memory, save_memory
from tools.eligibility import check_eligibility
from tools.scheme_db import SCHEME_DB

def planner(memory):
    if "income" not in memory:
        return "ASK_INCOME"
    if "gender" not in memory:
        return "ASK_GENDER"
    if "farmer" not in memory:
        return "ASK_FARMER"
    return "CHECK_ELIGIBILITY"

def agent_process(user_text):
    memory = load_memory()

    # Simple Telugu info extraction
    if "స్త్రీ" in user_text:
        memory["gender"] = "female"
    if "పురుషుడు" in user_text:
        memory["gender"] = "male"
    if "రైతు" in user_text:
        memory["farmer"] = True
    if "లక్ష" in user_text:
        memory["income"] = 150000

    save_memory(memory)

    action = planner(memory)

    if action == "ASK_INCOME":
        return "దయచేసి మీ వార్షిక ఆదాయం చెప్పండి."
    if action == "ASK_GENDER":
        return "మీ లింగం ఏమిటి?"
    if action == "ASK_FARMER":
        return "మీరు రైతునా?"

    schemes = check_eligibility(memory)

    if not schemes:
        return "క్షమించండి, మీకు అర్హత ఉన్న పథకాలు లేవు."

    response = "మీకు అర్హత ఉన్న ప్రభుత్వ పథకాలు:\n"
    for s in schemes:
        response += f"{s} – లాభం: {SCHEME_DB[s]['benefit']}\n"

    return response
age
