t=int(input())

for tc in range(1,t+1):
    l,u,x=map(int,input().split())

    need=0

    if x>u:
        need=-1
    elif l>x:
        need=l-x

    print("#")
