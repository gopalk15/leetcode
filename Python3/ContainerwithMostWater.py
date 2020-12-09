from typing import List

'''
Container with the Most Water
Given n non-negative integers a1, a2, ..., an , where each represents a point
at coordinate (i, ai). n vertical lines are drawn such that the two endpoints
of the line i is at (i, ai) and (i, 0). Find two lines, which, together with the
 x-axis forms a container, such that the container contains the most water.

Notice that you may not slant the container.

'''

class Solution:
    def maxArea(self,height:List[int]) -> int:
        l:int = 0; # left pointer
        r:int = (len(height) - 1); #Right pointer
        max_area:int = 0;


        while l < r:
            if height[l] <= height [r]:
                length:int = height[l];
            else:
                length:int = height[r];

            area:int = length*(r-l);
            if area > max_area:
                max_area = area;

            if height[l] <= height[r]:
                l+=1;
            else:
                r -= 1;

        return max_area


if __name__ == '__main__':
    height:List[int] = [1,8,6,2,5,4,8,3,7]
    test = Solution()

    result:int = test.maxArea(height)

    print(result)
