class Solution(object):
    def mySqrt(x):
        """
        :type x: int
        :rtype: int
        """
        mn = 0
        mx = x

        while mn <= mx:
            mid = (mn + mx) // 2
            if mid * mid > x:
                mx = mid - 1
            elif mid * mid < x:
                mn = mid + 1
            else:
                print(mid)
                return
        print(mx)


    mySqrt(4)
    mySqrt(8)
    mySqrt(144)