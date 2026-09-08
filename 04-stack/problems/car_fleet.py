# cars are all driving toward the same destination on a one lane road, 
# each with a starting position and speed (so each has a fixed time it 
# would take to reach the destination alone). A faster car behind a slower 
# one can never pass it just catches up and they merge into one "fleet," 
# from then on traveling at the slower car's speed. Return how many distinct 
# fleets arrive.

def car_fleet(target, position, speed):
    # Pair each car with its position, sort by position DESCENDING 
    # process the car closest to the destination first
    cars = sorted(zip(position, speed), reverse=True)
    stack = []

    for pos, spd in cars:
        arrival_time = (target - pos) / spd

        if not stack or arrival_time > stack[-1]:
            stack.append(arrival_time)
    return len(stack)

"""
Trace it: target = 12, position = [10, 8, 0, 5, 3], speed = [2, 4, 1, 1, 3]

Pair and sort by position descending: (10,2), (8,4), (5,1), (3,3), (0,1)

(10,2): arrival = (12-10)/2 = 1.0. Stack empty → push. stack=[1.0]

(8,4): arrival = (12-8)/4 = 1.0. Is 1.0 > 1.0? No → merges into the fleet ahead (catches up exactly at the destination). Don't push. stack=[1.0]

(5,1): arrival = (12-5)/1 = 7.0. Is 7.0 > 1.0? Yes → slower, new fleet. Push. stack=[1.0, 7.0]

(3,3): arrival = (12-3)/3 = 3.0. Is 3.0 > 7.0? No → merges into the fleet ahead of it (the one at 7.0 — it catches up before reaching the destination). Don't push. stack=[1.0, 7.0]

(0,1): arrival = (12-0)/1 = 12.0. Is 12.0 > 7.0? Yes → slower than everything ahead, new fleet. Push. stack=[1.0, 7.0, 12.0]

Final: len(stack) = 3 fleets. ✓ (matches the known answer for this classic example)
"""