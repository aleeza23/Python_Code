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
        hashmap = {}
        ans = []

        for i in range(len(nums) -1):
            hashmap[(i, i + 1)] = nums[i] + nums[i + 1]
            if hashmap[(i, i+1)] == target:
                ans.append(i)
                ans.append(i + 1)
        return ans         

               

        