class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i =0
        for j in range(i,len(nums)):
            if nums[j]== 0:
                nums[j]= nums[i]
                nums[i]=0
                i+=1
        
        for j in range(i,len(nums)):
            if nums[j]== 1:
                nums[j]= nums[i]
                nums[i]=1
                i+=1
        
        for j in range(i,len(nums)):
            if nums[j]== 2:
                nums[j]= nums[i]
                nums[i]=2
                i+=1