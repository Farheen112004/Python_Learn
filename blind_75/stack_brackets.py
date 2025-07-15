class Solution:
    def func(self, s: str) -> bool:
        stack = []
        brackets = {')': '(', '}': '{', ']': '['}
        
        for c in s:
            if c in brackets:
                if stack and stack[-1] == brackets[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        
        return not stack  # returns True if stack is empty, False otherwise
s = "({[]})"
sol = Solution()
print(sol.func(s))