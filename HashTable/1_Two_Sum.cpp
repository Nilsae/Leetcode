class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        // std::map<int, int> dictionary; lookup time avg: o(log n)
        std::unordered_map<int, int> dictionary; // lookup time avg: o(1)
        int n = nums.size();
        for (int i = 0; i < n ; i++){
            int complement  = target - nums[i];
            auto it = dictionary.find(complement);
            if (it != dictionary.end()) {
                // return {i, dictionary[complement]};
                return {i, it -> second}; // it -> second: complement
            }
            else {
                dictionary[nums[i]] = i;
            }
        } 
        return {};
    }
};