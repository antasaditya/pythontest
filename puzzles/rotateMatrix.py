class Solution:
    def prnt(self, a):
        print("...")
        for x in a:
            print(x)
        print("\n\n")
            
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        #self.prnt(matrix)
        N = len(matrix)
        for base in range(N//2):
            for ind in range(N-2*base-1):
                #print("--->", base, ind)
                self.rotateOuter(matrix, base, ind)
                #self.prnt(matrix)

        
        #self.prnt(matrix)

    def rotateOuter(self, a, base, ind):
        N = len(a)
        zero = base
        last = N-base-1
        
        first  = (base,base+ind);
        second = (base+ind,last);
        third  = (last,last-ind);
        fourth = (last-ind,base);   
        
        '''
        print(
            "will swap", 
            [ first, second, third, fourth ]       
        )
        '''
        
        def copy(a, elem1, elem2):
            x1,y1 = elem1
            x2,y2 = elem2
            a[x1][y1] = a[x2][y2]
            
        
        firstElem = a[first[0]][first[1]]
        copy(a, first, fourth)
        copy(a, fourth, third)
        copy(a, third, second)
        a[second[0]][second[1]] = firstElem
        
            