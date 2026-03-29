def togle_case(string):
    f =""
    for i in string:
        if i.islower():
            x = i.upper()
            f += x
        elif i.isupper():
            x = i.lower()
            f += x
        else:
            f += i
    return(f)
print(togle_case("HelloWorld123#4%rTuW"))