# 链表实现的基本构造块是节点
# 节点的定义：每个节点必须保存只少两个信息：1，节点的数据字段；2，对下一个节点的引用


class Node:
    def __init__(self, initdata):
        self.data = initdata
        self.next = None

    def getdata(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self, newdata):
        self.data = newdata

    def setNext(self, newnext):
        self.next = newnext

