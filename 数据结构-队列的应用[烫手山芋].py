from 算法与数据结构.Dqueue import Queue
#可以设想一下，将山芋放在最前面，每个孩子在那个位置代表他拿到了山芋，然后出列（代表的是下一个孩子拿到山芋）
def hotpotatos(nameList, num):
    simpleQueue = Queue()
    for name in nameList:
        simpleQueue.enqueue(name)
    while simpleQueue.size() > 1:
        for i in range(num):
            simpleQueue.enqueue(simpleQueue.dequeue())

        simpleQueue.dequeue()
    return simpleQueue.dequeue()
print(hotpotatos(["Jacky","Mukin","Amy","June","Frank","Tony"],30))
