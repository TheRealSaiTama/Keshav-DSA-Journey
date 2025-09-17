class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        n = len(nums)
        leftside = [1] * n

        for i in range(1, n):
            product *= nums[i-1]
            leftside[i] = product

        rightside = [1] * n
        product = 1
        for i in range(n-2, -1, -1):
            product *= nums[i+1]
            rightside[i] = product

        result = [1] * n
        for i in range(n):
            result[i] = leftside[i] * rightside[i]
        return result

# O(1) space 

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(n)
        result = [1] * n

        for i in range(1, n):
            result[i] = result[i-1] * nums[i-1]

        right = 1
        for i in range(n-1, -1, -1):
            result[i] *= right
            right *= nums[i]

        return result 