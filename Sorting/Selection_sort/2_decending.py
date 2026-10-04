def selection_sort(nums):
    n=len(nums)
    for i in range(n-1,-1,-1):
        max_index=i
        for j in range(i-1,-1,-1):
            if nums[j]>nums[max_index]:
                max_index=j
            nums[j],nums[max_index]=nums[max_index],nums[j]
    return nums
        
nums=[5,7,8,4,1,6,9,2]
print(selection_sort(nums))


