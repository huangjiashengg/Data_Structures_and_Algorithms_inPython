# 列表计算所有元素之和的递归形式：已知加和即为两个元素执行相加运算，有限个加和则进行递归运算两个元素之和

# def listsum(numList):
#     if len(numList) == 1:
#         return numList[0]
#     else:
#         return numList[0] + listsum(numList[1:])
#
#
# print(listsum([1, 3, 5, 7, 9]))
# ------------------------------------------------------------------------------------------------------------
# 将整型转换为字符型，利用递归整除的方式


# def toStr(n, base):
#     convertString = '0123456789ABCDEF'
#     if n < base:
#         return convertString[n]
#     else:
#         return toStr(n // base, base) + convertString[n % base]
#
#
# print(toStr(567, 10))
# -------------------------------------------------------------------------------------------------------
# from 算法与数据结构.Dstack import Stack
#
#
# def toStr(n, base):
#     rStack = Stack()
#     ret = ''
#     converString = '0123456789ABCDEF'
#     while n > 0:
#         if n < base:
#             rStack.push(converString[n])
#         else:
#             rStack.push(converString[n % base])
#         n = n // base
#     while not rStack.isEmpty():
#         ret = ret + rStack.pop()
#     return ret
#
# print(toStr(567, 10))

# -----------------------------------------------------------------------------------

# 递归画图
# import turtle
#
# myTurtle = turtle.Turtle()   # 创建一只乌龟
# myWin = turtle.Screen()  # 创建一个画画的屏幕
#
#
# def drawSpiral(myTurtle, linelen):
#     if linelen > 0:
#         myTurtle.forward(linelen)  # 向前走
#         myTurtle.right(90) # 向右拐弯
#         drawSpiral(myTurtle, linelen - 5)  # 递归，重复执行上述两个步骤，知道条件不满足为止
#
#
# drawSpiral(myTurtle, 300)
# myWin.exitonclick()


import turtle


def tree(branchlen, t):
    if branchlen > 5:
        t.forward(branchlen)
        t.right(20)
        tree(branchlen - 15, t)
        t.left(40)
        tree(branchlen - 15, t)
        t.right(20)
        t.backward(branchlen)


def main():
    t = turtle.Turtle()
    mywin = turtle.Screen()
    t.left(90)
    t.up()
    t.backward(300)
    t.down()
    t.color('green')
    tree(130, t)
    mywin.exitonclick()

main()






