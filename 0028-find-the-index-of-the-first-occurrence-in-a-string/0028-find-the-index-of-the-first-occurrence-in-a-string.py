class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        h_length = len(haystack)
        n_length = len(needle)

      
        for i in range(h_length - n_length + 1):
            h_pointer = i
            n_pointer = 0          

            while n_pointer < n_length and haystack[h_pointer] == needle[n_pointer]:
                h_pointer += 1
                n_pointer += 1
                print(h_pointer, n_pointer)                

            if n_pointer == n_length:
                return i
        return -1    

        