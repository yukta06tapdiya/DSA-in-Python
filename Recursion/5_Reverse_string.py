# TC-->O(n/2)==O(n)
# SC-->O(n)--> Stack space
def rev(num,left,right):
    if left>=right:
        return num
    
    num[left],num[right]=num[right],num[left]
        
    return rev(num,left+1,right-1)
nums=[4,7,3,2,6,1,5,9]
print(rev(nums,0,len(nums)-1))
