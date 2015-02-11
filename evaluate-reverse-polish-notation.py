# Evaluate the value of an arithmetic expression in Reverse Polish Notation.
# 
# Valid operators are +, -, *, /. Each operand may be an integer or another expression.
# 
# Some examples:
#   ["2", "1", "+", "3", "*"] -> ((2 + 1) * 3) -> 9
#   ["4", "13", "5", "/", "+"] -> (4 + (13 / 5)) -> 6
import time
#import operator
class Solution:#very quick solution
    # @param tokens, a list of string
    # @return an integer
    def evalRPN(self, tokens):
        stack =[]
        #operators = ['+','-','*','/']
        #operators = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.div}
        operators = {'+': 0, '-': 1, '*': 2, '/': 3}
        for item in tokens:
            
            if item not in operators:
                stack.append(int(item))
            else:
                index = operators[item]
                a = stack.pop()
                b = stack.pop()
                if index == 0:
                    stack.append(b+a)
                elif index==1:
                    stack.append(b-a)
                elif index == 2:
                    stack.append(b*a)
                else:#performance better than elif here
                    if a*b > 0:
                        stack.append(abs(b)/abs(a))
                    else:
                        stack.append(-(abs(b)/abs(a)))
            
        return stack.pop()

mysolution = Solution()
t0 = time.time()
print mysolution.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"])
t1 = time.time()
print str((t1-t0)*1000) +'s'
