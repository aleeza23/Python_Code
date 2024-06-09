class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        substring_set = set()
        longest = 0

        for right in range(len(s)):
            while s[right] in substring_set:
                substring_set.remove(s[left])
                left += 1
            substring_set.add(s[right])
            longest = max(longest, right - left + 1)
        return longest
