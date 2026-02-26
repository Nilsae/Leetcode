# You are given two strings, string1 and string2. Your goal is to determine a new string, string3, that is formed by characters that occur in both string1 and string2 in the same order as they occur in string1.

# Characters in string3 should maintain their original sequence order from string1. If a character is repeated in string1 and string2, include that character in string3 as many times as it occurs in both strings, but not more than that.

# For example, given string1 = "apple" and string2 = "peach", the resulting string3 would be "ape".

# Your algorithm should not exceed a time complexity of 
# O(string1.length+string2.length).
def solution(string1, string2):
    s3 = ""
    n2 = len(string2)
    n1 = len(string1)
    s2 = {}
    for i in range(n2):
        if string2[i] not in s2:
            s2[string2[i]] = 1
        else:
            s2[string2[i]] += 1
    for i in range(n1):
        if string1[i] in s2:
            s3 += string1[i]
            s2[string1[i]] -= 1
            if s2[string1[i]] == 0:
                s2.pop(string1[i])
    return s3



# You are given a string s. Your task is to create a function that checks whether the string s consists of one repeated substring.

# If it does, the function should return the substring. If there are multiple possible answers, return the longest one. If it does not consist of a repeated substring, return an empty string.

# To clarify, a "repeated substring" refers to a pattern of characters that reoccurs throughout the full string, with no characters left over. For example, the string "abababab" consists of repeated substrings "ab" and "abab". On the other hand, the string "abcabcab" does not consist of a repeated substring, as the final characters "ab" do not complete the repeating pattern of "abc".
def repeat_substring(s):
    lst = []
    # for i in range(len(s)):
    for w_len in range(1, len(s)//2 + 1):
        if s[:w_len] == s[w_len: w_len *2]:
            lst.append(w_len)
    lst = lst[::-1]
    # print(lst)
    for w_len in lst:
        if len(s)%w_len == 0:
            for i in range(0, len(s) - w_len, w_len):
                if s[i:i+w_len] != s[i+w_len: i+2*w_len]:
                    break
            else:
                return s[:w_len]
    return ""
# print(repeat_substring("1111111111"))




# efficient Largest Common Prefix
# To add an additional layer of complexity, in this task, you need to find a more efficient approach with the expected complexity of 
# O(strs.length⋅log(strs.length)⋅max_length).

# Hint: think about ordering strings in some way.
def efficient_LCP(strs):
    sorted_strs = sorted(strs)
    s1 = sorted_strs[0]
    s2 = sorted_strs[-1]
    max_i = len(s1)
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            max_i = i
            break
    return sorted_strs[0][:max_i]




# You are given a string of characters. Your task is to write a function that will find and return the most common substring of a given length in the input string. If two or more substrings have the same maximum frequency, you should return the lexicographically smallest one.

# For example, given the input string "bananabananaba" and a substring length of 5, your function should return "anaba", since it appears twice and is lexicographically smaller than other substrings that also appear twice (e.g., "banan").

# The expected time complexity for this task is 
# O(str.length⋅length).
def find_most_common_substring(s: str, length: int) -> str:
    all_subs = {}
    for i in range(len(s) - length + 1):
        sub = s[i:i + length]
        # print(sub)
        if sub in all_subs:
            all_subs[sub] += 1
        else:
            all_subs[sub] = 1
    most_commons = []
    # print(all_subs)
    max_num = max(all_subs.values())
    for sub, num in all_subs.items():
        if num == max_num:
            most_commons.append(sub)
    return sorted(most_commons)[0]
# print((find_most_common_substring('zyxwvutsr', 1)))