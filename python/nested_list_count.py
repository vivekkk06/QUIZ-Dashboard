def nested_list_count(lst):
    
    n=1
    for i in lst:
        if type(i)==list:
            n=n+nested_list_count(i)
    return n
print(nested_list_count([[1,3],[2,[3]]]))
print(nested_list_count([1,[2,[3,[]]]]))
print(nested_list_count([[1],[2,[3,[4]]]]))
