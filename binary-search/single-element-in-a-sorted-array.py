link = "https://leetcode.com/problems/single-element-in-a-sorted-array/description/"

class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        s=0
        e=n-1
        mid=(s+e)//2 

        if n==1:
            return nums[mid]
        elif nums[0]!=nums[1]:
            return nums[0]
        elif nums[-1] != nums[n-2]:
            return nums[-1]


        while(s<=e):
            mid=(s+e)//2



            if nums[mid]!=nums[mid-1] and nums[mid]!=nums[mid+1]:
                return nums[mid]
            elif  (mid%2==0 and (nums[mid]==nums[mid+1])) or ( mid%2!=0 and (nums[mid]==nums[mid-1])):
                s=mid+1
            else:
                e=mid-1


        
