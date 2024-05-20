class Solution:
    def isPalindrome(self, s: str) -> bool:
        alphanum = [c.lower() for c in s if c.isalnum()]
        cleaned_s = ''.join(alphanum)

        left_p = 0
        right_p  = len(cleaned_s) - 1

        while left_p < right_p:
            if cleaned_s[left_p] != cleaned_s[right_p]:
                return False
            else:
                left_p += 1
                right_p -= 1
        return True             
    



            
        

        
            
        