# def calculate_average_score(scores):
#     return sum(scores) / len(scores)

# skills = {
#     "machine_learning": 4,
#     "python": 5,
#     "DevOps": 3,
#     "Cloud":1
# }

# for skill, score in skills.items():
#     print(f"{skill}: {score}/10")

# average = calculate_average_score(list(skills.values()))

# print(f"\nAverage skill rating: {average:.2f}/10")


# name = input("Enter your name:")
# python = int(input ("how many minutes studied python:"))
# linux = int(input("how many minutes studied linux:"))
# total = python + linux 
# print(f"{name} studied for {total//60} hours and {total%60} minutes")

#score = int(input("Enter your score:"))

def calculate_score(score):
    #score = int(input("Enter your score:"))
    if score < 0 or score > 100:
        print("Enter valid score")
    else:
        if score <=30:
            print("fail")
        elif 30 < score <=60:
            print("pass")
        elif 60 < score <=80:
            print("Distinction")
        else:
            print("top")

calculate_score(89)   

