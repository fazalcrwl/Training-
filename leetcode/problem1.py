
"""
Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]


"""







def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        temp=[]

        for i in range(len(nums)):
    
            if(i!=len(nums)):
                for j in range(i+1,len(nums)):
                    if nums[i]+nums[j]==target:
                        if i  not in temp:
                            temp.append(i) 
                        if j not in temp:
                            temp.append(j)
        return temp 