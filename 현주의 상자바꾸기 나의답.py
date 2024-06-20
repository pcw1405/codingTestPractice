T=int(input())

for tc in range(1,T+1):

    N,Q=map(int,input().split())
    temp=[0]*N
    for i in range(1,Q+1):
        L,R=map(int,input().split())

        for v in range(L-1,R):
            temp[v]=i

    # print(f"#{tc}",*temp)    
    print("#"+str(tc),end=" ")

    for j in temp:
        print(j,end=" ")
    #마지막에 띄어쓰기를 안하도록 하니까 정답이 되었다 

