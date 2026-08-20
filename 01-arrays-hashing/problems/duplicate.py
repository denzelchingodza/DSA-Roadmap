#Given an integer array, return True if any value appears at least twice 

#for each pair of elements (i, j) where i < j:
#    if arr[i] == arr[j]: return True
# return False 

#---------------------------------BRUTE FORCE----------------------------------------------------------

def contains_duplicate(nums):
    for i in range(len(nums)):  
        for j in range(i + 1, len(nums)): 
            if nums[i] == nums[j]: 
                return True 
    return False 
#Time O(n^2), its a loop within a loop. Space O(1).
#------------------------------------OPTIMIZED--------------------------------

def contains_duplicate(nums):
    seen = set()
    for n in nums:
        if n in seen:
            return True 
        seen.add(n)
    return False 
#Time O(n) this is a one pass. Space O(n). The set can hold up to n elements 


#The Difference 
# the brute force re scans the whole array for every 
# element to ask "have I seen this before?" that repeated scanning 
# is the O(n²). A hash set answers "have I seen this before?" 
# in O(1), so the inner loop disappears entirely and collapses 
# into one linear pass. This trade O(n) extra memory to kill an 
# inner loop is the single most common move in this whole topic.