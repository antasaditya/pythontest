class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s)<=1:
            return(s)

        #f = [  d[i//2] if i%2==0 else ' ' for i in range(len(e))]
        #pivots = len(s);
        #i=0
        
        slen = len(s)
        candidate_count = 2*(slen)-1
        max_len = 0;
        for p in range(candidate_count):
            j = p%2;
            while True:
                left = (p-j)//2
                right = (p+j)//2
                #print(p,j,left,right)
                if  left < 0 or right >= slen or s[left] != s[right]:
                    break;
                pal_len = right-left+1;
                if pal_len > max_len: 
                    best_left = left 
                    best_right = right
                    max_len = pal_len
                j+=2;
        return(s[best_left:best_right+1])
        