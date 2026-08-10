numbers=[2,2,5,5,5,8,6]
print("original_list:",numbers)

unique=[]
for n in numbers:
    if n not in unique:
        unique.append(n)
print(unique)
