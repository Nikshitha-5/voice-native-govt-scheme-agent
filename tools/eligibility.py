def check_eligibility(user):
    eligible = []

    if user.get("gender") == "female" and user.get("income", 0) < 200000:
        eligible.append("మహిళా సమృద్ధి యోజన")

    if user.get("farmer") is True:
        eligible.append("రైతు భరోసా")

    return eligible
