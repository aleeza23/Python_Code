class Solution:
    def maxArea(self, height: List[int]) -> int:

        # formula of area
        # area = width * height

        left_p = 0
        right_p = len(height) - 1
        res = 0

        while left_p < right_p:
            area = (right_p - left_p) * min(height[left_p], height[right_p])
            res = max(res, area)

            if height[left_p] < height[right_p]:
                left_p += 1               
            else:
                right_p -= 1              

        return res                 
     