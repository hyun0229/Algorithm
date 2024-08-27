
T = int(input())

for test_case in range(1, T + 1):
    n = int(input())
    numbers = list(map(int, input().split()))
    a = 0
    ans = 0
    for x in reversed(numbers):
        if x>a:
            a=x
        else :
            ans += a-x
    print("#%d %d"%(test_case,ans))
        