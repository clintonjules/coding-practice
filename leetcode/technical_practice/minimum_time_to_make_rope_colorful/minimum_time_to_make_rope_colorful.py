def minCost(self, colors: str, neededTime: List[int]) -> int:
    cost = 0

    if len(set(colors)) == 1:
        neededTime.sort()
        
        return sum(neededTime[:-1])

    for i in range(len(colors)):
        tmp = [neededTime[i]]
        
        for j in range(i+1,len(colors)):
            if colors[i] == colors[j]:
                tmp.append(neededTime[j])
                neededTime[j] = 0
            else: 
                break

        tmp.sort()

        cost += sum(tmp[:-1])

    return cost
