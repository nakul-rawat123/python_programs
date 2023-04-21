list1 = ['Nakul','apple','Ram,','abc','XYZ']
new_list = []
for i in list1:
    if i[0].isupper():
        new_list.append(i)
print(new_list)