# Given a string of uppercase letters and an integer k, you can replace up 
# to k characters with any other character. Find the length of the longest 
# substring you can make consist of a single repeated character.

def character_replacement(s, k):
    best = 0

    for i in range(len(s)):
        counts = {}
        for j in range(i, len(s)):
            counts[s[j]] = counts.get(s[j], 0) + 1
            window_len = j - i + 1
            most_frequent = max(counts.values())
            chars_to_change = window_len - most_frequent
            if chars_to_change <= k:
                best = max(best, window_len)
            else:
                break
    return best

# time is O(n^2) or worse since max(xounts.values()) itself costs time per step. Space O(1) bounded by 26 letters

#---------------------------------------------OPTIMIZED(sliding window+frequency count)-----------------------------------------------
def character_replacement(s, k):
    counts = {} # frequency of each character currently in the window
    left = 0 
    max_freq = 0  # highest count of any single character seen in any window so far
    best = 0

    for right in range(len(s)):
        counts[s[right]] = counts.get(s[right], 0) + 1
        # Track the best "most frequent character count" seen across any window
        max_freq = max(max_freq, counts[s[right]])

        window_len = right - left + 1
        chars_to_change = window_len - max_freq

        if chars_to_change > k:
            counts[s[left]] -= 1
            left += 1
        best = max(best, right - left + 1)
    return best

# time complexity is O(n). Space O(1)

"""
s = "AABABBA", k = 1

right=0 (A): counts {A:1}, max_freq=1. window_len=1, change=1-1=0 <= 1 ✓. best=1.

right=1 (A): counts {A:2}, max_freq=2. window_len=2, change=2-2=0 ✓. best=2.

right=2 (B): counts {A:2,B:1}, max_freq=2. window_len=3, change=3-2=1 <= 1 ✓. best=3.

right=3 (A): counts {A:3,B:1}, max_freq=3. window_len=4, change=4-3=1 ✓. best=4.

right=4 (B): counts {A:3,B:2}, max_freq=3. window_len=5, change=5-3=2 > 1 ✗ → shrink: remove s[left]='A', counts {A:2,B:2}, left=1. best stays 4



"""  