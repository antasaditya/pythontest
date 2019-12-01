'''
Given a positive integer, return its corresponding column title as appear in an Excel sheet.

For example:

    1 -> A
    2 -> B
    3 -> C
    ...
    26 -> Z
    27 -> AA
    28 -> AB 
    ...
Example 1:

Input: 1
Output: "A"
Example 2:

Input: 28
Output: "AB"
Example 3:

Input: 701
Output: "ZY"

'''


class Solution:
    def convertToTitle(self, n: int) -> str:
        '''
            BZ --> 2*26 + 26 
               --> 2x + 1 
            
            78/26 --> 30
                  --> 2,10
            
            26*26 + 26 --> 26 
            
            27 0  
            
            divide by 26. 
            if mod is 0, this means you need a Z 
            reduce dividend by 1 and make mod 26.. 
            
            the point is mod=26 is valid
            
        '''
        ret = "";
        
        while n > 0:
            mod = n % 26;
            div = int(n / 26); 
            if mod == 0:
                div = div-1
                mod = 26
            n = div
            ret = chr(int(64+mod)) + ret
        
        return(ret)
        
        
            
            
        
        
        