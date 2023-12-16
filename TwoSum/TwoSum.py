class Solution(object):
    def twoSum(nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # brute force solution
        found = False
        # optional sorting of the array to speed up
        nums.sort()
        # cycle through every num
        for i in nums:
            for j in range(len(nums)-1):
                # if sum with the one following == target, than that's the answer
                if i + nums[j+1] == target:
                    print(nums.index(i), j+1)
                    found = True
                break
            if found:
                break

        # hashmap solution
        m = {}

        for i in range(len(nums)):
            # difference from actual number with target
            d = target - nums[i]
            # if it's inside the map, that's the answer
            if nums[i] in m:
                print('[{i1},{i2}]'.format(i1=m[nums[i]], i2=i))
                break
            else:
                # i insert the difference and the index in my map (Ex: {7: 0}, where 7 is the difference and 0 the index of the number
                # that subtracted from the target gives that difference)
                m[d] = i


    twoSum([2,7,11,15], 9)
    twoSum([3,2,4], 6)
    twoSum([3,3], 6)