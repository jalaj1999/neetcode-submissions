class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set()
        for num in nums:
            seen.add(num)
        ans =0 
        for num in nums:
            last =-1
            cur_length =0
            if num in seen and num -1 not in seen :
                last = num
            while last in seen:
                cur_length+=1
                last+=1
            ans = max(ans,cur_length)
        return ans
            
            
        