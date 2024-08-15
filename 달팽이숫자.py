T=int(input())

for tc in range(1,T+1):
    N=int(input())

    board=[ [0] * N for _ in range(N)]

    dy=[-1,0,1,0]
    dx=[0,1,0,-1]

    d=1
    y=x=0
    num=1
    
    for _ in range(N*N):
        board[y][x]=num
        num +=1
        y=y+dy[d%4]
        x=x+dx[d%4]

        if x < 0 or y <0 or x >= N or y >= N or board[y][x] != 0:
            y = y - dy[d%4]
            x = x - dx[d%4]
  
            d += 1
  
            y = y + dy[d%4]
            x = x + dx[d%4]

    print(f'#{tc}')

    for lst in board:
        print(*lst)