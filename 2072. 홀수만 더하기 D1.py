
T = int(input())

for test_case in range(1, T + 1):
    numbers = list(map(int, input().split()))
    ans = sum([x for x in numbers if x % 2 != 0])
    print("#%d %d"%(test_case,ans))
