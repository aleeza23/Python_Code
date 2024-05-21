class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        left_p = 0
        right_p = len(numbers) - 1

        while left_p < right_p:
            sum = numbers[left_p] + numbers[right_p]

            if sum == target:
                return [left_p + 1, right_p + 1]
            elif sum > target:
                right_p -= 1
            else:
                left  += 1         







        