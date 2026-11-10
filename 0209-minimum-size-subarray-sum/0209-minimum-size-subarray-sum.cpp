class Solution {
public:
    int minSubArrayLen(int target, vector<int>& nums) {
        int minLenWindow = INT_MAX;
        int currentSum = 0;
        int low = 0;
        int high = 0;

        while (high < nums.size()){
            currentSum += nums[high];
            high++;
            
            while (currentSum >= target){
                int currentWindowSize = high - low;
                minLenWindow = min(currentWindowSize, minLenWindow);
                currentSum -= nums[low];
                low++;

            }
        }
        if (minLenWindow == INT_MAX){
            return 0;
        }
        
    return minLenWindow;  
    }
    
};