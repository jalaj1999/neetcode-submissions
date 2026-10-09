
class Solution:
    def getDic(self, a: str) -> Dict:
        dic = {}
        for c in a:
            if c in dic:
                dic[c] += 1
            else:
                dic[c] = 1
        return dic

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}

        for word in strs:
            dic = self.getDic(word)

            # Convert dictionary into a hashable key
            key = tuple(sorted(dic.items()))

            if key not in groups:
                groups[key] = []

            groups[key].append(word)

        return list(groups.values())
