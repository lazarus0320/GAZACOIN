lst = list(range(1, 10001))
wow = []
for i in range(len(lst)):
    for j in str(i):
        i += int(j)
    wow.append(i)
wow.sort()
for i in lst:
    if i not in wow:
        print(i)

        
        
        
# a = [1, 3, 5, 7, 9]
# for i in range(1, 11):
#     if i not in a:
#         print(i)