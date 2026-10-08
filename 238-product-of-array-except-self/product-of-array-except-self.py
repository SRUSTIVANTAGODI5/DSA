class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)

        answer = [1] * n

        # Left products
        left = 1

        for i in range(n):
            answer[i] = left
            left = left * nums[i]

        # Right products
        right = 1

        for i in range(n - 1, -1, -1):
            answer[i] = answer[i] * right
            right = right * nums[i]

        return answer