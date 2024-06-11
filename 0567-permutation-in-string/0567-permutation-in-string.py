class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        dect_s1 = collections.defaultdict(int)
        dect_s2 = collections.defaultdict(int)

        window_size = len(s1)

        if len(s1) > len(s2):
            return False

        # updated dict with s1 char
        for c in s1:
            dect_s1[c] += 1      

        # compute the 1st window
        for i in range(window_size):
            dect_s2[s2[i]] += 1            

        # iterate on s2 
        for j in range(len(s2) - len(s1) + 1):
            # window = s2[j : j + len(s1)]
            # print(window)

           
            if dect_s1 == dect_s2:
                return True

          
            if j + window_size < len(s2) - len(s1) + 1:
                dect_s2[s2[j + window_size]] += 1
            

           
            if dect_s2[s2[j]] == 1:
                del dect_s2[s2[j]]
            else:
                dect_s2[s2[j]] -= 1

        return False
           