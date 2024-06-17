T = int(input())

for test_case in range(1, T + 1):
    n=int(input())
    temp=list(map(int,input().split()))
    temp.sort()
     
    print("#"+str(test_case),end=" ")
    for i in temp:
        print(i,end=" ")
    print()