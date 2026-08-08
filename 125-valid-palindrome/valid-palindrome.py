class Solution(object):
    def isPalindrome(self, s):
        """
        1. get the input s and clean the string by removing the symbols, making everything lowercase, remove all spaces
        2. compare first and last character and start moving towards the middle
        3. check if it is an empty string, if it is return True
        """

        #check if it is empty
        if len(s) == 1:
            return True
        # cleaning the string
        clean = "".join(char.lower() for char in s if char.isalnum())
        print(clean)

        # compare
        for i in range(len(clean)):
            if clean[i] != clean[-1-i]:
                return False
        return True
        