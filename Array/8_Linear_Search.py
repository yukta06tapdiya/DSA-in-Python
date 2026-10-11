def linear(nums,target):
    n=len(nums)
    for i in range(0,n):
        if nums[i]==target:
            return i
    return -1
nums=[1,2,3,4,5,6,7]
target=4
print(linear(nums,target))
