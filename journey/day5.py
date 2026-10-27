
# models = [
#     {"name": "Model_A", "accuracy": 0.92, "latency": 120},
#     {"name": "Model_B", "accuracy": 1.20, "latency": 100},
#     {"name": "", "accuracy": 0.85, "latency": -5},
#     {"name": "Model_D", "accuracy": 0.98, "latency": 150}
# ]


# def is_eligible(model):
#     errors = []

#     if not model["name"]:
#         errors.append("name should not be empty")

#     if not (0 < model["accuracy"] <= 1):
#         errors.append("accuracy must be greater than 0 and at most 1")
#     elif model["accuracy"] < 0.90:
#         errors.append("accuracy must be at least 0.90")

#     if model["latency"] < 0 or model["latency"] > 200:
#         errors.append("latency must be between 0 and 200")

#     return errors


# def evaluate_model(model):
#     errors = is_eligible(model)
#     return {
#         "name": model["name"],
#         "passed": len(errors) == 0,
#         "errors": errors
#     }


# def evaluate_models(models):
#     results = []

#     for model in models:
#         results.append(evaluate_model(model))

#     return results


# def select_release_candidate(models):
#     eligible_models = []

#     for model in models:
#         if is_eligible(model) == []:
#             eligible_models.append(model)

#     if not eligible_models:
#         print("No eligible release candidate found.")
#         return None

#     best_model = max(
#         eligible_models,
#         key=lambda model: model["accuracy"]
#     )

#     print(f'{best_model["name"]} is the release candidate.')

#     for model in models:
#         if model is best_model:
#             continue

#         errors = is_eligible(model)

#         if errors:
#             name = model["name"] or "Model_C"
#             print(f'{name} failed its tests: {", ".join(errors)}')
#         else:
#             print(f'{model["name"]} passed, but was not selected.')

#     return best_model


# report = evaluate_models(models)

# for item in report:
#     print(item)

# print("\nRelease report:")
# candidate = select_release_candidate(models)






    
scores =[85,92,76,92,88, 88, 87, 85] 

def second_highest_distinct_score(scores):
    highest = float('-inf')
    sechigh = float('-inf')
    for score in scores:
        if score > highest:
            sechigh = highest
            #print(sechigh)
            highest = score
            #print(highest)
                
        elif score < highest and score > sechigh:
            sechigh = score

    if sechigh == float('-inf'):
        return None
    return sechigh   

result = second_highest_distinct_score(scores)
print(result)
             

# scores = [85, 92, 76, 92, 88, 88, 87, 85]

# def second_highest_unique_score(scores):
#     highest = float('-inf')
#     second_highest = float('-inf')

#     for score in scores:
#         if scores.count(score) == 1:
#             if score > highest:
#                 second_highest = highest
#                 highest = score
#             elif score > second_highest:
#                 second_highest = score

#     if second_highest == float('-inf'):
#         return None

#     return second_highest

# result = second_highest_unique_score(scores)
# print(result)

    



