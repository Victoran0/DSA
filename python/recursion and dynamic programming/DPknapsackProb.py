# Also known as the 01 knapsack problem

# You’re in charge of selecting a football (soccer) team from a large pool of
# players. Each player has a cost, and a rating. You have a limited budget.
# What is the highest total rating of a team that fits within your budget.
# Assume that there’s no minimum or maximum team size.

from jovian.pythondsa import evaluate_test_case, evaluate_test_cases


def max_profit_memo(weights, profits, capacity):
    memo = {}

    def recurse(remaining, idx=0):
        key = (remaining, idx)
        if key in memo:
            return memo[key]
        elif idx == len(weights):
            memo[key] = 0
        elif weights[idx] > remaining:
            memo[key] = recurse(remaining, idx+1)
        else:
            memo[key] = max(recurse(remaining, idx+1), profits[idx] + recurse(remaining-weights[idx], idx+1))
        return memo[key]
    return recurse(capacity, 0)


def max_profit_recursive(weights, profits, capacity, idx=0):
    if idx == len(weights):
        return 0
    elif weights[idx] > capacity:
        return max_profit_recursive(weights, profits, capacity, idx+1)
    else:
        option1 = max_profit_recursive(weights, profits, capacity, idx+1)
        option2 = profits[idx] + max_profit_recursive(weights, profits, capacity-weights[idx], idx+1)
        return max(option1, option2)


def max_profit_dp(weights, profits, capacity):
    n = len(weights)
    table = [[0 for _ in range(capacity+1)]for _ in range(n+1)]
    for i in range(n):
        for c in range(1, capacity+1):
            if weights[i] > c:
                table[i+1][c] = table[i][c]
            else:
                table[i+1][c] = max(table[i][c], profits[i] + table[i][c-weights[i]])
    return table[-1][-1]


test0 = {'input': {'capacity': 165, 'weights': [23, 31, 29, 44, 53, 38, 63, 85, 89, 82], 'profits': [92, 57, 49, 68, 60, 43, 67, 84, 87, 72]}, 'output': 309}
test1 = {'input': {'capacity': 3, 'weights': [4, 5, 6], 'profits': [1, 2, 3]}, 'output': 0}
test2 = {'input': {'capacity': 4, 'weights': [4, 5, 1], 'profits': [1, 2, 3]}, 'output': 3}
test3 = {'input': {'capacity': 170, 'weights': [41, 50, 49, 59, 55, 57, 60], 'profits': [442, 525, 511, 593, 546, 564, 617]}, 'output': 1735}
test4 = {'input': {'capacity': 15, 'weights': [4, 5, 6], 'profits': [1, 2, 3]}, 'output': 6}
test5 = {'input': {'capacity': 15, 'weights': [4, 5, 1, 3, 2, 5], 'profits': [2, 3, 1, 5, 4, 7]}, 'output': 19}
tests = [test0, test1, test2, test3, test4, test5]

print(evaluate_test_cases(max_profit_dp, tests))
































