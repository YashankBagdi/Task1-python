def fact(n):
    res=1
    if n==0:
        return 1
    elif n==1:
        return 1
    res = res * (fact(n-1))
    return res
n=int(input("Enter number: "))
print(fact(n))
