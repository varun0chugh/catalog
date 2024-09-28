def summ(n):
    if n==1:
        return 1
    return n+summ(n-1)
n=5
print(summ(n))