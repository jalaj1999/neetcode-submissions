class Solution:
    def isPalindrome(self, s: str) -> bool:
        l,r =0, len(s)-1
        while l<r:
            if s[l]!=s[r]:
                return False
            l+=1
            r-=1
        return True
            
    def validPalindrome(self, s: str) -> bool:
        if self.isPalindrome(s):
            return True
        l,r =0, len(s)-1
        count =1
        
        while s[l] == s[r] and l!=r:
            l+=1
            r-=1
            
        if l==r:
            return True
        return self.isPalindrome(s[l:r]) or self.isPalindrome(s[l+1:r+1])

            
        