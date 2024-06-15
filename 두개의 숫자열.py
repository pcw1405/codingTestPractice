T=int(input())

for tc in range(1,T+1):
    n,m=map(int(input().split()))
    temp1=list(map(int,input().split()))
    temp2=list(map(int,input().split()))

    if n>m:
        n,m=m,n
    if len(temp2)<len(temp1):
        temp1,temp2=temp2,temp1

    max1=0
    for i in range(m-n+1):
        total=0
        for j in range(n):
            sum1=temp2[i+j]*temp1[j]
            total=total+sum1
        max1=max(max1,total)
    print("#"+str(tc),max1)
