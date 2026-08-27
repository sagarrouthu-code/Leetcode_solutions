class Solution:
    def isPalindrome(self, x: int) -> bool:
        original_x = x
        rev = 0

        if x < 0:
            return False


        while (original_x > 0):

            digit = original_x % 10
            rev = rev * 10 + digit
            original_x = original_x // 10
        
        final_rev = rev 

        

        if final_rev == x:
            return True
        else:
            return False