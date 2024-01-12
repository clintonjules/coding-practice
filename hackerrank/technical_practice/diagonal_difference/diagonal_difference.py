def diagonalDifference(arr):
    # Write your code here
    sumA = 0
    sumB = 0

    # Since it's square, len(arr) shows how many elements in a row
    for i in range(len(arr)):
        sumA += arr[i][i]
        sumB += arr[(len(arr)-1) - i][i]
        
    return abs(sumA - sumB)
