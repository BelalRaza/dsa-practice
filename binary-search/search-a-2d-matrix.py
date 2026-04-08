link="https://leetcode.com/problems/search-a-2d-matrix/description/"

class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        row =len(matrix[0])
        for i in range(len(matrix)):
    
                if target<= matrix[i][-1] and target >= matrix[i][0]:
                    # print("got it")
                    s=0
                    e=row-1
                    while s<=e:
                        mid=(s+e)//2
                        # print("mid",matrix[i][mid])
                        if matrix[i][mid]==target:
                            return True
                        elif matrix[i][mid]<target:
                            s=mid+1
                        else:
                            e=mid-1
        return False
                
        
  
        