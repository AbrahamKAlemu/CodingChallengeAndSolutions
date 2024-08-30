"""Given n non-negative integers representing an elevation map where the
    width of tach bar is 1, compute how much water it can trap after raining."""

class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        leftHeight, rightHeight = height[l], height[r]
        res = 0
        while l < r:
            if height[l] < height[r]:
                l += 1
                leftHeight = max(height[l], leftHeight)
                res += leftHeight - height[l]
            else:
                r -= 1
                rightHeight = max(height[r], rightHeight)
                res += rightHeight - height[r]
        return res
