class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        currentps = 0
        pm = defaultdict(int)
        pm[currentps]+=1
        count=0
        for num in nums:
            currentps+=num
            previousps = currentps -k
            if previousps in pm:
                count+=pm[previousps]
            pm[currentps]+=1
        return count

