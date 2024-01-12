def lonelyinteger(a):
    # Write your code here
    bins = [0] * 100
    
    a.sort()
    
    for each in a:
        bins[each] += 1
        
    return bins.index(1)
