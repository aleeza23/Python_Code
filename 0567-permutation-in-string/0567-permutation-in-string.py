# class Solution:
#     def checkInclusion(self, s1: str, s2: str) -> bool:
#         dect_s1 = collections.defaultdict(int)
#         dect_s2 = collections.defaultdict(int)
#         left_p = 0
                 

#         for c in s1:
#             dect_s1[c] += 1
  

#         for right_p in range(1 , len(s2)):
#             dect_s2[s2[left_p]] += 1
#             dect_s2[s2[right_p]] += 1
            
#             if dect_s1 == dect_s2:
#                 return True

#             if dect_s2[s2[left_p]] == 1:
#                 del dect_s2[s2[left_p]]
#                 dect_s2[s2[right_p]] = 0
#             left_p += 1

#         return False    


import collections

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        dect_s1 = collections.defaultdict(int)
        dect_s2 = collections.defaultdict(int)

        if len(s1) < len(s2):
            return False

        # Populate dect_s1 with the frequency of characters in s1
        for c in s1:
            dect_s1[c] += 1

        left_p = 0
        right_p = 0

        # Initialize dect_s2 with the counts of the first window in s2
        while right_p < len(s1):
            dect_s2[s2[right_p]] += 1
            right_p += 1

        # Slide the window across s2
        for j in range(len(s2) - len(s1) + 1):
            window = s2[j : j + len(s1)]

            # Check if the current window matches dect_s1
            if dect_s1 == dect_s2:
                return True

            # Update dect_s2 for the next window
            if right_p < len(s2):
                dect_s2[s2[right_p]] += 1
                right_p += 1

            # Update dect_s2 for the characters going out of the window
            if dect_s2[window[0]] == 1:
                del dect_s2[window[0]]
            else:
                dect_s2[window[0]] -= 1

        return False


    

           