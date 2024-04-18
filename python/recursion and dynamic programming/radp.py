# Write a function to find the length of the longest common subsequence between two
# sequences, e.g. Given the strings serendipitous and precipitation, the longest common
# subsequence is reipito and its length is 7

# a sequence is a group of items wiih a deterministic ordering. Lists, tuples and
# ranges are some common sequence types in python.
# A subsequence is a sequence obtained by deleting zero or more elements from another
# sequence. For example, edpt is a subsequence of serendipitous
from jovian.pythondsa import evaluate_test_cases, evaluate_test_case


def lcs_recursive(seq1, seq2, idx1=0, idx2=0):
    if idx1 == len(seq1) or idx2 == len(seq2):
        return 0
    elif seq1[idx1] == seq2[idx2]:
        return 1 + lcs_recursive(seq1, seq2, idx1+1, idx2+1)
    else:
        option1 = lcs_recursive(seq1, seq2, idx1+1, idx2)
        option2 = lcs_recursive(seq1, seq2, idx1, idx2+1)
        return max(option1, option2)


def lcs_memo(seq1, seq2):
    memo = {}

    def recurse(idx1=0, idx2=0):
        key = (idx1, idx2)
        if key in memo:
            return memo[key]
        elif idx1 == len(seq1) or idx2 == len(seq2):
            memo[key] = 0
        elif seq1[idx1] == seq2[idx2]:
            memo[key] = 1 + recurse(idx1 + 1, idx2 + 1)
        else:
            memo[key] = max(recurse(idx1+1, idx2), recurse(idx1, idx2+1))
        return memo[key]
    return recurse(0, 0)


def lcs_dp(seq1, seq2):
    n1, n2 = len(seq1), len(seq2)
    table = [[0 for x in range(n2+1)] for x in range(n1+1)]
    for i in range(n1):
        for j in range(n2):
            if seq1[i] == seq2[j]:
                table[i+1][j+1] = 1 + table[i][j]
            else:
                table[i+1][j+1] = max(table[i][j+1], table[i+1][j])
    return table[-1][-1]


T0 = {'input': {'seq1': 'serendipitous', 'seq2': 'precipitation'}, 'output': 7}
T1 = {'input': {'seq1': [1, 3, 5, 6, 7, 2, 5, 2, 3],'seq2': [6, 2, 4, 7, 1, 5, 6, 2, 3]}, 'output': 5}
T2 = {'input': {'seq1': 'longest', 'seq2': 'stone'}, 'output': 3}
T3 = {'input': {'seq1': 'asdfwevad', 'seq2': 'opkpoiklklj' }, 'output': 0}
T4 = {'input': {'seq1': 'dense', 'seq2': 'condensed'}, 'output': 5}
T5 = {'input': {'seq1': '', 'seq2': 'opkpoiklklj'}, 'output': 0}
T6 = {'input': {'seq1': '', 'seq2': ''}, 'output': 0}
T7 = {'input': {'seq1': 'abcdef', 'seq2': 'badcfe'}, 'output': 3}

lcq_tests = [T0, T1, T2, T3, T4, T5, T6, T7]


print(evaluate_test_cases(lcs_dp, lcq_tests))






















