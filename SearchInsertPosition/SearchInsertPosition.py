class Solution(object):
    def searchInsert(nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        maxN = max(nums)
        minN = min(nums)
        if target > maxN:
            print(str(len(nums)+1))
        elif target < minN:
            print(str(0))
        else:
            if nums[len(nums)//2] == target:
                print(str(len(nums)//2))
                

    searchInsert([1,3,5,6], 5)
    searchInsert([1,3,5,6], 2)
    searchInsert([1,3,5,6], 7)