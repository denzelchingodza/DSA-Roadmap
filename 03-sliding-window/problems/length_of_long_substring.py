# Given a string, find the length of the longest substring with no repeated characters

#---------------------------------------BRUTE FORCE----------------------------------------
def length_of_longest_substring(s):
    best = 0
    for i in range(len(s)):
        seen = set()
        for j in range(i, len(s)):
            if s[j] in seen:
                break 
            seen.add(s[j])
            best = max(best, j - i + 1)
    return best 

# Time complexity is O(n^2)

#--------------------------------OPTIMIZZED (sliding window)-----------------------------------
def length_of_longest_substring(s):
    window = set() # characters currently in the window 
    left, best = 0, 0
    for right in range(len(s)):
        #if the incoming character is already in the window, keep
        #shrinking from the left, removing characters and advancing left
        #until the duplicate is gone
        while s[right] in window:
            window.remove(s[left])
            left += 1

        # now add characters to the right
        window.add(s[right])

        best = max(best, right - left + 1)
    return best

# time is O(n) moves forward n times total. 

"""
s = 'abcabcbb'

right = 0 'a': not in window, add it window = {a}. best = 1
right = 1 'b': not in window, add it window = {a, b}. best = 2
right = 2 'c': not in window, add it window = {a, b, c}. best = 3
right = 3 'a': already in window, shrink:remove s[left]='a', left=1. 
Now 'a' is gone from window, loop stops. Add 'a' back in. window = {b,c,a}. 
Window is now [1,3] = "bca", width 3. best stays 3.
right = 4 'b': already in window → shrink: remove s[left]='b', left=2. 
Add 'b'. window = {c,a,b}, window [2,4] = "cab", width 3.
this continues, window sliding along, best never exceeding 3 for this string. 
Final answer: 3 ("abc")

"""