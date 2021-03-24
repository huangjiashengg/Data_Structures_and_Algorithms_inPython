#栈用于诸如"()))(()"括号匹配：后进先出，一旦遇到结束符即可用pop消掉开始符
from 算法与数据结构.Dstack import Stack
def parchecker(symbolstring):
    s = Stack()
    balance = True
    index = 0
    while index < len(symbolstring) and balance:
        symbol = symbolstring[index]
        if symbol == "(":
            s.push(symbol)
        else:
            if s.isEmpty():
                balance = False
            else:
                s.pop()
        index = index + 1
    if s.isEmpty() and balance:
        return True
    else:
        return False

print(parchecker("()()(()())("))