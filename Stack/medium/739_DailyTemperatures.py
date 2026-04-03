class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = [0 for i in range(len(temperatures))]
        d = {}
        for i, temp in enumerate(temperatures):
            past_temps_to_be_removed = []
            for past_temp in d.keys():
                if temp > past_temp:
                    for value in d[past_temp]:
                        if answer[value] == 0:
                            answer[value] = i - value
                    past_temps_to_be_removed.append(past_temp)
            for pt in past_temps_to_be_removed:
                d.pop(pt)
            if temp not in d:
                d[temp] = [i]
            else:
                d[temp].append(i)
        return answer

