"""
本节定义二分法查找算法：
1，二分法查找针对的查找对象是有序的；
2，二分查找同样返回布尔值；
"""

def erfenquery(object, value):
    first = 0
    last = len(object) - 1
    found = False
    while first <= last and not found:
        midpoint = (first + last) // 2
        if midpoint == value:
            found = True
        else:
            if midpoint < value:
                first = midpoint + 1
            else:
                last = midpoint - 1
    return found

print(erfenquery([1,2,3,4,5,6,7,8], 5))

# 下面展示一个递归版本
def erfen_query(alist, value):
    if len(alist) == 0:
        return False
    else:
        midpoint = len(alist)//2
        if value == alist[midpoint]:
            return True
        else:
            if value < alist[midpoint]:
                return erfen_query(alist[:midpoint], value)
            else:
                return erfen_query(alist[midpoint+1:], value)
print("递归版本：", erfen_query([1,2,3,4,5,6,7,8], 11))
