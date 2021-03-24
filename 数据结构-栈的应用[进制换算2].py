#1,输入二进制数值；2，统计位数，提取每一位数值进行运算；3，递归求和
def MultipelPower():
    num = input("请输入数值：")
    p = int(input("请输入该数值的进制数："))
    length = len(num)
    sum = 0
    n = length - 1
    while n >= 0:
        sum = sum + int(num[length-n-1])*pow(p, n)
        n = n-1
    print(sum)
MultipelPower()