# Given an array nums and a target, return the indices of the two numbers that add up to the target

# for each pair of elements (i, j) where i < j:
#     if nums[i] + nums[j] == target: return (i, j)

# example lets say nums = [1, 8, 7, 12, 5, 9]  target 13
#----------------------------------------BRUTE FORCE-------------------------------------------
def two_sum(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
# time complexity is O(n^2). Space O(1)

#------------------------------OPTIMIZED SOLUTION-------------------------------------------------
def two_sum(nums, target):
    seen = {}
    for i, n in enumerate(nums):
        compliment = target - n 
        if compliment in seen:
            return [seen[compliment], i]
        seen[n] = i
# time is O(n) one pass and space O(n)

"""
instead of checking every pair (which means looping twice) you loop once and ask 'have i already seen the nymber
that would part with this one?'

example:
nums = [3, 5, 2, 8], target = 7 
start: seen = {} empty dictionary 
- i = 0, n = 3
- compliment = 7 - 3 = 4
- is 4 in seen? seen is empty so no
seen = {3:0}

- i = 1, n = 5
- compliment = 7 - 5 = 2
- is 2 in seen? no so we update 
seen = {3:0, 5:1}

- i = 2, n = 2
compliment = 7 - 2 = 5 
- is 5 in seen? Yes seen = {3:0, 5:1} has got 5 mapped at index 1 
- return [seen[5], i] [1,2]


"""