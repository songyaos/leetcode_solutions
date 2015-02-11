class Solution:
    # @return an integer
    def numTrees(self, n):
        if n==0:
            return 1
        elif n==1:
            return 1
        else:
            return sum([self.numTrees(i)*self.numTrees(n-i-1) for i in range(n)])
               