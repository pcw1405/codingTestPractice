number = ["ZRO", "ONE", "TWO", "THR", "FIV", "SIX", "SVN", "EGT", "MIN"]
number_index = {word: idx for idx, word in enumerate(number)}

T = int(input())

for tc in range(1, T + 1):
    # 케이스 번호와 테스트 케이스 길이를 읽습니다. 테스트 케이스 길이는 실제로 필요하지 않습니다.
    _, n = input().split()
    n = int(n)
    
    # 테스트 케이스 데이터를 읽습니다.
    temp = input().split()
    
    # 카운팅 배열 초기화
    count = [0] * len(number)
    
    # 각 단어를 카운트
    for word in temp:
        count[number_index[word]] += 1
    
    # 결과 출력
    print(f"#{tc}")
    for idx, cnt in enumerate(count):
        print((number[idx] + " ") * cnt, end="")
    print()  # 줄바꿈