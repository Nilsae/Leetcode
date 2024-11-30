class Solution(object):
    def romanToInt(self, s):
            """
            :type s: str
            :rtype: int
            """
            hashmap = {
                "I": 1,
                "V": 5,
                "X": 10,
                "L": 50,
                "C": 100,
                "D": 500,
                "M": 1000
            }
            result = 0
            for i, char in enumerate(s):
                print(f'i:', i, 'char:', char)
                if (i < len(s) - 1 and hashmap[char] < hashmap[s[i+1]]):
                    result -= hashmap[char]
                else:
                    result += hashmap[char]
            return result
print(Solution().romanToInt("MCMXCIV"))