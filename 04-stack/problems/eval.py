# evaluate an arithmetic expression given in Reverse Polish (postfix) 
# notation operators come after their operands, 
# e.g. ["2", "1", "+", "3", "*"] means (2 + 1) * 3 = 9. No parentheses 
# needed in this notation; order is implicit.

def eval_rpn(tokens):
    stack = []

    for token in tokens:
        if token in ('+', '-', '*', '/'):
            right = stack.pop()
            left = stack.pop()

            if token == '+':
                result = left + right
            elif token == '-':
                result = left - right
            elif token == '*':
                result = left * right
            else:
                result = int(left/right)

            stack.append(result)
        else:
            stack.append(int(token))
    return stack[0]

"""
Trace it: tokens = ["2", "1", "+", "3", "*"]

"2" → number, push. stack = [2]

"1" → number, push. stack = [2, 1]

"+" → operator. Pop right=1, pop left=2. result = 2 + 1 = 3. Push. stack = [3]

"3" → number, push. stack = [3, 3]

"*" → operator. Pop right=3, pop left=3. result = 3 * 3 = 9. Push. stack = [9]

Final: stack[0] = 9. ✓ Matches (2+1)*3 = 9
"""