class Sol:
    def min_cost_climbing(self,cost):
        i = len(cost) - 1
        j = len(cost) - 2
        sum=0
        while j>0:
            min_cost=min(cost[i],cost[j])
            sum+=min_cost
            if min_cost==cost[i]:
                i-=2
                j-=2
            else:
                i-=1
                j-=1
        return sum

if __name__ == '__main__':
    p=Sol()
    print(p.min_cost_climbing([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]))
