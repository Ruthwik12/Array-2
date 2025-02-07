# time complexity is o(n), where n is the size of the input
# space complexity is o(1)
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        res = list()
        if(len(nums) == 0):
            return res
        for i in range(len(nums)):
            idx = abs(nums[i]) - 1
            if nums[idx] > 0:
                nums[idx] *= -1
        for i in range(len(nums)):
            if(nums[i] > 0):
                res.append(i+1)
            else:
                nums[i] *= -1
        return res
        