T=int(input())

for test_case in range(1,T+1):
    n,m=map(int(),input().split())
    temp=[list(map(int,input().split())) for i in range(n)]
    result=[]
 
    for i in range(n-m+1):
        for j in range(n-m+1):
            fly=0
            for k in range(i+m):
                for v in range(j+m):
                    fly=fly+temp[k,v]
            result.append(fly)
    print(max(result))







