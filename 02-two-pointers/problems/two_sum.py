# Given a sorted array and a target, return the 1-indexed positions of 
# the two numbers that add up to the target.

"""
With the hash map version, we didn't need the array sorted 
we just remembered every number we'd seen. Here, because it's sorted, 
we get something better for free: if you take the smallest and largest 
numbers in the array and their sum is too big, we know for certain the 
largest number can never be part of any valid pair (pairing it with anything 
else only makes the sum bigger, not smaller) so you can rule it out completely 
and move the right pointer inward. Symmetrically, if the sum is too small, 
the smallest number is ruled out, so move the left pointer inward. This is 
the "certainty" from the intro made concrete: sortedness tells you exactly 
which pointer is safe to move.
"""

# -----------------------------------BRUTE FORCE------------------------------------------------
def two_sum_sorted(numbers, target):
    for i in range (len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] + numbers[j] == target:
                return [i + 1, j + 1] # problem is it wants 1 indexed position
# because of the two loops Time O(n^2) and space O(1)

#------------------------------OPTIMIZED (two pointers)------------------------------------------------

def two_sum_sorted(numbers, target):
    left, right = 0, len(numbers) - 1

    while left < right:
        current_sum = numbers[left] + numbers[right]

        if current_sum == target:
            return [left + 1, right + 1]
        elif current_sum < target:
            left += 1
        else:
            right -= 1
    return []

# time is O(n) one pass, pointers only move inside. Space O(1)

