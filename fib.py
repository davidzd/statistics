def removeDuplicates(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    result_list = []
    print nums
    if nums:
        i = 0
        while i < len(nums):
            if i == 0:
                result_list.append(nums[i])
            elif nums[i] != result_list[-1]:
                result_list.append(nums[i])
            i+=1
    print result_list

removeDuplicates([1,2,3,4,4])