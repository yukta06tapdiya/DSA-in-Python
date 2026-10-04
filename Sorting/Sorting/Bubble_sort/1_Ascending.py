# TC-avg & wirst--O(n^2)
# TC- best case if false condition is given --O(n)
# SC-O(1)
def bubbleSort(arr):
        
    n=len(arr)
    for i in range(n-2,-1,-1):
        is_swap=False
        for j in range(0,i+1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
                is_swap=True
        if is_swap==False:
            break

nums=[5,8,1,6,9,2,4]
bubbleSort(nums)
print(nums)
