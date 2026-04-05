class Solution:
    def customSortString(self, order: str, s: str) -> str:
        d = {}
        for i, c in enumerate(order):
            d[c] = i
        answer = [c for c in s if c in d]
        dummies = [c for c in s if c not in d]
        answer.sort(key = lambda x: d[x])
        a = ""
        for c in answer:
            a += c
        for c in dummies:
            a += c
        return a
