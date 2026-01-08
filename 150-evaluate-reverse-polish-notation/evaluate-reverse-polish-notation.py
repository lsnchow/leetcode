class Solution(object):
    def evalRPN(self, tokens):
        stack = []
        curr = 0
        for i in tokens:
            if not stack:
                # always a number
                stack.append(int(i))
            else:
                if i in ["/","+","-","*"]:
                    b = stack.pop()
                    a = stack.pop()
                    if i == "/":
                        stack.append(int(float(a)/b))
                    elif i == '+':
                        stack.append(a+b)
                    elif i == '-':
                        stack.append(a-b)
                    else:
                        stack.append(a*b)
                else:
                    stack.append(int(i))
        return stack.pop()