class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        alphastrs = []
        for word in strs:
            alphastrs.append("".join(sorted(word)))

        groups = {}
        for i in range(len(strs)):
            key = alphastrs[i]
            if key in groups:
                groups[key].append(strs[i])
            else:
                groups[key] = [strs[i]]

        return list(groups.values())
            