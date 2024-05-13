class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        hashmap_s = collections.defaultdict(int)
      
        if len(s) != len(t):
            return False

        for c in s:
            hashmap_s[c] += 1

        # check if t char present in hashmap_s
        for char in t:
            if hashmap_s[char] == 0:
                return False
                
            hashmap_s[char] -= 1

        return True
