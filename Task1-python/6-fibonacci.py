def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)
k=int(input("How many numbers: "))
for i in range(k):
    print(fibonacci(i), end=' ')
