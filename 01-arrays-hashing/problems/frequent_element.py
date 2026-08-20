# Given an array and an integer k, return the k most frequent elements

"""
count frequency of each element 
sort elements by frequency, descebding
return top k
""" 
#------------------------------------BRUTE FORCE----------------------------------------------
def top_k_frequent(nums, k):
    counts = {}
    for n in nums:
        counts[n] = counts.get(n, 0) + 1
    sorted_items = sorted(counts.items(), key=lambda x: x[1], reverse=True)
    return [item[0] for item in sorted_items[:k]]
# time O(n log n)

#-------------------------------------OPTIMIZED (bucket sort by frequency)-------------------------------
def top_k_frequent(nums, k):
    counts = {}
    for n in nums:
        counts[n] = counts.get(n, 0) + 1
    buckets = [[] for _ in range(len(nums) + 1)]
    for n, c in counts.item():
        buckets[c].append(n)

    result = []
    for freq in range(len(buckets) - 1, 0, -1):
        for n in buckets[freq]:
            result.append(n)
            if len(result) == k:
                return result
    return result 
# time O(n) counting is linear, and frequency can never exceed n

"""


"""