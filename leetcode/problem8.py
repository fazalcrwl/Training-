class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        

        if len(nums)==0:
                return 0

        elif target in nums:
                idx=nums.index(target)
                return idx

        elif target <nums[-1]:
            for i in range(len(nums)):
                if target<nums[i]:
                    x=i                    
                
                    return x
        else:
                return len(nums)