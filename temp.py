T=int(input())

for tc in range(1,T+1):
    h,m,h2,m2=map(int,input().split())


    if(h>=h2):
        h=h
    else:
        h2,h=h,h2

    total=m+h*60
    total2=m2+h2*60

    totaldif=total-total2
    hourDif=totaldif//60
    minDif=totaldif%60

    print("#"+str(tc)+"차이는"+str(hourDif)+"시간"+str(minDif)+"분 입니다")




    




















