def chu_yu(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "错误：除数不能为零"

try:
    a,b = input("请输入两个数，用空格隔开：").split()
    a = float(a)
    b = float(b)
    print(chu_yu(a, b))
except ValueError:
    print("错误：输入必须是数字，且需要用空格隔开两个数")