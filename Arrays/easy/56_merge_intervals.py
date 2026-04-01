
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
    

# more readable:

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 1:
            return intervals
        intervals.sort(key = lambda x: x[0])
        answer = []
        prev_start = intervals[0][0]
        max_end = intervals[0][1]
        for i in range(len(intervals) - 1):
            new_start = intervals[i + 1][0]
            new_end = intervals[i + 1][1]
            if max_end < new_start:
                new_interval = [prev_start, max_end]
                answer.append(new_interval)
                prev_start = new_start
                max_end = new_end
    
            max_end = max(max_end, new_end)
        answer.append([prev_start, max_end])
        return answer