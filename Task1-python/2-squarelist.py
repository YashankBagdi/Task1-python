n=int(input("how many numbers: "))
print('enter numbers: ')
l=[]
for i in range(n):
    j=int(input())
    l.append(j)
print(l)
lsq=[]
for i in l:
    p=i*i
    lsq.append(p)
print('square of each number is: ')
print(lsq)
    
    
