'''
Given a string s consists of some words separated by spaces, return the length of the last word in the string. If the last word does not exist, return 0.

A word is a maximal substring consisting of non-space characters only.
'''

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        #Clean up string 
        s_clean = s.strip()
        length:int = 0
        
        for i in range(1,(len(s_clean)+1)):
            if s_clean[-i] == ' ':
                break
            else:
                length += 1
                continue
        
        return length 
