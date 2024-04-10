class Solution(object):
    def twoSum(self, nums, target):
        output = []
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                result = nums[i] + nums[j]
                if result == target:
                    output.append(i)
                    output.append(j)
        return output        
                
