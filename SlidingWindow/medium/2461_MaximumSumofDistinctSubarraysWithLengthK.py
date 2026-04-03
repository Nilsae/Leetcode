class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        max_sum = 0
        cur_sum = 0
        seen_dict = {}
        w_len = 0
        for i in range(len(nums)):
            if nums[i] not in seen_dict:
                if w_len == k:
                    seen_dict.pop(nums[i-k])
                    cur_sum -= nums[i-k]
                else:
                    w_len += 1
            else:
                last_rep_idx = seen_dict[nums[i]]
                for j in range(min(seen_dict.values()), last_rep_idx + 1):
                        cur_sum -= nums[j]
                        seen_dict.pop(nums[j])
                w_len = i - last_rep_idx
            cur_sum += nums[i]
            seen_dict[nums[i]] = i
            if w_len == k:
                max_sum = max(max_sum, cur_sum)
            # print(w_len, cur_sum)
        return max_sum
            
             
        
            