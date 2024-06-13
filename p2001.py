T=int(input())

for test_case in range(1,T+1):
    n,m=map(int,input().split())
    temp=[list(map(int,input().split())) for i in range(n)]

    result=[]
    for i in range(n-m+1):
        for j in range(n-m+1):
            fly=0
            for k in range(m):
                for l in range(m):
                    fly=fly+temp[i+k][i+l]
                result.append(fly)
    
    print("#"+str(test_case),max(result))

