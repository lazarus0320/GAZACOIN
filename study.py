M = int(input())
N = M
i = 0
while True:
    num1 = M // 10
    num2 = M % 10
    num3 = (num1 + num2) % 10
    M = (num2 * 10) + num3
    i += 1
    if M == N:
        print(i)
        break
    