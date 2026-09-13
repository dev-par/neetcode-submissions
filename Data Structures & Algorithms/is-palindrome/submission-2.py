class Solution:
    def isPalindrome(self, s: str) -> bool:
        # case insensitive and ignores all non alphanumeric characters 
        # palindrome is where reading the string forward and backward is the same order of
        # characters

        # use a pointer at the front and back. each iteration, move them to the next 
        # alphanumeric character
        # if they differ, return false. Once they converge on the same character or 
        # further, return true

        i = 0
        j = len(s) - 1

        while i < j:
            while i < j and not s[i].isalnum():
                i += 1
            while i < j and not s[j].isalnum():
                j -= 1
            
            if s[i].lower() != s[j].lower():
                return False
            i += 1
            j -= 1
        
        return True