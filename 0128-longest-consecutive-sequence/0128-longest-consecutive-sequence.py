class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
       
        length = 0        
        unique_nums = set(nums)        
      
        for n in nums:
            if (n -1) not in unique_nums:
                count = 0
                while (n + count) in unique_nums:
                    count += 1
                length = max(length, count)                
                
        return length        