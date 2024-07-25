nums = [3,2,2,3]

def Removal(val):
    if len(nums) !=0:   
        while val in nums:
            nums.remove(val)

