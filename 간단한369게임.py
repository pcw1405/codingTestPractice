n=int(input())
clap=['3','6','9']

for i in range(1,n+1):
    count=0
    for j in str(i):
        if j in clap:
            count=count+1
    if count==0:
        print(i,end=" ")
    else:
        print("-"*count,end=" ")
        

    
    

