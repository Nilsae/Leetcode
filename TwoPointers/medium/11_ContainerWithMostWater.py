class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n = len(height)
        left, right = 0, n - 1
        max_vol = 0

        while left < right:
            # Calculate the area
            width = right - left
            max_vol = max(max_vol, min(height[left], height[right]) * width)

            # Move the pointer of the shorter height inward
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_vol

print(Solution().maxArea(height = [1,8,6,2,5,4,8,3,7]))
print(Solution().maxArea(height = [4,3,2,1,4]))
