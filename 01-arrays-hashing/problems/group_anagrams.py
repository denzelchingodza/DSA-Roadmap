# Given an array of strings, group the ones that are anagrams of each other.

# you are given a list of strings. You need to bucket them into like groups
# where every string in a group is an anagram of every other string in that group
# same letters just rearranged

"""
for each string:
    compute a canonical key (like sorted letters)
    append string to groups[key]
return list(groups.values())
"""

#---------------------------------BRUTE FORCE--------------------------------------------
def group_anagrams(strs):
    groups = []
    used = [False] * len(strs)
    for i in range(len(strs)):
        if used[i]: 
            continue
        group = [strs[i]]
        used[i] = True
        for j in range(i + 1, len(strs)):
            if not used[j] and sorted(strs[i]) == sorted(strs[j]):
                group.append(strs[j])
                used[j] = True
        groups.append(group)
    return groups 

# time O(n^2 x k log k) where k is average string length for every string
"""
Idea: for each string not yet used, start a new group, then scan every 
remaining string to see if it's an anagram (by sorting both and comparing), 
marking matches as used so you don't reprocess them.

	•	used = [False, False, False, False]

i=0, strs[0]="eat"

	•	Not used. Start group = ["eat"], mark used[0]=True.
	•	Inner loop checks j=1,2,3:
	•	j=1, "tea": not used, sorted("eat")=['a','e','t'], sorted("tea")=['a','e','t'] → match! group=["eat","tea"], used[1]=True
	•	j=2, "tan": not used, sorted("tan")=['a','n','t'] ≠ ['a','e','t'] → no match
	•	j=3, "ate": not used, sorted("ate")=['a','e','t'] → match! group=["eat","tea","ate"], used[3]=True
	•	groups = [["eat","tea","ate"]]

i=1 → used[1]=True, skip.

i=2, strs[2]="tan"

	•	Not used. Start group=["tan"], mark used[2]=True.
	•	j=3: already used, skip.
	•	groups = [["eat","tea","ate"], ["tan"]]

i=3 → used[3]=True, skip.

Final: [["eat","tea","ate"], ["tan"]]

Why it's slow: for every unused string, you re-scan the rest of the array 
and re-sort strings you may have already sorted before. That's the nested 
loop → O(n²) comparisons, each comparison paying O(k log k) to 
sort — hence O(n² · k log k).

"""
#------------------------------------------OPTIMIZED (hash by canonical key)--------------------------------

def group_anagrams(strs):
    groups = {}
    for s in strs:
        key = ''.join(sorted(s))
        groups.setdefault(key, []).append(s)
    return list(groups.values())
"""
strs = ["eat", "tea", "tan", "ate"]
it deals with keys basically. We start with 
groups = {} and empty dictionary 

s = "eat"
key = ''.join(sorted(eat)) = "aet"
groups.setdefault("aet", []).append("eat")

groups = {"aet": ["eat"]}

s = "tea"
key = "aet" (same sorted letters)
groups.setdeafult("aet", []) the key already exists so its just appended 
groups = {"aet": ["eat", "tea"]}

s = "tan"
key = ''.join(sorted(tan)) = "ant"
new key groups = {"aet": ["eat", "tea"], "ant": ["tan"]}

s = "ate"
key = "aet"
existing key so we just append
groups = {"aet": ["eat", "tea", "ate"], "ant": ["tan"]}

return list(groups.values())
{["eat", "tea", "ate"], ["tan"]}

"""

# time O(n x k log k) sort each string onve, n strings total. 