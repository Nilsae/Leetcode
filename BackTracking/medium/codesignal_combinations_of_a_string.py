# Given a string s of n characters, your task is to write a Python function called all_combinations(s) that uses a recursive algorithm to generate and return a list of all possible combinations of the characters in the string, including the original string and its reverse. The combinations should be sorted in alphabetical order.

# For instance, if the input is 'abc', the function should return a list of all possible combinations: ['a', 'ab', 'abc', 'ac', 'acb', 'b', 'ba', 'bac', 'bc', 'bca', 'c', 'ca', 'cab', 'cb', 'cba'].








def all_combinations(s):
    answers = []
    s = list(s)
    used = set()
    def backtrack(s, first, used):
        if first == len(s) - 1:
            for cut in range(1, len(s)+1):
                if s[:cut] not in answers:
                    answers.append(s[:cut])
                    used = set()
        s = s[:]
        for i in range(first, len(s)):
            s[first], s[i] = s[i], s[first]
            # s = s[:first] + s[i] + s[first+1:i] + s[first] + s[i+1:]
            used.add(first)
            backtrack(s, first + 1, used)
            s[first], s[i] = s[i], s[first]
            # s = s[:first] + s[i] + s[first+1:i] + s[first] + s[i+1:]
    backtrack(s, 0, used)
    answers_str = [] 
    for a in answers:
        st = "".join(a)
        answers_str.append(st)

    return answers_str