def addTwoNumbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        n1=str(l1[-1])
        n2=str(l2[-1])
        l=[]
        for i in range(len(l1)):
            if i != 0:
                n1=n1+str(l1[len(l1)-i-1])
        for i in range(len(l2)):
            if i != 0:
                n2=n2+str(l2[len(l2)-i-1])
        n3 = int(n1) + int(n2)
        for i in str(n3):
            l.append(i)
        l.reverse()
        return l

print(addTwoNumbers([2,3,4],[2,3]))
print(addTwoNumbers([2,3,4,7,5],[2,3,0,8,7]))
print(addTwoNumbers([0],[8,9]))
print(addTwoNumbers([9,9,9,9,9,9,9],[9,9,9,9]))
print(addTwoNumbers([8,9],[9,9]))
print(addTwoNumbers([0],[0]))
print(addTwoNumbers([0,7,9],[8,9]))