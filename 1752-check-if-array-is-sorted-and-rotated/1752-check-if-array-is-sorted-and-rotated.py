class Solution:
    def check(self, nums: List[int]) -> bool:

        drop = 0

        for i in range(len(nums)):
            if nums[i] > nums[(i+1)% len(nums)]:
                drop += 1
                

        if drop == 1 or drop == 0:
            return True

        else:
            return False
        