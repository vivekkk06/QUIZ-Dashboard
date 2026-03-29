'''
def twoSum(nums: list[int], target: int) -> list[int]:
        for i in nums:
            for j in nums:
                if nums.index(i) != nums.index(j):
                    if i+j == target:
                        return [nums.index(i), nums.index(j)]
'''
def twoSum(nums: list[int], target: int) -> list[int]:
    for i in range(len(nums)):
        for j in range(len(nums)):
            if i != j:
                if nums[i] + nums[j] == target:
                    return [i,j]


print(twoSum([3,2,4], 6))
print(twoSum([3,3], 6))
print(twoSum([3,8,9,7,1,3,6], 6))
print(twoSum([0,8,2,4,6,5], 6))