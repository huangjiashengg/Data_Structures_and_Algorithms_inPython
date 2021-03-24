from 算法与数据结构.Dstack import Stack
def infixPostfix(infixexpr):
    pre = {}
    pre["*"] = 3
    pre["/"] = 3
    pre["-"] = 2
    pre["+"] = 2
    pre["("] = 1
    opStack = Stack()
    postfixList = []
    tokenList = infixexpr.split()

    for token in tokenList:
        if token in "ABCDFFGHIJKLMNOPQRSTUVWXYZ" or token in "0123456789":
            postfixList.append(token)
        elif token == '(':
            opStack.push(token)
        elif token == ')':
            toptoken = opStack.pop()
            while toptoken != '(':
                postfixList.append(toptoken)
                toptoken = opStack.pop()
        else:
            while (not opStack.isEmpty()) and (pre[opStack.peek()] >= pre[token]):
                postfixList.append(opStack.pop())
            opStack.push(token)
    while not opStack.isEmpty():
        postfixList.append(opStack.pop())
    return "".join(postfixList)
print(infixPostfix("( A + B * C ) / D "))