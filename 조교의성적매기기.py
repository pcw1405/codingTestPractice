
temp=['A+','A0','A-','B+','B0','B-','C+','C0','C-','D0']

T=int(input())

for tc in range(1,T+1):

    n,k=map(int,input().split())
    count=0
    score=[]

    for i in range(n):
        a,b,c=map(int,input().split())
        total=a*0.35+b*0.45+c*0.2
        score.append(total)

   
    for j in range(n):
        if score[k-1]<score[j]:
            count=count+1

    print("#"+str(tc),temp[count//(n//10)])





