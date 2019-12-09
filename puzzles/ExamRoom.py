'''
In an exam room, there are N seats in a single row, numbered 0, 1, 2, ..., N-1.

When a student enters the room, they must sit in the seat that maximizes the distance to the closest 
person.  If there are multiple such seats, they sit in the seat with the lowest number.  
(Also, if no one is in the room, then the student sits at seat number 0.)

Return a class ExamRoom(int N) that exposes two functions: ExamRoom.seat() 
returning an int representing what seat the student sat in, and ExamRoom.leave(int p) 
representing that the student in seat number p now leaves the room.  It is guaranteed that 
any calls to ExamRoom.leave(p) have a student sitting in seat p.
'''

class ExamRoom:

    def __init__(self, N: int):
        self.seated = []
        self.N = N
        
    def reset(self):
        self.potentialBestSeat = -1;
        self.potentialBestDst = -1; 
        self.potentialLocation = -1;
        
    def setPotential(self, seat, distance, location):
        if distance > self.potentialBestDst:
            self.potentialBestSeat = seat
            self.potentialBestDst = distance
            self.potentialLocation = location
    
    
    def seat(self) -> int:
        if len(self.seated) == 0:
            self.seated.append(0);
            return 0;
        
        self.reset()
        
        #first seat is empty
        if self.seated[0] != 0: 
            self.setPotential(0, self.seated[0], 0) 
        
        N = self.N
          
        #now lets rollover the existing entries
        for i in range(len(self.seated)-1):
            middle = (self.seated[i+1]-self.seated[i])//2
            if middle > 0:
                self.setPotential(self.seated[i]+middle, middle, i+1)

        #if last seat is empty
        if self.seated[-1] != N-1:
            self.setPotential(N-1, N-1-self.seated[-1], len(self.seated))                
        if self.potentialBestSeat > -1: 
            self.seated.insert(self.potentialLocation, self.potentialBestSeat)
            return self.potentialBestSeat
        else:
            return None
        
    def leave(self, p: int) -> None:
        self.seated.remove(p)

# Your ExamRoom object will be instantiated and called as such:
# obj = ExamRoom(N)
# param_1 = obj.seat()
# obj.leave(p)