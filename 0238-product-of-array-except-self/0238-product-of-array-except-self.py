class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        ans_array = [1] * len(nums)
        prefix_product = 1
        suffix_product = 1

        for i in range(len(nums)):
            ans_array[i] = prefix_product
            prefix_product *= nums[i]


        for i in reversed(range(len(nums))):
            ans_array[i] *= suffix_product 
            suffix_product *= nums[i]
            
        return ans_array  
     
