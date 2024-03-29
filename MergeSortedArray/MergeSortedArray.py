class Solution(object):
    def merge(nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        while n > 0 and m > 0:
            if nums1[m-1] < nums2[n-1]:
                nums1[m+n-1] = nums2[n-1]
                n-=1
            else:
                 nums1[m+n-1] = nums1[m-1]
                 m-=1
        print(nums1)
        
    merge([1,2,3,0,0,0], 3, [2,5,6], 3)
    merge([1], 1,[], 0)
    merge([0], 0, [1],1)
    merge([1,5,6,0,0,0,0], 3, [2,5,6,8], 4)

