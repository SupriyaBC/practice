
models = [
    {"name": "Model_A", "accuracy": 0.92, "latency": 120},
    {"name": "Model_B", "accuracy": 1.20, "latency": 100},
    {"name": "", "accuracy": 0.85, "latency": -5},
    {"name": "Model_D", "accuracy": 0.98, "latency": 150}
]


def is_eligible(model):
    errors = []

    if not model["name"]:
        errors.append("name should not be empty")

    if not (0 < model["accuracy"] <= 1):
        errors.append("accuracy must be greater than 0 and at most 1")
    elif model["accuracy"] < 0.90:
        errors.append("accuracy must be at least 0.90")

    if model["latency"] < 0 or model["latency"] > 200:
        errors.append("latency must be between 0  to 200")

    return errors


def evaluate_model(model):
    errors = is_eligible(model)
    return {
        "name": model["name"],
        "passed": len(errors) == 0,
        "errors": errors
    }


def evaluate_models(models):
    results = []

    for model in models:
        results.append(evaluate_model(model))

    return results


def select_release_candidate(models):
    eligible_models = []

    for model in models:
        if is_eligible(model) == []:
            eligible_models.append(model)

    if not eligible_models:
        print("No eligible release candidate found.")
        return None

    best_model = max(
        eligible_models,
        key=lambda model: model["accuracy"]
    )

    print(f'{best_model["name"]} is the release candidate.')

    for model in models:
        if model is best_model:
            continue

        errors = is_eligible(model)

        if errors:
            name = model["name"] or "Model_C"
            print(f'{name} failed its tests: {", ".join(errors)}')
        else:
            print(f'{model["name"]} passed, but was not selected.')

    return best_model

if __name__ == "__main__":
    report = evaluate_models(models)

    for item in report:
        print(item)

    print("\nRelease report:")
    candidate = select_release_candidate(models)


# #most frequent number

# numbers = [4,2,4,3,2,4,5,2,2]
# def most_frequent_number(numbers):
#     counts={}
#     for num in numbers:
#         if num in counts:
#             counts[num]+=1
#         else:
#             counts[num]=1

#     highest=0
#     result = None
#     for num, count in counts.items():
#         if count > highest:
#             highest = count
#             result = num

#     return result

# final = most_frequent_number(numbers)
# print(final)