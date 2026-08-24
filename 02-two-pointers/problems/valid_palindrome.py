# Given a string, return True if it reads the same forwards and backwards, 
# ignoring case and non-alphanumeric characters (spaces, punctuation).

#-----------------------------------BRUTE FORCE-------------------------------------
def is_palindrome(s):
    cleaned = [ch.lower() for ch in s if ch.isalnum()]
    return cleaned == cleaned[::-1]
# time O(n) to clean and O(n) to reverse. Space O(n)

#------------------------------------OPTIMIZED (two pointers)----------------------------------
def is_palindrome(s):
    left, right = 0, len(s) - 1 #start at both ends of the string

    while left < right:
        while left < right and not s[left].isalnum():
            left += 1
        while left < right and not s[right].isalnum():
            right -= 1

        if s[left].lower() != s[right].lower():
            return False 
        left += 1
        right -= 1
    return True 
# time is O(n)


# Brute force does fix the time proble as much as the optimized solution does 
# but it does that by paying the memory. 