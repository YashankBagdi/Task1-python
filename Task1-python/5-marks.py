n=int(input('Enter number of students: '))
d={}
for i in range (1,n+1):
    l=[]
    l2=[]
    print('Enter name of student ',i, ': ', end=' ')
    name=input()
    print('Enter 3 marks for ',name,' separated by space: ',end=' ')
    marks=input()
    l=marks.split()
    for i in l:
        b=int(i)
        l2.append(b)
        d[name]=l2
it=list(d.keys())   
l3=[]
for i in d:
    s=sum(d[i])
    l3.append(s)
    av=(sum(d[i]))/3.0
    print(i,': Total = ',s,', Average = ',av)
m=max(l3)
ind=l3.index(m)
print('Topper: ',it[ind],'with',m,'marks.')




