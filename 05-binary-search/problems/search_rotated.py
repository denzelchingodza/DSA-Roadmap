# Given the same kind of rotated sorted array, and a target value, return the
# index of the target if it exists, or -1 if it doesn't.

def search_rotated(nums, target):
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid

        if nums[left] <= nums[mid]:
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1
    return -1

"""
THE PICTURE: at every step, ONE of the two halves around mid is guaranteed
to be a normal, boring, fully sorted stretch -- the rotation "damage" can
only ever be hiding in the OTHER half. The whole trick is: figure out
which half is the clean one, and only trust ordinary "is my target between
these two values" reasoning on that clean half. You never need to know
where the rotation point actually is (that's Find Minimum's job) -- you
only need to know which SIDE is trustworthy this step.

nums[left] <= nums[mid] is the test for "is the LEFT half clean." If
that's true, the rotation break must be sitting somewhere in the right
half instead, which is exactly why the left half can be trusted for a
normal range check.

TRACE IT: nums = [4,5,6,7,0,1,2], target = 0

left=0, right=6 -> mid=3, nums[3]=7. Not target.
nums[0]=4 <= nums[3]=7 -> left half (0..3) is sorted.
Is 4 <= 0 < 7? No -> target's not in the sorted left half
-> left = mid+1 = 4

left=4, right=6 -> mid=5, nums[5]=1. Not target.
nums[4]=0 <= nums[5]=1 -> left half (4..5) is sorted.
Is 0 <= 0 < 1? Yes -> right = mid-1 = 4

left=4, right=4 -> mid=4, nums[4]=0 == target -> return 4.
"""
