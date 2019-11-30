class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        opmap = {
            "+" : lambda x,y: x+y,
            "-" : lambda x,y: x-y,
            "*" : lambda x,y: x*y,
            "/" : lambda x,y: x/y
        }        
        for t in tokens:
            op = opmap.get(t,None);
            if op != None:
                a2 = stack.pop();
                a1 = stack.pop();
                stack.append(int(op(a1,a2)))
            else:
                stack.append(int(t));
        return(stack[0])