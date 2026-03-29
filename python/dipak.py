d = int(input("enter marks:"))
if d > 33:
    print("pass")
    if d > 60:
        print("good")
        if d>80:
            print("first class")            # 80-100
        else:
            print("too good")               # 60-80
    else:
        print("marks btween 33 to 60")
else:
    print("fail")
