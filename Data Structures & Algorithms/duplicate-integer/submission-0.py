class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        vistos = set()
        for num in nums: 
            if num in vistos:
                return True
            else:
                vistos.add(num)

        return False