# N, X = map(int, input().split(" "))
# A = list(map(int, input().split(" ")))
# answer = [str(i) for i in A if i<X]
# print(' '.join(answer))

from numpy import average


n = int(input())
sum = 0
a = list(map(int, input().split()))
for i in range(n):
    print(a[i])
    sum += (a[i] / max(a) * 100)
print(sum/n)
# lst = [1, 2, 3, 4, 1, 2, 3, 4, 4, 4]
# a = []
# for i in range(len(lst)):
#     a.append(lst.count(lst[i]))
# print(a.count(max(a)))

        