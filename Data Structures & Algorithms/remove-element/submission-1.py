class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        l= len(nums)
        count =0
        for i in range(0,l):
            if nums[i] == val:
                for j in range(i,l):
                    if nums[j]!=val:
                        nums[i] = nums[j]
                        nums[j] = val
                        break
        print(nums)
        for num in nums:
            if num!=val:
                count+=1
        return count
                    