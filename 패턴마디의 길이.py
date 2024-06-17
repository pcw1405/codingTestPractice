T=int(input())
for test_case in range(1,T+1):
    temp=input()
    for i in range(1,10):
        if temp[:i] == temp[i:i*2]:
            print("#"+str(test_case)+" "+str(i))
            break

