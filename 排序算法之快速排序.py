"""
快速排序依然采用分而治之的做法，运用递归的思想：
1，寻找分割点，使得分割点左边的点小于分割点，右边的点大于分割点
2，不断重复上诉的步骤
"""

def kuaisu_sort(alist):
    kuaisu_sorthelp(alist, 0, len(alist)-1)
    return alist

def kuaisu_sorthelp(alist, first, last):
    if first < last:
        splitpoint = partition(alist, first, last)

        kuaisu_sorthelp(alist, first, splitpoint-1)
        kuaisu_sorthelp(alist, splitpoint+1, last)

def partition(alist, first, last):
    leftmark = first + 1
    rightmark = last
    done = False

    while not done:
        while leftmark <= rightmark and alist[leftmark] <= alist[first]:
            leftmark = leftmark + 1
        while leftmark <= rightmark and alist[rightmark] >= alist[first]:
            rightmark = rightmark - 1

        if leftmark > rightmark:
            done = True
        else:
            temp = alist[rightmark]
            alist[rightmark] = alist[leftmark]
            alist[leftmark] = temp

        temp = alist[rightmark]
        alist[rightmark] = alist[first]
        alist[first] = temp
    return rightmark

print(kuaisu_sort([4,7,1,0,3]))




