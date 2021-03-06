'''
Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). 
n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines,
which together with x-axis forms a container, such that the container contains the most water.

Note: You may not slant the container and n is at least 2.

The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of
water (blue section) the container can contain is 49.

Example:

Input: [1,8,6,2,5,4,8,3,7]
Output: 49

'''
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        max_area = 0
        l = 0
        r = len(height)-1
        while l<r:
        	max_area = max(max_area, min(height[l],height[r])*(r-l))
        	if height[l]<height[r]:
        		l += 1
        	else:
        		r -= 1

        return max_area

a = Solution()
print(a.maxArea([1,8,6,2,5,4,8,3,7]))


'''
Time complexity - O(n)
50 / 50 test cases passed.
Status: Accepted
Runtime: 108 ms
Memory Usage: 14.1 MB
'''

