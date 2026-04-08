link = "https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/description/"


class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        "first"
        
        s=0
        n=len(nums)
        e=n-1
        start=-1
        end=-1
        arr=[-1,-1]
        while s<=e:
            mid=(s+e)//2
            if nums[mid]==target:
                start=mid
                e=mid-1
            elif nums[mid]<target:
                s=mid+1
            else:
                e=mid-1
            
        print(start)

        s=0
        e=n-1
        
        while(s<=e):
            mid=(s+e)//2
            if nums[mid]==target:
                end=mid
                s=mid+1
            elif nums[mid]<target:
                s=mid+1
            else:
                e=mid-1
        print(end)
        
        arr[0]=start
        arr[1]=end
        return arr
        