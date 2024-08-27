
T = 10

for test_case in range(1, T + 1):
    n = int(input())
    numbers = list(map(int, input().split()))
    ans=0
    for x in range(2, n-2):  # 인덱스 범위 확인 (2, n-2)
        diff1 = numbers[x] - numbers[x-2]
        diff2 = numbers[x] - numbers[x-1]
        diff3 = numbers[x] - numbers[x+1]
        diff4 = numbers[x] - numbers[x+2]
        
        min_a = min(diff1, diff2, diff3, diff4)
        if min_a > 0 : ans += min_a

    print("#%d %d"%(test_case,ans))