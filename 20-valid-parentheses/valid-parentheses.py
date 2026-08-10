class Solution:
    def isValid(self, s: str) -> bool:
       # this question involves stacks. you push the parentheses into the stack and if it is the opening bracket.
       # You pop the stack if you encounter a closed bracket. You will use a dictionary and make the opening bracket
       # The key and the closed bracket the value.

        pairs = {
            "(":")",
            "{":"}",
            "[":"]"
        }
        
        stack = []
        
        for char in s:
            if char in pairs:
                stack.append(char)
            else:
                if not stack or pairs[stack[-1]] != char:
                    return False
                stack.pop()
        return len(stack) == 0