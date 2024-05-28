class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        h_length = len(haystack)
        n_length = len(needle)
      
        for i in range(h_length ):
            n_pointer = 0 

            while n_pointer < n_length and i + n_pointer < h_length and haystack[i + n_pointer] == needle[n_pointer]:
                n_pointer += 1
                print(i + n_pointer)

            if n_pointer == n_length:
                return i

        return -1        