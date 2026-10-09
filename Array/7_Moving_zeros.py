def moving(nums):
    left=0
    n=len(nums)
    for right in range(n):
        if nums[right]!=0:
            nums[left],nums[right]=nums[right],nums[left]
            left+=1

num=[1,0,2,4,3,0,0,3,5,1]
moving(num)
print(num)

