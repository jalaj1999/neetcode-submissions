class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        data = {}
        for num in nums:
            if num in data:
                data[num]+=1
            else:
                data[num]=1
        ans = dict(sorted(data.items(), key=lambda item: item[1], reverse=True))
        ans = list(ans)
        final_ans = []
        for i in range(0,k):
            final_ans.append(ans[i])
        return final_ans
        