class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        if(n < 10):
            return 0
        tot_sum = 0
        tot_prod = 1
        n1 = n
        while(n1 != 0):
            tot_sum = tot_sum + (n1 % 10)
            tot_prod = tot_prod * (n1 % 10)
            n1 = int(n1/10)
        return (tot_prod - tot_sum)
        