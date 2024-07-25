def Dupliacte(nums):
    if not nums:
        return 0

            # Convert to set to remove duplicates and then back to list
    nums_list = sorted(list(set(nums)))

            # Place the sorted unique elements back into the original list
    for i in range(len(nums_list)):
        nums[i] = nums_list[i]

    return len(nums_list)