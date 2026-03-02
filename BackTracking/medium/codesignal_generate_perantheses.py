# Given an integer n, your task is to return an array with all the possible combinations of n pairs of parentheses that are correct. A correct combination of parentheses is one where every opening bracket has a corresponding closing bracket.

# For example, given n = 3, the possible combinations would be ["((()))", "(()())", "(())()", "()(())", "()()()"].


def generate_parentheses(n: int) -> list[str]:
    answers = []
    s = []
    if n == 0:
        return []
    def backtrack(s, num_closed, num_open):
        if len(s) == n * 2:
            answers.append(s[:])
            # s = []
            # num_open = 0
            # num_closed = 0
            return
        
        if num_open < n:
            s.append("(")
            backtrack(s, num_closed, num_open + 1)
            s.pop() # s.pop() actually removes the last element from the list s in place, so it undoes the last append and keeps the same list object. s[:-1] creates a new list that is a copy of s without the last element, but it does not modify s itself
        if num_open > num_closed:
            s.append(")")
            backtrack(s, num_closed + 1, num_open)
            s.pop()
            
    backtrack(s, 0, 0)
    answers_str = [] 
    for a in answers:
        st = "".join(a)
        answers_str.append(st)

    return answers_str
            
            

            