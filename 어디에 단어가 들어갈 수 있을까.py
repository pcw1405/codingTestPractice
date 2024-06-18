def count(arr):
    ret=0
    for i in arr:
        count=0
        for j in range(len(i)):
            if i[j]==1:
                count=count+1
            else:
                if count==k:
                    ret=ret+1
                count=0
    return ret


T=int(input())

for tc in range(1,T+1):
    n,k=map(int,input().split())

    arr=[list(map(int,input().split()))+[0] for _ in range(n)]+[[0]*(n+1)]
    arr_t=list(map(list,zip(*arr)))

    result=count(arr)+count(arr_t)

    print(f'#{tc} {result}')