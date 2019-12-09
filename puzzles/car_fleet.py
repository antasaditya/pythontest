'''
N cars are going to the same destination along a one lane road.  The destination is target miles away.

Each car i has a constant speed speed[i] (in miles per hour), and initial position position[i] miles towards the target along the road.

A car can never pass another car ahead of it, but it can catch up to it, and drive bumper to bumper at the same speed.

The distance between these two cars is ignored - they are assumed to have the same position.

A car fleet is some non-empty set of cars driving at the same position and same speed.  Note that a single car is also a car fleet.

If a car catches up to a car fleet right at the destination point, it will still be considered as one car fleet.


How many car fleets will arrive at the destination?

 

Example 1:

Input: target = 12, position = [10,8,0,5,3], speed = [2,4,1,1,3]
Output: 3
Explanation:
The cars starting at 10 and 8 become a fleet, meeting each other at 12.
The car starting at 0 doesn't catch up to any other car, so it is a fleet by itself.
The cars starting at 5 and 3 become a fleet, meeting each other at 6.
Note that no other cars meet these fleets before the destination, so the answer is 3
'''

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        if len(position) == 0:
            return 0;
        
        ps = list(zip(position, speed))
        
        #sort so that you cant bypass 
        ps.sort(key=lambda x:(x[0],x[1]))
        
        #time to reach target if there is no obstacle
        ts = [(target-x[0])/x[1] for x in ps]
        
        #now for all i,j ts[i] >= ts[j] where i > j  
        
        #[10,8,0,5,3]
        #[2,4,1,1,3]
        
        #[0, 3, 5, 8, 10]
        #[1, 3, 1, 4, 2 ]
        #[12, 3, 7, 1, 1]
        
        fleet = ts[-1]
        fleet_count = 1;
        for i in reversed(ts):
            if i <= fleet:
                continue;
            else:
                fleet = i
                fleet_count += 1
        
        return fleet_count
                
            
        
                
        