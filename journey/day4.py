models = [{"name": "Model_A", "accuracy":0.92, "latency":120},
           {"name":"Model_B", "accuracy":1.20, "latency":100},
           {"name":"", "accuracy":0.85, "latency":-5},
           {"name":"Model_D", "accuracy":0.98, "latency":150}
           ]

def is_eligible(model):
    if not model["name"]:
        return False

    if not (0 < model["accuracy"]<= 1):
        return False

    if model["accuracy"]<0.90:
        return False

    if (model["latency"] < 0 or model["latency"] > 200):
        return False

    return True
    
def select_best_model(models):
    best_model = None
    for rec in models:
        if is_eligible(rec):
            if best_model is None or rec["accuracy"] > best_model["accuracy"]:
                best_model = rec

    if best_model is not None:
        return best_model["name"]

    return None

def generate_report(models):
    total= len(models)
    eligible=0
    ineligible = 0

    for rec in models:
        if is_eligible(rec):
            eligible += 1
        else:
            ineligible += 1

    
    best_model = select_best_model(models)

    print("Total models:", total)
    print("Eligible models:", eligible)
    print("Ineligible models:", ineligible)
    print("Best model:", best_model)

    return best_model
    
final = generate_report(models)
print("Returned value:", final)




       
