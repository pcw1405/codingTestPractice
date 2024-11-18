T = int(input())

for tc in range(1, T + 1):
    n=int(input())
    temp=list(map(int,input().split()))
    price=[]

    for i in range(len(temp)):
        x = int(temp[i]/(0.75))
        if x in temp and x % 4==0:
            price.append(temp[i])

    sorted_price=sorted(set(price))
    print("#{} {}".format(tc," ".join(map(str,sorted_price))))            
        
        



    

