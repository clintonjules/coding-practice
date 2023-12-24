#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#

def countingValleys(steps, path):
    # Write your code here
    level = 0
    count = 0
    prev = 0
    
    for s in path:
        if s == "U":
            prev = level
            level += 1
            # prev = "U"
            
        elif s == "D":
            prev = level
            level -= 1
            # prev = "D"
    
        if prev < 0:
            if level >=0:
                count+=1
    
    return count
