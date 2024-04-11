class Solution(object):
    def canJump(self, nums):
            destination = len(nums) - 1 
            max_jump= 0
            for i in range(len(nums)):
                if i > max_jump:
                    return False
                max_jump = max(max_jump, i + nums[i])
                if max_jump >= destination:
                    return True