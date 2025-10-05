def numTeams(self, rating: List[int]) -> int:
        total = 0

        for j in range(1, len(rating)):
            ll, ls, rl, rs = 0, 0, 0, 0

            for i in range(j):
                ll += 1 if rating[i] > rating[j] else 0
                ls += 1 if rating[i] < rating[j] else 0

            for k in range(j+1, len(rating)):
                rl += 1 if rating[k] > rating[j] else 0
                rs += 1 if rating[k] < rating[j] else 0

            total += ls*rl + ll*rs

        return total
