T=int(input())
 
for test_case in range(1,T+1):
    N,Q=map(int, input().split())
    N_list=[0]*N
 
    for i in range(1,Q+1):
        x,y=map(int,input().split())
        for a in range(x-1,y):
            N_list[a]=i
    print(f"#{test_case}",*N_list)