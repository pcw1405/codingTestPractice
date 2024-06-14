
score=['A+','A0','A-','B+','B0','B-','C+','C0','C-','D0']

T=int(input())
for tc in range(1,T+1):
    n,k=map(int(),input().split())
    count=0
    student=[]

    for i in range(n):
        test1,test2,work=map(int(),input().split())
        result=test1*0.35+test2*0.45+work*0.2
        student.append(result)

   
    for j in range(n):
        if score[k-1]<score[j]:
            count=count+1

    print("#"+str(tc),score[count//(n//10)])





