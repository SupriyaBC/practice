
# skills = ["python","devops", "mlops", "docker", "kubernates"]
# scores=[]
# def add_skill(skills, name):
#    skills.append(name)

# add_skill(skills, "aiops")

# for skill in skills:
#    score = int(input(f"enter score for {skill}\n "))
#    scores.append(score)

# def calculate_avg(scores):
#    avg = sum(scores)/len(scores)
#    print(f"{avg:.2f}")

# def display_skills(skills):
#     for number, skill in  enumerate (skills, start=1):
#        print(f"{number}.{skill}")

# calculate_avg(scores)
# display_skills(skills)




skills ={}

# def add_skill(skills, name, score):
#     skills[name] = score

# def calculate_avg(skills):
#     avg = sum(skills.values())/len(skills)
#     print(f"\nAverage skill rating : {avg:.2f}/10")    

# def display_skills(skills):
#     for number, (skill,score) in enumerate(skills.items(), start=1):
#         print(f"{number}. {skill}: {score/10}")

# n = int(input("how many skills u want to enter: "))

# for i in range (n):
#     name = input("enter a skill name: ")
#     score = int(input(f"enter score for the {name}: "))

#     add_skill(skills, name, score)

# calculate_avg(skills)
# display_skills(skills)



#largest number

numbers = ["5", "-6", "78"]


def find_max(numbers):
    largest = int(numbers[0])

    for num in numbers:
        num = int(num)
        if largest < num:
            largest = num

    return (largest)        

result = find_max(numbers)

print(result)        