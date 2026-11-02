class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for digit in nums:
            if digit in count:
                count[digit] += 1
            else:
                count[digit] = 1

        ordered = sorted(count, key=count.get, reverse=True)
        return ordered[:k]