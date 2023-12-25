int minSubArrayLen(int target, int* nums, int numsSize) {
    int min_len = INT_MAX;

    for (int i = 0; i < numsSize; i++) {
        int sum = nums[i];
        int count = 0;
        count++;

        // Check if len == 1 is a possible solution
        if (sum >= target && count < min_len) {
            return count;
        }

        // Sliding window to aggregate
        for (int j = i+1; j < numsSize; j++) {
            sum += nums[j];
            count++;
            // printf("i: %d, j: %d, sum: %d, count: %d\n", nums[i],nums[j], sum, count);

            if (sum >= target && count < min_len) {
                min_len = count;
            }
        }
    }

    return min_len == INT_MAX ? 0 : min_len;
}


// Min length of sum >= target
// Sliding window to get the sums of each thing -> cut off once >= target to get shortest arr len
// Repeat for each i where j is the other end of the window starting at i
