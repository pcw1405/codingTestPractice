def get_month(a):
    sum1=0
    for i in range(1,a):
        if i==2:
            sum1=sum1+28
        elif i<8 and i%2!=0:
            sum1=sum1+31
        elif i<8 and i%2==0:
            sum1=sum1+30
        elif i>7 and i%2!=0:
            sum1=sum1+30
        elif i>7 and i%2==0:
            sum1=sum1+31
    return sum1
     
     
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    m1,d1,m2,d2=map(int,input().split())
     
    temp=get_month(m1)+d1
    temp2=get_month(m2)+d2
     
    print("#"+str(test_case),temp2-temp+1)
     
     