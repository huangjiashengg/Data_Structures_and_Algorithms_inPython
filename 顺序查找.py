"""
本节定义顺序查找算法代码：
1，顺序查找对象可以是无序的，也可以是有序的；
2，从第一项开始查找直到最后一项，返回值是True以及False
"""
# 第一种，假设查找对象是无序的
def shunxuquery(object, value):
    found = False
    pos = 0
    while pos < len(object) and not found:
        if object[pos] == value:
            found = True
        else:
            pos = pos + 1
    return found

print("顺序查找中的无序查找：", shunxuquery([3,6,9,2,5], 6))

# 第二种，假设查找对象是有序的，并且是从小到达排序的

def shunxu_query(object, value):
    found = False
    stop = False
    pos = 0
    while pos < len(object) and not found and not stop:
        if object[pos] == value:
            found = True
        else:
            if object[pos] > value:
                stop = True
            else:
                pos = pos + 1
    return found

print("顺序查找中的有序查找算法：", shunxu_query([1,2,3,5,6], 3))
