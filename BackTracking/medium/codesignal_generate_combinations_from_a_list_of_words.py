# As part of the team of software engineers at XYZ Corp, you're working on a new word game. The game takes an array of n strings, where each string contains m characters. Your task is to design a Python program that returns all combinations of the characters in the strings by taking one character from each string to form a unique word. Words should be returned in alphabetical order.

# Return an array of all the new words.

# For example, for words = ["abc", "def", "ghi"], the output should be ["adg", "adh", "adi", "aeg", "aeh", "aei", "afg", "afh", "afi", "bdg", "bdh", "bdi", "beg", "beh", "bei", "bfg", "bfh", "bfi", "cdg", "cdh", "cdi", "ceg", "ceh", "cei", "cfg", "cfh", "cfi"].

def solution(words):
    results = []
    for i in range(len(words)):
        words[i] = list(words[i])
    indices = [0 for j in range(len(words))]
    new_word = []
    def backtrack(new_word, word_num):
        if word_num == len(words):
            results.append(new_word)
            return
        new_word = new_word[:]
        for c in words[word_num]:
            backtrack(new_word + [c], word_num + 1)

    backtrack([], 0)
    
    answers_str = [] 
    for a in results:
        st = "".join(a)
        answers_str.append(st)

    return sorted(answers_str)