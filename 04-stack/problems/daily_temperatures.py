"""
Monotonic Stack

a monotonic stack is a stack that's kept in sorted order 
(increasing or decreasing) as an invariant whenever a new element would break that 
order, you pop everything that's now "wrong" before pushing. It's still just a stack; 
the only new idea is why you'd pop things that haven't been "resolved" yet in the matching 
sense from before here, popping means "this element can no longer be the answer for 
anything after it, because something better just showed up."
"""


# Given a list of daily temperatures, for each day return how many days you'd have to wait 
# until a warmer temperature. If there's no future warmer day, put 0.

def daily_temperatures(temperatures):
    n = len(temperatures)
    answer = [0] * n
    stack = []

    for today in range(n):
        while stack and temperatures[today] > temperatures[stack[-1]]:
            cold_day = stack.pop()
            answer[cold_day] = today - cold_day
        stack.append(today)

    return answer 

"""
Trace it: temperatures = [73, 74, 75, 71, 69, 72, 76, 73]

today=0 (73): stack empty, push. stack=[0]

today=1 (74): 74 > temperatures[0]=73 → pop 0, answer[0] = 1 - 0 = 1. Stack now empty, push 1. stack=[1]

today=2 (75): 75 > temperatures[1]=74 → pop 1, answer[1] = 2 - 1 = 1. Push 2. stack=[2]

today=3 (71): 71 > temperatures[2]=75? No. Push anyway (71 is now waiting). stack=[2,3]

today=4 (69): 69 > temperatures[3]=71? No. Push. stack=[2,3,4]

today=5 (72): 72 > temperatures[4]=69? Yes → pop 4, answer[4]=5-4=1. 72 > temperatures[3]=71? Yes → pop 3, answer[3]=5-3=2. 72 > temperatures[2]=75? No, stop popping. Push 5. stack=[2,5]

today=6 (76): 76 > temperatures[5]=72? Yes → pop 5, answer[5]=6-5=1. 76 > temperatures[2]=75? Yes → pop 2, answer[2]=6-2=4. Stack empty, push 6. stack=[6]

today=7 (73): 73 > temperatures[6]=76? No. Push. stack=[6,7]

End: indices 6 and 7 never resolved → stay 0.

Final answer = [1, 1, 4, 2, 1, 1, 0, 0] — matches the known correct answer for this classic example.
"""