class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        dect_s1 = collections.defaultdict(int)
        dect_s2 = collections.defaultdict(int)
        left_p = 0
        right_p = 0

        if len(s1) > len(s2):
            return False
        # updated dict with s1 char
        for c in s1:
            dect_s1[c] += 1      

        # updated 1st window in dict for s2
        while right_p < len(s1):
            dect_s2[s2[right_p]] += 1
            right_p += 1
            
        print(right_p)

        # iterate on s2 
        for j in range(len(s2) - len(s1) + 1):
            window = s2[j : j + len(s1)]
            print(window)

           
            if dect_s1 == dect_s2:
                return True

          
            if right_p < len(s2):
                dect_s2[s2[right_p]] += 1
                right_p += 1

           
            if dect_s2[window[0]] == 1:
                del dect_s2[window[0]]
           

        return False
           