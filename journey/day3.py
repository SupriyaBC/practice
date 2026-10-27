# records = [{"name": "Model_A", "accuracy":1.92, "latency":120},
#            {"name":"Model_B", "accuracy":1.20, "latency":100},
#            {"name":"", "accuracy":0.85, "latency":-5},
#            {"name":"Model_D", "accuracy":0.88, "latency":150}
#            ]

# def validate_record(records):

#     errors =[]
#     valid_count =0
#     invalid_count=0


#     for i,rec in enumerate(records, start=1):
#         is_valid = True
#         if (rec["name"]==""):
#             errors.append((f"Record:{i} : name should not be empty"))
#             is_valid = False

#         if (rec["latency"]<0):
#             errors.append((f"Record:{i} :latency should not be negative"))
#             is_valid = False

#         if (rec["accuracy"]<0 or rec["accuracy"]>1):
#             errors.append((f"Record:{i} : accuracy should be between 0 and 1"))
#             is_valid=False

#         if is_valid:
#             valid_count+=1  
#         else:
#             invalid_count+=1      

#     print(valid_count)
#     print(invalid_count)    
#     return errors

# errors = validate_record(records)
# print(errors)


 
    

#find duplicate values
numbers = [4,2,7,2,4,9,7,7]
liss=[]

def duplicate_numbers(numbers):
    for num in numbers:
        if numbers.count(num)>1 and num not in liss:
            liss.append(num)

    return liss    

result = duplicate_numbers(numbers)
print(result)


    
         



    