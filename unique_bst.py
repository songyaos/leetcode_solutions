class Solution:
    # @return an integer
    def numTrees(self, n):
        result = [0 for _ in range(n+1)]
        result[0] = 1
        for i in range(n+1):
            for j in range(i):
                result[i] =result[i] + result[j]*result[i-j-1]

        return result[n]    