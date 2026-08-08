class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return []
        res=[]
        
        rowbegin=0
        columnbegin=0
        rowend=len(matrix)-1
        columnend=len(matrix[0])-1
        
        while(rowbegin<=rowend and columnbegin<=columnend):
            #left to right
            for j in range(columnbegin,columnend+1):
                res.append(matrix[rowbegin][j])
            rowbegin+=1
            #top to bottom
            for i in range(rowbegin,rowend+1):
                res.append(matrix[i][columnend])
            columnend-=1
            #right to left
            if rowbegin<=rowend:

                for j in range(columnend,columnbegin-1,-1):
                    res.append(matrix[rowend][j])
                rowend-=1
            if columnbegin<=columnend:
                for i in range(rowend,rowbegin-1,-1):
                    res.append(matrix[i][columnbegin])  
                columnbegin+=1
        return res
        