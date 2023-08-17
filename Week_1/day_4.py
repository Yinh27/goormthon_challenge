N = int(input())
K = list(map(int, input().split()))

up = K[0:K.index(max(K))]
down = K[K.index(max(K)):]

result = 0

if up == sorted(up):
	result += sum(up)
	if down == sorted(down, reverse=True):
		result += sum(down)
		print(result)
	else:
		print(0)
else:
	print(0)
    