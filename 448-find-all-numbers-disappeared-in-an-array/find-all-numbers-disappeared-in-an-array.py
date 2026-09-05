class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
       numbers = set(nums)
       result = []

       for i in range(1, len(nums) + 1):
            if i not in numbers:
                result.append(i)

       return result 