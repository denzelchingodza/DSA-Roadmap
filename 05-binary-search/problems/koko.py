# Given piles of bananas and h hours to eat them all, where Koko chooses
# one fixed bananas-per-hour eating speed for the entire time
# (and moves to the next pile once she finishes the current one, even mid-hour),
# return the minimum integer eating speed that lets her finish all the piles
# within h hours.

import math

def min_eating_speed(piles, h):
    left, right = 1, max(piles)
    best = right

    while left <= right:
        speed = (left + right) // 2

        hours_needed = sum(math.ceil(pile / speed) for pile in piles)

        if hours_needed <= h:
            best = speed
            right = speed - 1
        else:
            left = speed + 1
    return best

"""
THE PICTURE: this is different from every other file in this topic --
there's no array being index-searched here. piles never gets looked up by
position. Instead the search space is the number line of possible eating
SPEEDS, from 1 up to the biggest pile. The property that makes this
searchable: if some speed S is fast enough to finish in time, every speed
FASTER than S is obviously also fast enough. That "once true, stays true"
relationship is what a normal sorted array gives you for free -- here it
comes from the problem itself, not from the data being in order.

BUG I HAD, AND WHY IT WAS WORSE THAN A WRONG-ANSWER BUG:
the "too slow" branch originally said "left = speed - 1" -- it needed to
be "left = speed + 1". If the current speed can't finish in time, the ONLY
direction that could possibly fix it is a FASTER speed, so left has to
move forward, past the speed just tried. Moving it backward instead means
the search can try the exact same speed again next time, get the exact
same "still too slow" result, and move left backward again -- the two
boundaries never converge, and the function hangs forever instead of
just giving a wrong answer.

Concrete case that used to hang: piles=[3,6,7,11], h=8
...eventually reaches left=2, right=5 -> speed=(2+5)//2=3 -> too slow.
With the OLD bug: left = speed-1 = 2 (unchanged!) -> next loop: mid is
STILL (2+5)//2=3 -> too slow again -> left stuck at 2 forever. Infinite
loop, never returns.

TRACE IT WITH THE FIX: piles=[3,6,7,11], h=8

left=1, right=11 -> speed=6.
hours = ceil(3/6)+ceil(6/6)+ceil(7/6)+ceil(11/6) = 1+1+2+2 = 6
6 <= 8 -> works -> best=6, try slower -> right=5

left=1, right=5 -> speed=3.
hours = 1+2+3+4 = 10
10 > 8 -> too slow -> move left FORWARD, past this speed -> left=4

left=4, right=5 -> speed=4.
hours = 1+2+2+3 = 8
8 <= 8 -> works -> best=4 -> right=3

left=4, right=3 -> boundaries crossed, loop ends. Final answer: best=4.
Correctly converges this time, instead of hanging.
"""
