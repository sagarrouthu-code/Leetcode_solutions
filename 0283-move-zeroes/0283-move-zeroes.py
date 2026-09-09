class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        l = -1

        for i in range(len(nums)):

            if nums[i] == 0:
                l = i
                break
            
        if l == -1:
            return

        for r in range( l + 1 , len(nums)):
            if nums[r] != 0:
                nums[l] , nums[r] = nums[r] , nums[l]
                l += 1


            
            
       
        