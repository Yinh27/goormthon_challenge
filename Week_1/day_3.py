T = int(input())
result_list = []

for i in range(T):
    x, symbol, y = input().split()
    x = int(x)
    y = int(y)

    if symbol == '+':
        result_list.append(x + y)
    elif symbol == '-':
        result_list.append(x - y)
    elif symbol == '*':
        result_list.append(x * y)
    elif symbol == '/':
        result_list.append(x // y)

print(sum(result_list))
