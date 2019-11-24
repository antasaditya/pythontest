class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        gasMinusCost = [g-c for g,c in zip(gas,cost)]
        l = len(gas)
        
        min_sum = math.inf
        sum = 0;
        min_ind = -2
        for i,x in enumerate(gasMinusCost):
            sum += x;
            if sum <= min_sum: 
                min_sum = sum
                min_ind = i
            print(i,x,sum,min_ind)
                
        if sum < 0:
            return -1
        else:
            return (min_ind+1)%l
        
        '''
        for i,delta in enumerate(self.gasMinusCost):
            if delta>=0 and self.canCompleteCircuitAt(i):
                return i;
        '''            

    def canCompleteCircuitAt(self, ind):
        sum = 0
        for i in range(self.l):
            sum += self.gasMinusCost[(ind+i) % self.l]
            if sum < 0:
                return False;
        return True;    