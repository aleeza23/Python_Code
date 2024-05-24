class Solution:
    def trap(self, height: List[int]) -> int:

        left_p = 0
        right_p = len(height) - 1
        left_max = height[left_p]
        right_max = height[right_p]
        units = 0

        while left_p < right_p:
            if left_max < right_max:
                left_p += 1
                left_max = max(left_max, height[left_p])
                units += left_max - height[left_p]
            else:
                right_p -= 1
                right_max = max(right_max, height[right_p])
                units += right_max - height[right_p]
        return units     



