res1=[]
res2=[]

def merge_sorted(res1,res2):
    #res1=sorted(list1)
    #res2=sorted(list2)
    i=0
    j=0
    result=[]

    while i<len(res1) and j<len(res2):
        if res1[i]<=res2[j]:
            result.append(res1[i])
            i+=1
        else:
            result.append(res2[j])
            j+=1

    while i<len(res1):
        result.append(res1[i])
        i+=1
    while j<len(res2):
        result.append(res2[j])  
        j+=1

    return result

print(merge_sorted(res1,res2))   

