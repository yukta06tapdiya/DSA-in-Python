# tc=O(n)
# sc=O(1)
#method1
def largest_element(nums):
    largest=nums[0]
    n=len(nums)
    for i in range(0,n):
        largest=max(largest,nums[i]) 
        #if nums[i]>largest: 
            #largest=nums[i]
    return largest

num=[55,32,-90,99,-3,67]
print(largest_element(num))

#method2
def largest_element(nums):
    largest=float("-inf")
    n=len(nums)
    for i in range(0,n):
        largest=max(largest,nums[i])
    return largest

num=[55,32,-90,99,-3,67]
print(largest_element(num))

