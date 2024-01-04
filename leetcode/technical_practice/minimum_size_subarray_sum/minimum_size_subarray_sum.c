int minSubArrayLen(int target, int* nums, int numsSize) {
    int min_len = INT_MAX;
    int left = 0, right = 0, sum = 0;

    for (; right < numsSize; right++) {
        // Increment until the target condition is met
        sum += nums[right];

        // Oh, wait, STOP!!!
        // We need to check if the len of this iteration is the min
        // how do we check the len of the current iteration
        // That's why we keep track of the left and right!
        while (sum >= target) {
            int current_len = right-left +1;

            if (min_len > current_len) {
                min_len = current_len;
            }

            sum -= nums[left];
            
            // Once we find the len and compare, onto to the next min window using left
            left++;
        }
    }

    return min_len == INT_MAX ? 0 : min_len;
}


// Min length of sum >= target
// Sliding window to get the sums of each thing -> cut off once >= target to get shortest arr len
// Repeat for each i where j is the other end of the window starting at i
