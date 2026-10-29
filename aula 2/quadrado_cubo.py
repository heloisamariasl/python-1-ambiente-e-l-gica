N = int(input())

if N > 1 and N < 1000:
    for i in range(1, N + 1):
        print(f"{i} {i*i} {i*i*i}")
