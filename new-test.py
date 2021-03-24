# import itertools
# list = ['h', 'e', ':', 'l', 'l', 'o']
# s = "".join(itertools.chain(*list))
# sh = s.strip().split(':')
# print(s)

# import PySimpleGUI as sg
# import time
#
# mylist = range(10000)
# for i, item in enumerate(mylist):
#     sg.one_line_progress_meter('This is my progress meter!', i+1, len(mylist), '-key-')
# time.sleep(1)

# from time import sleep
# from tqdm import tqdm
#
# # 这里同样的，tqdm就是这个进度条最常用的一个方法
# # 里面存一个可迭代对象
# for i in tqdm(range(1, 500)):
#    # 模拟你的任务
#    sleep(0.1)


