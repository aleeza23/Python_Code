class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

     
        count = 1
        length = 0
        
        unique_nums = sorted(set(nums))
      
        for i in range(len(unique_nums) -1):
                       
            if unique_nums[i]+1 == unique_nums[i+1]:
                count +=1

            else:                
                length = max(length,count)               
                count = 1
             
        return max(length, count)
        