
# 定义：二叉查找树依赖于左子树中找到的键小于父节点
# 以及右子树中找到的键都大于父节点的属性，这里将实
# 现两个类，一个是TreeNode，一个是BinarySearchTree,
# 两者分别的作用是：BinarySearchTree对TreeNode进行
# 引用。


class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.size = 0

    def length(self):
        return self.size

    def __len__(self):
        return self.size

    def __iter__(self):
        return self.root.__iter__()

    # 实现put()方法---添加一个新的键值对。如果键已存在，那么用新值代替旧值
    def put(self, key, val):
        if self.root:
            self._put(key, val, self.root)
        else:
            self.root = TreeNode(key, val)
        self.size = self.size + 1

    def _put(self, key, val, currentNode):
        if key < currentNode.key:
            if currentNode.hasLeftChild():
                self._put(key, val, currentNode.leftChild)
            else:
                currentNode.leftChild = TreeNode(key, val, parent=currentNode)
        else:
            if currentNode.hasRightChild():
                self._put(key, val, currentNode.rightChild)
            else:
                currentNode.rightChild = TreeNode(key, val, parent=currentNode)

    # 以下私有函数定义可以实现类似字典的赋值方式，如：myZipTree["Plymouth"] = 6979
    def __setitem__(self, key, value):
        self.put(key, value)

    # 实现get()方法---通过键返回值
    def get(self, key):
        if self.root:
            res = self._get(key, self.root)
            if res:
                return res.payload
            else:
                return None
        else:
            return None

    def _get(self, key, currentNode):
        if not currentNode:
            return None
        elif currentNode.key == key:
            return currentNode
        elif key < currentNode.key:
            return self._get(key, currentNode.leftChild)
        else:
            return self._get(key, currentNode.rightChild)

    # 以下私有函数定义可以实现类似字典的索引方式，如z = myZipTree["Plymouth"]
    def __getitem__(self, key):
        return self.get(key)

    # 以下私有函数定义可以实现in操作。如：if 'Plymouth' in myZipTree: print("Bingo")
    def __contains__(self, key):
        if self._get(key, self.root):
            return True
        else:
            return False
    # 以下定义删除函数
    def delete(self, key):
        if self.size > 1:
            nodeToRemove = self._get(key, self.root)
            if nodeToRemove:
                self.remove(nodeToRemove)
                self.size = self.size - 1
            else:
                raise KeyError('Error, key not in tree')
        elif self.size == 1 and self.root.key == key:
            self.root = None
            self.size = 0
        else:
            raise KeyError('Error, key not in tree')

    def __delitem__(self, key):
        self.delete(key)
# 一旦我们找到要删除的键的节点，必须考虑三种情况：
# 1，要删除的节点没有子节点；
# 2，要删除的节点只有一个子节点；
# 3，要删除的节点有两个子节点。
# 第一种情况相对比较简单，即直接删除节点并删除父节点对该节点的引用
    def remove(self, currentNode):
        if currentNode.isLeaf():
            if currentNode == currentNode.parent.leftChild():
                currentNode.parent.leftChild = None
            else:
                currentNode.parent.rightChild = None
# 第二种情况相对第三种情况来说简单，先看第三种情况，即要删除的节点
# 有两个子节点;这里我们用findSuccessor和findmin找到后继节点（用于替
# 换被删除节点的节点）；并使用spliceOut()删除后继节点
        elif currentNode.hasBothChildren():
            succ = currentNode.findSuccessor()
            succ.spliceOut()
            currentNode.key = succ.key
            currentNode.payload = succ.payload

        else:
            # 这里考虑第二种情况，即要删除的节点只有一个子节点
            if currentNode.hasLeftChild():
                if currentNode.isLeftChild():
                    currentNode.leftChild.parent = currentNode.parent
                    currentNode.parent.leftChild = currentNode.leftChild
                elif currentNode.isRightChild():
                    currentNode.leftChild.parent = currentNode.parent
                    currentNode.parent.rightChild = currentNode.leftChild
                else:
                    currentNode.replaceNodeData(currentNode.leftChild.key,
                                                currentNode.leftChild.payload,
                                                currentNode.leftChild.leftChild,
                                                currentNode.rightChild.rightChild)
            else:
                if currentNode.isLeftChild():
                    currentNode.rightChild.parent = currentNode.parent
                    currentNode.parent.leftChild = currentNode.rightChild
                elif currentNode.isRightChild():
                    currentNode.rightChild.parent = currentNode.parent
                    currentNode.parent.rightChild = currentNode.rightChild
                else:
                    currentNode.replaceNodeData(currentNode.rightChild.key,
                                                currentNode.rightChild.payload,
                                                currentNode.leftChild.leftChild,
                                                currentNode.rightChild.rightChild)





# TreeNode提供了许多辅助函数，使得在BinarySearchTree类方法中
# 完成的工作更加容易。


class TreeNode:
    def __init__(self, key, val, left=None, right=None, parent=None ):
        self.key = key
        self.payload = val
        self.leftChild = left
        self.rightChild = right
        self.parent = parent

    def hasLeftChild(self):
        return self.leftChild

    def hasRightChild(self):
        return self.rightChild

    def isLeftChild(self):
        return self.parent and self.parent.leftChild == self

    def isRightChild(self):
        return self.parent and self.parent.rightChild == self

    def isRoot(self):
        return not self.parent

    def isLeaf(self):
        return not (self.rightChild or self.leftChild)

    def hasAnyChildren(self):
        return self.rightChild or self.leftChild

    def hasBothChildren(self):
        return self.rightChild and self.leftChild

    def replaceNodeData(self, key, value, lc, rc):
        self.key = key
        self.payload = value
        self.leftChild = lc
        self.rightChild =rc
        if self.hasLeftChild():
            self.leftChild.parent = self
        if self.hasRightChild():
            self.rightChild.parent = self

    def findSuccessor(self):
        succ = None
        if self.hasRightChild():
            succ = self.rightChild.findmin()
        else:
            if self.parent:
                if self.isLeftChild():
                    succ = self.parent
                else:
                    self.parent.rightChild = None
                    succ = self.parent.findSuccessor()
                    self.parent.rightChild = self  # 将右边的孩子还给他

    def findmin(self):
        current = self
        while current.hasLeftChild():
            current = current.leftChild
        return current

    def spliceOut(self):
        if self.isLeaf():
            if self.isLeftChild():
                self.parent.leftChild = None
            else:
                self.parent.rightChild = None
        elif self.hasAnyChildren():
            if self.hasLeftChild():
                if self.isLeftChild():
                    self.parent.leftChild = self.leftChild
                else:
                    self.parent.rightChild = self.leftChild
                self.leftChild.parent = self.parent
            else:
                if self.isLeftChild():
                    self.parent.leftChild = self.rightChild
                else:
                    self.parent.rightChild = self.rightChild
                self.rightChild.parent = self.parent


# 实现一下
mytree = BinarySearchTree()
mytree[3] = 'red'
mytree[4] = 'blue'
mytree[6] = 'yellow'
mytree[2] = 'at'

print(mytree[6])
print(mytree[2])




