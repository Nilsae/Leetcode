class Solution(object):
    def CleanerIsValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        bracket_map = {")":"(", "]":"[", "}":"{"}
        stack = []
        for c in s:
            if c in bracket_map.values():
                stack.append(c)
            elif c in bracket_map and stack and stack[-1]== bracket_map[c]:
                stack.pop()
            else:
                return False
        if not stack:
            return True
        return False
    
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        for c in s:
            if c == "(":
                stack.append(1)
            elif c == ")" and stack and stack[-1]==1:
                stack.pop()
            elif c == "[":
                stack.append(2)
            elif c == "]"  and stack and stack[-1]==2:
                stack.pop()
            elif c == "{":
                stack.append(3)
            elif c == "}"  and stack and stack[-1]==3:
                stack.pop()
            else:
                return False
        if not stack:
            return True
        return False
# print(Solution().isValid(s = "({{{{}}}))"))
# Example 1:

# Input: s = "()"

# Output: true

# Example 2:

# Input: s = "()[]{}"

# Output: true

# Example 3:

# Input: s = "(]"

# Output: false

# Example 4:

# Input: s = "([])"

# Output: true