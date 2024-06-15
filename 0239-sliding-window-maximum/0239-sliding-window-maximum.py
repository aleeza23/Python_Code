class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        window_max = 0
        result_array = []

        for i in range(len(nums) - k + 1):           

            if k <= len(nums):
                window = nums[i : k + i]
                window_max = max(window)
                result_array.append(window_max)


        return result_array        