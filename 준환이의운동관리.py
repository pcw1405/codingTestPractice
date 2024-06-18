T=int(input())

for tc in range(1,T+1):
    L,U,X=map(int,input().split())

    need=0

    if X>U:
        need=-1
    elif L>X:
        need=L-X

    print("#"+str(tc)+" "+str(need))
    
    
