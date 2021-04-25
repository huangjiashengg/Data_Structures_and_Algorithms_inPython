"""
1，插入排序输入对象是无序列表，输出对象是有序列表；
2，所谓插入排序，是指不断往子列表添加新元素的一种方法，体现分而治之的一种方法；
3，最终实现整个列表的排序
"""

def insertsort(alist):
    for index in range(1, len(alist)):
        temp = alist[index]
        position = index
        while position > 0 and alist[position-1] > temp:
            alist[position] = alist[position-1]
            position = position - 1
        alist[position] = temp
    return alist
print(insertsort([8,3,5,1]))