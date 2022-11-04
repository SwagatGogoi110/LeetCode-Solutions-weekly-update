// Time:  O(n)
// Space: O(n)

// greedy
class Solution {
public:
    int sortArray(vector<int>& nums) {
        const auto& min_moves = [&](int d) {
            vector<int> lookup(size(nums));
            for (int i = 0; i < size(nums); ++i) {
                lookup[nums[i]] = i;
            }
            int result = 0, i = 1;
            while (i < size(nums)) {
                int ni = -1;
                if (lookup[0] != d * (size(nums) - 1)) {
                    ni = lookup[0] + d;
                } else {
                    for (; i < size(nums) && lookup[i] + d == i; ++i);
                    if (i == size(nums)) {
                        continue;
                    }
                    ni = i;
                }
                swap(lookup[0], lookup[ni]);
                ++result;
            }
            return result;
        };

        return min(min_moves(0), min_moves(1));
    }
};