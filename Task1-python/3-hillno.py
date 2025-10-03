def is_hill_number(n):
    l=[]
    for i in n:
        l.append(i)
    p=len(l)
    m=l.index(max(l))
    if (m==0):
        print('No')
    elif (m==p-1):
        count=0
        for k in range(p-2):
            if (l[k]>l[k+1]):
                count=1
                break
        if (count==1):
            print('No')
        else:
            print('Yes')
    else:
        ck=1
        for c in range(m-1):
            if l[c]>l[c+1]:
                ck=0
                break
        if (ck==1):
            newck=1
            for t in range(m+1,p-1):
                if (l[t]<l[t+1]):
                    newck=0
                    break
            if (newck==0):
                print('No')
            else:
                print('Yes')
        else:
            print('No')

n=input('Enter a number: ')
is_hill_number(n)
                
                
        
                
