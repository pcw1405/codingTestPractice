T=int(input())

for tc in range(1,T+1):
    D,L,N=map(int,input().split())
    result=0
    for i in range(N):
        result += D * (1 + i * L/100)
        

    print("#"+str(tc)+" "+str(int(result)))

