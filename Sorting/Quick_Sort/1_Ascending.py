# TC-O(nlogn)--best/avg
# WC-O(n^2)
# SC-O(1)
class Solution:
    def quick_sort(self,nums,low,high):
        if low<high:
            p_ind=self.partition(nums,low,high)
            self.quick_sort(nums,low,p_ind-1)
            self.quick_sort(nums,p_ind+1,high)

    def partition(self,nums,low,high):
        pivot=nums[low]
        i=low
        j=high
        while i<j:
            while nums[i]<pivot and i<=high-1:
                i+=1
            while nums[j]>pivot and j>=low+1:
                j-=1
            if i<j:
                nums[i],nums[j]=nums[j],nums[i]
        nums[low],nums[j]=nums[j],nums[low]
        return j






