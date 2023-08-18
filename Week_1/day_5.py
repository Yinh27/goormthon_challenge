N, K = map(int, input().split())
a = list(map(int, input().split()))

sorted_list = sorted(a, key=lambda x: (-bin(x).count('1'), -x))

print(sorted_list[K - 1])
