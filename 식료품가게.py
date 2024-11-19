T = int(input())

for tc in range(1, T + 1):
    n=int(input())
    temp=list(map(int,input().split()))
    price=[]

    for i in range(len(temp)):
        original_price=temp[i]/0.75

        if original_price%4 ==0 and original_price in temp:
            price.append(temp[i])
            temp[temp.index(original_price)]=-1
    price.sort()
    print("#{} {}".format(tc," ".join(map(str,price))))            
        
        



    

