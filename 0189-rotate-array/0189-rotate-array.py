class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        k = k % len(nums)

        l = 0
        r = len(nums) - 1

        while l < r:
            nums[l] , nums[r] = nums[r] , nums[l]
            l += 1
            r -= 1

        left = 0
        right = k -1

        while left < right:

            nums[left] , nums[right] = nums[right] , nums[left]
            left += 1
            right -= 1

        l1 = k
        r1 = len(nums) -  1

        while l1 < r1:

            nums[l1] , nums[r1] = nums[r1] , nums[l1]
            l1 += 1
            r1 -= 1
        