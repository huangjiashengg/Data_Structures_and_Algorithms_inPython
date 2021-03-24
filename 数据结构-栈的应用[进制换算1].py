from 算法与数据结构.Dstack import Stack
#1，输入十进制数值；2，除以进制数；3，将一个一个的余数放进栈；4，最顶部的数字放在最前面；5，输出
def divideByn(n):
    s = Stack()
    num = input("请输入一个十进制数值：")
    num = int(num)
    while num > 0:
        leftnum = num % n
        s.push(leftnum)
        num = num // n
    result = ""
    while not s.isEmpty():
        result = result + str(s.pop())
    print(result)
divideByn(8)








