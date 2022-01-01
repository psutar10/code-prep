class Solution:
    def isPalindrome(self, x: int) -> bool:
        num = str(x)
        new_list = num[::-1]
        if new_list == num:
            return True
        else:
            return False
