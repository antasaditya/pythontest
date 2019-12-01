'''
Given the coordinates of four points in 2D space, return whether the four points could construct a square.

The coordinate (x,y) of a point is represented by an integer array with two integers.

Example:

Input: p1 = [0,0], p2 = [1,1], p3 = [1,0], p4 = [0,1]
Output: True
'''

class Solution:
    def dist2(self, p1, p2):
        xd = p1[0]-p2[0]
        yd = p1[1]-p2[1]
        return xd*xd+yd*yd;
    
    def addToMap(self, m, d):
        curr = m.get(d, 0)
        m[d] = curr+1
    
    
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        m = {};
        self.addToMap(m, self.dist2(p1,p2))
        self.addToMap(m, self.dist2(p1,p3))
        self.addToMap(m, self.dist2(p1,p4))
        self.addToMap(m, self.dist2(p2,p3))
        self.addToMap(m, self.dist2(p2,p4))
        self.addToMap(m, self.dist2(p3,p4))

        print(m)
        if len(m) != 2: 
            return False;        
        keys = list(m.keys()); 
        vals = list(m.values());
        kvl = list(zip(keys, vals))
        kvl.sort(key=lambda x:x[0])
        return 2*kvl[0][0] == kvl[1][0] and kvl[0][1] == 4 and kvl[1][1] == 2

        
        