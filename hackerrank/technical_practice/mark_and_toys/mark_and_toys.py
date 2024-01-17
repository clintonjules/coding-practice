def maximumToys(prices, k):
    # Write your code here
    prices.sort()
    
    if prices[0] > k:
        return 0
    elif prices[0] == k:
        return 1
    
    count = 0
    
    for p in prices:
        if p <= k:
            count += 1
            k -= p
        
        else:
            break
            
    return count
