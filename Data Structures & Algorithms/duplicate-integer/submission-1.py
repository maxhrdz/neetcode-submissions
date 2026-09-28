class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        vistos = set()
        for n in nums:
            if n in vistos:
                return True
            else:
                vistos.add(n)
        return False