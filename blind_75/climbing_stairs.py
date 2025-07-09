class Solution:
    def climbStairs(self, n ):
        #reccursive
        def dfs(i):
            if i == 0 or i == 1:
                return 1
            return dfs(i - 1) + dfs(i - 2)
        return dfs(n)
