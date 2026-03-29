'''
def print_words(str1):
    lst = []
    for i in str1:
        lst.append(i)
    for j in range(len(lst)):
        print(f"{j}:{lst[j].upper()}")
print(print_words("nitin thakur"))
'''
str="nitin thakur"

x = str.split(" ")
print(x)
for i in range(len(x)):
    print(f"{i+1}: {x[i].upper()}")
