# #with indexing
num=[5,-2,3,9,0,6,10,7]
def rotate(nums):
    n=len(nums)
    nums[:]=[nums[-1]]+nums[0:n-2]
    return nums

print(rotate(num))

# without indexing
def rotate(nums):
    n=len(nums)
    temp=nums[n-1]
    for i in range(n-2,-1,-1):
        nums[i+1]=nums[i]
    nums[0]=temp
    return nums
print(rotate(num))

#TC=O(N)
#SC=O(1)