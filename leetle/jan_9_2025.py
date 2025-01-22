'''
Leetle #9 2/6 10:35
[6 lines]

🟥🟥🟥🟥🟥🟥
🟩🟩🟩🟩🟩🟩
https://leetle.app
'''

def solve(nums, k):
  output = []
  
  for i in range(len(nums)):
    if i + k <= len(nums):
      output.append(max(nums[i:i+k]))

  return output
