T = int(input())

for tc in range(1, T + 1):
    h, m, h2, m2 = map(int, input().split())

    # 첫 번째 시간을 분으로 변환
    total = h * 60 + m
    # 두 번째 시간을 분으로 변환
    total2 = h2 * 60 + m2

    # 시간 차이를 절대값으로 계산
    totaldif = abs(total - total2)
    hourDif = totaldif // 60
    minDif = totaldif % 60

    print(f"#{tc} 차이는 {hourDif}시간 {minDif}분 입니다")

    # 약간 더 빠르고 가독성 있게