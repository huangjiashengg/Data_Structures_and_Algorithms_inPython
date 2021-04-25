"""
归并排序总共有两个过程：
1，拆分；
2，合并。
"""

def mergesort(alist):
    print("切分...")
    if len(alist) > 1:
        splitepoint = len(alist)//2
        lefthalf = alist[:splitepoint]
        righthalf = alist[splitepoint:]

        mergesort(lefthalf)
        mergesort(righthalf)

        i = 0
        j = 0
        k = 0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k] = lefthalf[i]
                i = i + 1
            else:
                alist[k] = righthalf[j]
                j = j + 1

            k = k + 1
        while i < len(lefthalf):
            alist[k] = lefthalf[i]
            i = i + 1
            k = k + 1
        while j < len(righthalf):
            alist[k] = righthalf[j]
            j = j + 1
            k = k + 1
    print("合并...")
    return alist

print(mergesort([5,2,9,3,7]))