
# 표준 출력 예제

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    cnt = 0
    a, b, n = map(int, input().split())
    while(True):
        cnt+=1
        if a>b:
            b+=a
            if b>n:
                break
        else:
            a+=b
            if a>n:
                break
    print(cnt)
