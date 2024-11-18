T = int(input())

for tc in range(1, T + 1):
    n=int(input())
    temp=list(map(int,input().split()))
    orignal=[]
    for i in range(len(temp)):
        x = float(temp[i]/(0.75))
        if x in temp and x % 4==0:
            orignal.append(temp[i])

    sorted_original=sorted(temp)
    print("#{} {}".format(T + 1," ".join(map(str,sorted_original))))            
        
        



    

