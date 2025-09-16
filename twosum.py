class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        check = {}
        for i, num in enumerate(nums):
            needed = target - num
            if needed in check:
                return [check[needed], i]
            check[num] = i
