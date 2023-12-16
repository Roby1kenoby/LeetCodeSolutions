class Solution(object):
    def twoSum(nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        found = False
        for i in nums:
            for j in range(len(nums)-1):
                if i + nums[j+1] == target:
                    print(nums.index(i), j+1)
                    found = True
                break
            if found:
                break

        
    twoSum([2,7,11,15], 9)
    twoSum([3,2,4], 6)
    twoSum([3,3], 6)