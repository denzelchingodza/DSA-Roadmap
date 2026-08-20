# Given an array nums, return an array where output[i] is the product of 
# all elements except nums[i] without using division, in O(n).
"""
for each i:
    output[i] = product of all elements to the left of i x 
    all elements to the right of i
"""
#---------------------------BRUTE FORCE------------------------------------------------
def product_except_self(nums):
    n = len(nums)
    result = []
    for i in range(n):
        product = 1
        for j in range(n):
            if i != j:
                product *= nums[j]
        result.append(product)
    return result
# Time O(n^2)

#--------------------------------OPTIMIZED (prefix * suffix products)--------------------------------
def product_except_self(nums):
    n = len(nums)
    result = [1] * n
    prefix = 1
    for i in range(n):
        result[i] = prefix
        prefix *= nums[i]

    suffix = 1
    for i in range(n - 1, -1, -1):
        result[i] *= suffix
        suffix *= nums[i]
    return result 
# Time is O(n) two linear passes 

"""
????
"""

