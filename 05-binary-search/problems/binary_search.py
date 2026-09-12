# Given a sorted array of integers and a target value, return the index of
# the target if it exists in the array, or -1 if it doesn't.


def binary_search(nums, target):
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = (left + right) // 2 #integer division, always lands on a valid index
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

"""
nums = [1, 3, 5, 7, 9, 11], target = 9
left = 0 right=5 -> mid=2 , nums[2]=5 which is less than the target. left=3
left=3, right=5 --> mid=4, nums[4]=9 which is equal to 9, return 4


BUG I HAD, AND WHY IT MATTERED:
the loop condition was originally "while left < right" instead of
"while left <= right". Picture the search boundaries as two hands closing
in on a shelf of books: "left < right" means "keep going as long as there's
more than one book between my hands." The moment only ONE book is left
(left == right), the hands stop -- but that one remaining book might
actually be the target, and it never gets checked.

Concrete case that broke with the old "<": nums = [1,3,5,7,9,11], target = 11
(the very last element).
left=0,right=5 -> mid=2, 5<11 -> left=3
left=3,right=5 -> mid=4, 9<11 -> left=5
left=5,right=5 -> with the OLD "<", left<right is False, loop quits without
checking index 5 at all -> wrongly returns -1, even though 11 is right there.

With the fixed "<=", left=5,right=5 still runs one more time: mid=5,
nums[5]=11 -> match -> returns 5. Correct.

Lesson: any time left and right can legitimately end up equal and that
position still needs checking, the loop needs "<=", not "<".
"""
