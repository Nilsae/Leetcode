# You are given a string s, your task is to implement a function that returns all possible letter case combinations in the string.

# For example, if the input string is s = "a1b2", the output should be ["a1b2", "a1B2", "A1b2", "A1B2"]. Another example: if the input string is s = "3z4", the output should be ["3z4", "3Z4"].

# Your function should handle both lowercase and uppercase input, and it should treat digits and special characters as invariable elements.

def solution(s):
    results = []
    s = list(s)
    n = len(s)
    def backtrack(nth, s):
        if nth == n:
            results.append(s[:])
            return 
        s = s[:]
        i = nth
        c = s[i]
        backtrack(i + 1, s)
        if (ord(c) >= 65 and ord(c) <= 90):
            backtrack(i + 1, s[:i] + [chr(ord(c) + 32)] + s[i+1:])
        elif (ord(c) >= 97 and ord(c) <= 122):
            backtrack(i + 1, s[:i] + [chr(ord(c) - 32)] + s[i+1:])

    backtrack(0, s)
    
    answers_str = [] 
    for a in results:
        st = "".join(a)
        answers_str.append(st)

    return answers_str