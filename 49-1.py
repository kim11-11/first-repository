def Fact(n):
    if n==0:
        return 1
    return n * Fact(n-1)

print(Fact(10))