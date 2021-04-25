"""
本节实现选择排序算法：
1，排序对象为无需排序列表，输出对象为排序后的列表（从小到大）；
2，选择排序是先找到最大值，放在合适的位置；其次再找出次大值，放在合适的位置，往复循环；
"""

def selectsort(alist):
    for index in range(len(alist)-1, 0, -1):
        maxposition = 0
        for position in range(1, index+1):
            if alist[position] > alist[maxposition]:
                maxposition = position
        temp = alist[index]
        alist[index] = alist[maxposition]
        alist[maxposition] = temp
    return alist

print(selectsort([5,2,9,4]))