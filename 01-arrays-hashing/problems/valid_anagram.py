# Given two strings s and t, return True if t is an anagram of s (this is basically same letters, same counts)

# for two strings to be anagrams they have to have the same length and when sorted they have to be the same word 
# example s = eat, t = tea. So length of both is 3 and when sorted they both are (aet)

# if len(s) != len(t) : return False
# sort s, sort t
# return sorted_s == sorted_t

#---------------------------------BRUTE FORCE----------------------------------------------------------------------
def is_anagram(s, t):
    if len(s) != len(t):
        return False 
    return sorted(s) == sorted(t)
# time O(n log n), and space O(n) for sorted copies 

# -----------------------------------OPTIMIZED SOLUTION--------------------------------------------------------------
def is_anagram(s, t):
    if len(s) != len(t):
        return False # # Different lengths can never be anagrams of 
    # each other cheap check we do first so we don't waste time otherwise
    counts = {}
    for ch in s:
        counts[ch] = counts.get(ch, 0) + 1
    for ch in t:
        if ch not in counts or counts[ch] == 0:
            return False
        counts[ch] -= 1
    return True 
#time O(n) two linear passes. Space O(1) in practice 


"""
s = "listen", t = "silent"
- len(s) = len(t) = 6

- counts = {} to start 
- counts.get(ch, 0) + 1 means: lookup each ch in the dict, if its not there yet
treat it as 0 then add 1. 
'listen'
l counts = {'l' : 1}
i counts = {'l' : 1, 'i' : 1}
s counts = {'l' : 1, 'i': 1, 's': 1}
t counts = {'l' : 1, 'i': 1, 's': 1, 't' : 1}
e counts = {'l' : 1, 'i': 1, 's': 1, 't' : 1, 'e' : 1}
n counts = {'l' : 1, 'i': 1, 's': 1, 't' : 1, 'e' : 1, 'n' : 1}

final counts = {'l' : 1, 'i': 1, 's': 1, 't' : 1, 'e' : 1, 'n' : 1} every letter appears once 

now for the second for each letter in 'silent' 
checks is it in counts and is its count still above 0?
 s in counts, count = 1, decrement counts['s'] = 0
 do the same for all else letters
no letter was ever missing or already at 0 when we needed it 
so we return 

"""