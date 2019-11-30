class Solution:
    '''
    4 2 4 5 2 3 0 8 9 9 9 2 3 3
    2 1 2 3 1 2 1 2 3 1 2 1 2 1
    '''
    def candy(self, ratings: List[int]) -> int:
        #1, 0, 2
        lenr = len(ratings)
        if lenr <= 1:
            return lenr;
        
        if lenr == 2:
            if ratings[0] == ratings[1]:
                return 2
            else:
                return 3; 
           
        candies = [0] * lenr; 
        zero_count = lenr+1;    
    
        rev = 0;
        while True:
            new_zero_count = sum( [1 if x == 0 else 0 for x in candies] )
            if new_zero_count == zero_count or new_zero_count == 0:
                break;
            zero_count = new_zero_count; 
            
            if rev==0:
                ranges = range(lenr)
            else:
                ranges = reversed(range(lenr))
            rev = (rev+1)%2
            
            for i in ranges:
                nbr = []
                nbc = []
                
                if i > 0:
                    nbr.append(ratings[i-1])
                    nbc.append(candies[i-1])
                if i < lenr-1: 
                    nbr.append(ratings[i+1])
                    nbc.append(candies[i+1])

                #already allocated
                if candies[i] >0:
                    continue;
                    
                #if less than equal to neighbours, gets one candy
                if ratings[i] <= min(nbr):
                    candies[i] = 1
                    continue;
                
                zipn = list(zip(nbr,nbc))
                            
                #if there is a smaller neighbour uninitialized lets come here late
                if len([x for x in zipn if x[0] < ratings[i] and x[1]==0])>0:
                    continue;

                zipn = list(zip(nbr,nbc))
                #should get more candy than neighbours already having candy
                pcs = [x[1] for x in zipn if x[0] < ratings[i] and x[1]>0]
                if len(pcs) > 0:
                    candies[i] = 1+max(pcs)
            
            
        return(sum(candies))