def nested_sum(lst):
    s=0
    for i in lst:
        if type(i)!=list:
            s=s+i
        else:
            s=s+(nested_sum(i))
    return s

print(nested_sum([1,[2,[3,4],[]],5]))
print(nested_sum([]))
print(nested_sum([2,4,[4,6,[5,[],5,[1,90,[]]]]]))