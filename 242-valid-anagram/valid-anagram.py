class Solution(object):
    def isAnagram(self, s, t):
        # take both strings
        # rearrange in alphabetical order, then compare each letter to see if 
        # it is a valid anagram
        # check if they are the same length first
        
        if len(s) != len(t):
            return False
        
        sortedS = sorted(s)
        sortedT = sorted(t)

        for i in range(len(s)):
            if sortedS[i] != sortedT[i]:
                return False
        return True