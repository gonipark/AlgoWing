t=int(input())

bi=[]
for i in range(12) :
    bi.append(2**-(i+1))

for tc in range(t) :
    n=float(input())
    a=0
    ch=0
    l=[]
    for i in range(12) :
        if(a+bi[i]>n) :
            l.append(0)
            continue
        else :
            a+=bi[i]
            l.append(1)
            if(a==n) :
                ch=1
                break
    print('#%d'%(tc+1), end=' ')
    if(ch==0) :
        print('overflow')
    else :
        for i in l :
            print(i, end='')
        print()