class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = [] 

        for i in range(len(nums)):            
            if i > 0 and nums[i] == nums[i - 1]:
                continue 

            left_p = i + 1
            right_p = len(nums) - 1 


            while left_p < right_p:              

                triplets = nums[i] + nums[left_p] + nums[right_p]

                if triplets == 0:
                    ans.append([nums[i] ,+ nums[left_p] , nums[right_p]]) 

                    while left_p < right_p and nums[left_p] == nums[left_p + 1]:
                        left_p  += 1

                    while left_p < right_p and nums[right_p] == nums[right_p - 1]:
                        right_p -= 1
                    left_p += 1
                    right_p -= 1    

                elif triplets < 0:
                    left_p += 1
                else:
                    right_p -= 1   





           
        return ans              






       

        