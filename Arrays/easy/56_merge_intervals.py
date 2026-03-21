
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        k0 = intervals[0][0]
        max_k1 = intervals[0][1]
        answer = []
        for i in range(len(intervals) - 1):
            if max_k1 < intervals[i+1][0]:
                answer.append([k0, max_k1])
                k0 = intervals[i+1][0]
                max_k1 = intervals[i+1][1]
            max_k1 = max(max_k1, intervals[i + 1][1])
          
            
        answer.append([k0, max_k1])
        return answer