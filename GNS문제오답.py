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
        # cost비용 
# 선택 정렬은 비효율적인 정렬 알고리즘이며, 최악의 경우 O(N^2)의 시간 복잡도를 가집니다.
# 특히 입력 데이터가 많아지면 처리 속도가 급격히 느려질 수 있습니다.
            
#더 빠르고 효율적인 정렬 알고리즘인 계수 정렬(counting sort)이나 
#병합 정렬(merge sort) 등을 적용하지 않아서 성능이 저하될 수 있습니다.

    

        
