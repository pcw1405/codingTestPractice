T=int(input())

for tc in range(1,T+1):
    N,A,B=map(int,input().split())
    
    if(A>B):
        big=B
    else:
        big=A

    if(A+B>N):
        small=(A+B)-N
    else:
        small=0

    print("#"+str(tc)+" "+str(big)+" "+str(small))