class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums3=list[int]
        nums3=nums1+nums2
        nums3.sort()
        length=len(nums3)
        median=0
        if length%2==0:
            z=length//2
            e=nums3[z]
            q=nums3[z-1]
            median=(e+q)/2
        else:
            z=length//2
            median=nums3[z]
            return median
            
        return median    
            
