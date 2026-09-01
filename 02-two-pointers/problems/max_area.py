# Given an array height where height[i] is the height of a 
# vertical line at position i, find two lines that, 
# together with the x-axis, form a container holding the most water. 
# Return the max water it can hold.

"""
Picture a bunch of fence posts standing in a row, all different heights.
Now imagine you pick any two of those posts, and you pour water between them. 
The water fills up the gap but here is the catch: water only rises as high as 
the shorter post, because once it hits that height, it just spills over the top 
and runs out.

So two things decide how much water you can hold between two posts:

	1.	How far apart they are (a wider gap = more space for water)
	2.	How tall the shorter one is (that is the limit — the taller post does not 
    help you once water reaches the short one is height)

The question is: out of every possible pair of posts you could pick, which two 
hold the most water?
"""
#----------------------------------------BRUTE FORCE--------------------------------------------
def max_area(height):
    best = 0
    for i in range(len(height)):
        for j in range(i + 1, len(height)):
            width = j - i
            shorter_wall = min(height[i], height[j])
            area = width * shorter_wall
            best = max(best, area)
    return best
# Time O(n^2)

#---------------------------------OPTIMIZED (two pointers)------------------------------------------
def max_area(height):
    left, right = 0, len(height) - 1
    best = 0

    while left < right:
        width = right - left
        shorter_wall = min(height[left], height[right])
        area = width * shorter_wall
        best = max(best, area)

        if height[left] < height[right]:
            left += 1
        else: 
            right -= 1
    return best 

# time is O(n)
