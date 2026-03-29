def longestAlternating(nums):
    for i in nums:
        nums.remove(i)
    for j in len(nums):
        if diff(j) > 0:
            if diff(j+1) < 0:
                l.append(j)

def diff(j):
    a = nums[j]-nums[j+1]
    return a

l=[]
def lst(j):
    if diff(j) > 0:
        if diff(j+1) < 0:
            l.append(j)
    if diff(j) < 0:
        if diff(j+1) > 0:
            l.append(j)