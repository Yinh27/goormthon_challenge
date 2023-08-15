N = int(input())
T, M = map(int, input().split())

for i in range(N):
	M += int(input())

T = (T + M // 60) % 24
M %= 60

print(f"{T} {M}")

