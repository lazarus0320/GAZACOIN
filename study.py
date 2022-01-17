num = int(input())
lst = []
for i in range(num):
    s = int(input())
    lst.append(s)
new_lst = []
for i in range(num):
    new_lst.append(lst[i] / max(lst) * 100)
print(float(sum(new_lst))/num)
    
