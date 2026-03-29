def is_increasing(lst):
    l=[True]
    for i in range(1,len(lst)):
        if(lst[i-1]<lst[i]):
            l.append(True)
        else:
            l.append(False)
    if(False in l):
        return False
    else:
        return True

print(is_increasing([1,9,7,0]))
print(is_increasing([1,2,2,3]))
print(is_increasing([10]))
print(is_increasing([-8,0]))
print(is_increasing([]))

#   more good solution
#   for i in range(1,len(lst)):
#      if lst[i-1]<lst[i]:
#          return False
#   return true