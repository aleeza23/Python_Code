class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # brute force approach O(n^2) TC
        # ans = []
        # for i in range(len(nums)):
        #     for j in range((i + 1), len(nums)):
        #         if (nums[i] + nums[j]) == target:
        #             ans.append(i)
        #             ans.append(j)
                    
        # return ans



        # another approach
        hashmap= {}

        for i in range(len(nums)):
            target_diff = target - nums[i]

            if target_diff not in hashmap:
                hashmap[nums[i]] = i
            else:
                return [hashmap[target_diff], i]   
              
           

        

               

        