from 算法与数据结构.Dstack import Stack
def postfixEval(fixpostexpr):
    operandstack = Stack()
    fixpostList = fixpostexpr.split()
    for token in fixpostList:
        if token in [str(x) for x in range(1000)]:
            operandstack.push(token)
        else:
            operand2 = int(operandstack.pop())
            operand1 = int(operandstack.pop())
            result = dmath(token, operand1, operand2)
            operandstack.push(result)
    return operandstack.pop()
def dmath(token, operand1, operand2):
    if token == "+":
        return operand1 + operand2
    elif token == "-":
        return  operand1 -operand2
    elif token == "*":
        return operand1 * operand2
    else:
        return operand1 / operand2

print(postfixEval("86 9 2 + *"))
