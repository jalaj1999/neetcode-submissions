class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        seen={}
        ans =[]
        n = len(nums)
        for num in nums:
            if num in seen:
                seen[num]+=1
            else:
                seen[num]=0
        print(seen,n//3)
        for num in nums:
            if seen[num]>= n//3 and num not in ans:
                ans.append(num)

        return ans