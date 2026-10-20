class Solution:
    def isPalindrome(self, s: str) -> bool:
        a= ""
        for c in s:
            if c in "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890":
                a+=c
        l,r =0 , len(a)-1
        a= a.lower()
        while l<r:
            if a[l]!=a[r]:
                return False
            l+=1
            r-=1
        return True