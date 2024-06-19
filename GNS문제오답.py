number=["ZRO","ONE","TWO","THR","FIV","SIX","SVN","EGT","MIN"]

T=int(input())

for tc in range(1,T+1):

    new_list=[]
    print("#"+str(tc),end=" ")

    n=int(input())
    
    temp=list(input().split())
    
    for i in range(len(temp)-1):
        for j in range(i+1,len(temp)):
            index = number.index(temp[i])
            index2 = number.index(temp[j])
            if(index>index2):
                temp[i],temp[j]=temp[j],temp[i]

    for v in temp:
        print(v,end=" ")

        # 어떻게 하면 더 빠르게 정렬할 수 있는지 찾아본다 
            

    

        
