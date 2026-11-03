class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = ""

        s = s.lower()
        
        for i in s:
            if i.isalnum():
                cleaned += i

        if cleaned == cleaned[::-1]:
            return True
        else:
            return False    
        