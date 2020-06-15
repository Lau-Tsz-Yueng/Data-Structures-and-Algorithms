class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if len(tokens) == 1:
            return int(tokens[0])
        tmp = 0
        for i in range(len(tokens)):
            for j in range(len(tokens)):
                if tokens[j] == '+' or tokens[j] == '-' or tokens[j] == '/' or tokens[j] == '*':
                    if tokens[j] == '+':
                        tmp = int(tokens[j-2]) + int(tokens[j-1])
                    elif tokens[j] == '-':
                        tmp = int(tokens[j-2]) - int(tokens[j-1])
                    elif tokens[j] == '/':
                        tmp = int(int(tokens[j-2]) / int(tokens[j-1]))
                    elif tokens[j] == '*':
                        tmp = int(tokens[j-2]) * int(tokens[j-1])
                    if len(tokens) == 3:
                        return (tmp)
                    else:
                        tokens[j] = str(tmp)
                        tokens.pop(j-2)
                        tokens.pop(j-2)
                        break
    
