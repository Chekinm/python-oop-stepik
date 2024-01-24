def pi_function(s):
    """pi_funciton count"""
    pi = [0] * len(s)
    j = 0
    for i in range(1, len(s)):
        while j != 0 and s[j] != s[i]:
            j = pi[j - 1]
        if s[j] == s[i]:
            j += 1
        pi[i] = j
    return pi