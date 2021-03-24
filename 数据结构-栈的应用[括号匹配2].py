from 算法与数据结构.Dstack import  Stack
def parchecker(symbolstring):
     s = Stack()
     balance = True
     index  = 0
     while index < len(symbolstring) and balance == True:
         symbol = symbolstring[index]
         if symbol in "{[(":
             s.push(symbol)
         else:
            if s.isEmpty():
                balance = False
            else:
                top = s.pop()
                if not matches(top,symbol):
                    balance = False
         index = index + 1
     if balance and s.isEmpty():
         return True
     else:
         return False
def matches(open,close):
    opens = "{[("
    closes = "}])"
    return opens.index(open) == closes.index(close)

print(parchecker("{}"))