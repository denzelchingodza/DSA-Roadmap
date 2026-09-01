# Given an array of daily prices, find the max profit from buying on one day and 
# selling on a later day. (If no profit is possible, return 0.)

# --------------------------------BRUTE FORCE-----------------------------------------------------
def max_profit(prices):
    best = 0
    for buy in range(len(prices)):
        for sell in range(buy + 1, len(prices)):
            profit = prices[sell] - prices[buy]
            best = max(best, profit)
    return best 
# Time O(n^2) every buy and sell pair checked. Space O(1)

#---------------------------------OPTIMIZED (sliding window)--------------------------------------------------
def max_profit(prices):
    min_price_so_far = prices[0] #assume you bought on day 0, as a starting point
    best_profit = 0

    for price in prices[1:]: #Loop through every day after the first one (since day 0 was used as a starting buy price)
        profit_if_sold_today = price - min_price_so_far
        best_profit = max(best_profit, profit_if_sold_today)

        min_price_so_far = min(min_price_so_far, price)
    return best_profit


"""
imagine prices is a list of a stocks price each day 
[7, 1, 5, 3, 6, 4]
You can only buy once and sell once, and you must buy before you sell. You need to pick 
the best day to buy and best sell day to maximize profit.

As you walk through the days you keep track of 'the lowest price you've seen so far' (which is the 
best day you could have bought, up to this point), 
you also look at best profit you could've made so far if you had sold on any day up to now

So for each new day, you ask 'if i sold today, using the lowest price i have seen so far
as my buy price, how much profit would that be?' Then you check if that beats your best profit thus far

prices = [7, 1, 5, 3, 6, 4]

Start: min_price_so_far = 7, best_profit = 0.

Day 1: profit if sold = 1 - 7 = -6 → best_profit stays 0. New min = min(7, 1) = 1.

Day 5: profit if sold = 5 - 1 = 4 → best_profit = 4. Min stays 1.

Day 3: profit if sold = 3 - 1 = 2 → best_profit stays 4. Min stays 1.

Day 6: profit if sold = 6 - 1 = 5 → best_profit = 5. Min stays 1.

Day 4: profit if sold = 4 - 1 = 3 → best_profit stays 5.

Final answer: 5 (buy at 1, sell at 6). 
"""
# Time O(n) space O(1)
