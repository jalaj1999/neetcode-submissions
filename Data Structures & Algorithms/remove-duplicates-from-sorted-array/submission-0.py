class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        seen=set()
        ans =[]
        for num in nums:
            if num in seen:
                continue
            else:
                ans.append(num)
                seen.add(num)
        nums.clear()
        for num in ans:
            nums.append(num)
        return len(ans)