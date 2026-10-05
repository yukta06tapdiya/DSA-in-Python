#Brute Force
# TC=O(nlogn)
nums=[55,32,97,-55,45,32,88,21]
nums.sort()
print(nums[-2])

# Better
# TC=O(2n)==(O(n))
def largest(nums):
    largest=float("-inf")
    s_largest=float("-inf")
    n=len(nums)
    for i in range(0,n):
        largest=max(largest,nums[i])
    for i in range(0,n):
        if nums[i]>s_largest and nums[i]!=largest:
            s_largest=nums[i]
    return s_largest
print(largest(nums))

#optimal
#TC=O(n)
def largest(nums):
    largest=float("-inf")
    s_largest=float("-inf")
    n=len(nums)
    for i in range(0,n):
        if nums[i]>largest:
            s_largest=largest
            largest=nums[i]
        elif nums[i]>s_largest and nums[i]!=largest:
            s_largest=nums[i]
    return s_largest
print(largest(nums))