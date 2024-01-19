class Solution(object):
    def searchInsert(nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        mn = 0
        mx = len(nums) - 1
        
        while mn <= mx:
            mid = (mn + mx) // 2
            if nums[mid] == target:
                mn = mid
                break
            elif target < nums[mid]:
                mx = mid-1
            elif target > nums[mid]:
                mn = mid+1
        
        print('position: ', mn)
            
    searchInsert([1,3,5,6], 5)
    searchInsert([1,3,5,6], 2)
    searchInsert([1,3,4,5,6], 4)