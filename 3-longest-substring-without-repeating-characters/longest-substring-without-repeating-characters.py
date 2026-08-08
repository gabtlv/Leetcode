class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        1. get the input and iterate through the letters until it detects the initial character and also does an iteration of a counter
        2. once detected, it goes to the next character in the string repeating the same process in step 1.
        3. once it reaches the end of the string, the loop terminates and returns the highest count
        """
        
        window = set() # holds only the characters in the window
        left = 0 # the left side of the window
        max_length = 0 # the maximum length of the window recorded

        #sliding window, the right expands while the left edge shrinks by 1 until the duplicate character is no longer inside of the window.
        for right in range(len(s)):
            # if s[right] is a duplicate, shrink the left side until it is gone
            while s[right] in window:
                window.remove(s[left]) # kick out left edge character in window
                left += 1 # move the left edge forward
            window.add(s[right]) # keep adding 1 since no duplicate left in the window
            # update max length by taking the highest length between current window or max_length
            max_length = max(max_length, right - left + 1) 
        return max_length
        