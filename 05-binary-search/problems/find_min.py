# Given a sorted array that has been rotated at some unknown pivot point
# (e.g. [4,5,6,7,0,1,2] was originally [0,1,2,4,5,6,7]), find the minimum
# element. Assume no duplicate values.

def find_min(nums):
    left, right = 0, len(nums) - 1

    while left < right:
        mid = (left + right) // 2

        if nums[mid] > nums[right]:
            left = mid + 1
        else:
            right = mid
    return nums[left]

"""
Note on the loop condition: this one correctly uses "while left < right",
not "<=" -- and for a different reason than ordinary Binary Search. Here,
left and right aren't hunting for a match, they're closing in on EACH
OTHER until they land on the same index. The loop is supposed to stop the
instant they're equal, and the answer is whatever value is sitting there.

THE PICTURE: nums[mid] compared to nums[right] tells you which side is
"broken" by the rotation. If nums[mid] > nums[right], the rotation point
(and therefore the minimum) must be somewhere to the RIGHT of mid, because
a properly sorted stretch would never have a bigger number before a
smaller one. If nums[mid] <= nums[right], the stretch from mid to right is
clean/sorted, so the rotation point is at mid or to its LEFT -- and mid
itself has to stay in play, which is why right gets set to mid, not mid-1.

TRACE IT: nums = [4, 5, 1, 2, 3]

left=0, right=4 -> mid=2, nums[2]=1. Compare to nums[right]=nums[4]=3.
Is 1 > 3? No -> the right side (mid..right) is clean/sorted, so the
rotation point is at mid or to its left -> right = mid = 2

left=0, right=2 -> mid=1, nums[1]=5. Compare to nums[right]=nums[2]=1.
Is 5 > 1? Yes -> rotation point is to the right of mid -> left = mid+1 = 2

left=2, right=2 -> loop stops (they're equal). Return nums[2] = 1.

That 1 is the actual minimum of [4,5,1,2,3] -- correct. (Worth noting: the
function returns nums[left], the VALUE at that index -- not the number of
the index itself.)
"""
