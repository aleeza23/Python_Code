class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        window_start = 0
        window_end = 2
        good_str = 0

        while window_end < len(s):
            if s[window_start] != s[window_start + 1] != s[window_end] != s[window_start] :
                good_str += 1
            
            window_start += 1
            window_end += 1

        return good_str       


        