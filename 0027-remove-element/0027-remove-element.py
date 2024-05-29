class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        fast_p = 0
        slow_p = 0

        while fast_p < len(nums):
            if nums[fast_p] != val:
                nums[slow_p] = nums[fast_p]
                slow_p += 1
            fast_p += 1
        return slow_p