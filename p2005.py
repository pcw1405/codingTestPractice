

T=int(input())

for tc in range(1,T):
    n=int(input())

    temp=[1]
    print(1)
    for i in range(1,n):
        ptemp=temp[:]
        temp.append(1)
        for j in range(1,len(temp)-1):
            temp[j]=ptemp[j-1]+ptemp[j]
        for v in temp:
            print(v,end=" ")
        print()






        




