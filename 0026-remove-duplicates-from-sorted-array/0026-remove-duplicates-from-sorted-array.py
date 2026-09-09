class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        s = 0

        for f in range(1 , len(nums)):

            if nums[s] != nums[f]:
                nums[s+1] = nums[f]
                s += 1

        return s+1

        