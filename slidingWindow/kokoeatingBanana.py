link ="https://leetcode.com/problems/koko-eating-bananas/submissions/1976905551/"

class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
    
        """

        # print(piles[-1])
        # for i in range(piles[-1]+1):
        start=1
        end=max(piles)
        while(start<end):
            # temp=0
            mid=(start+end)//2

            temp=0
            for i in piles:
                temp+=(i//mid)
                if i%mid !=0:
                    temp+=1


            if temp<=h  :

                end=mid
            elif temp>h  :
                start=mid+1
        return start
            
        