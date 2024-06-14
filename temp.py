T=int(input())

for tc in range(1,T+1):
    n=int(input())

    temp=[1]
    print(1)
    for i in range(n):
        ptemp=temp[:]
        temp.append(1)
        for j in range(1,len(temp)):
            temp[j]=ptemp[j]+ptemp[j-1]
        for v in temp:
            print(v,end="")
        print()














