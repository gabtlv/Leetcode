class Solution(object):
    def isPalindrome(self, x):
        """
        convert to a string first
        compare first and last part of the string
        """
        s = str(x)
        for i in range(len(s)):
            if s[i] != s[-1-i]:
                return False
        return True
        