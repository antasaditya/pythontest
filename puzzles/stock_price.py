class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if 0==len(prices):
            return 0;
        
        new_prices = [prices[0]];
        for i in range(1,len(prices)):
            if prices[i] != new_prices[-1]:
                new_prices.append(prices[i])
        prices = new_prices

        min = None;
        current_income = 0
        for i in range(len(prices)):
            prev = prices[i-1] if i > 0 else prices[0]+1
            next = prices[i+1] if i < len(prices)-1 else prices[-1]-1
            
            print(str(prev) + "," + str(prices[i]) + "," + str(next))
            
            if prev > prices[i] and next > prices[i]:
                if min == None or prices[i] < min:
                    min = prices[i]
                    print("min=" + str(min))
                    
            if prev < prices[i] and next < prices[i]:
                if min != None:
                    candidate = prices[i]-min;
                    current_income = max(candidate, current_income)
                    print("candidate=" + str(candidate))
                    
        return(current_income)
                    