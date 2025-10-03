def is_prime(n):
    count =0
    for i in range(2,n):
        if (n%i==0):
            count=1
            break
    if (count==1):
        print('Not prime')
    else:
        print('Prime')

n=int(input('Enter number: '))
is_prime(n)
