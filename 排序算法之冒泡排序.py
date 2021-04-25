"""
本节实现冒泡排序的算法：
1，排序针对对象是无序列表，输出对象是有序列表（c从小到大）
2，所谓冒泡，即将每次遍历排序得到的最大值排除在外；
3，冒泡排序有两层遍历
"""

def maopaosort(alist):
    for index in range(len(alist)-1, 0, -1):
        for position in range(index):
            if alist[position] > alist[position+1]:
                temp = alist[position]
                alist[position] = alist[position+1]
                alist[position+1] = temp
    return alist

print(maopaosort([5,3,8,1]))