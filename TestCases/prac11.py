# from collections import Counter
from itertools import groupby
#
# str1 = "test"
# print(Counter(str1))

# dic1 = {"name": "Apratim","add": "GD","company":"riscovry"}
# print(sorted(dic1.values()))

# ccno = 1234567890123456
# ccnos = str(ccno)
# sum = 0
# for i in ccnos[0:4]:
#     sum = sum+int(i)
# if sum == 16:
#     print("VISA")
# else:
#     print("MASTER")

# ccno = "1234 5678 9012 3456"
# lst1 = ccno.split(" ")
# str1 = lst1[0]
# sum = 0
# for i in str1:
#     sum = sum + int(i)
# if sum == 16:
#     print("VISA")
# else:
#     print("MASTER")

series = [0,2, 1, -2, 0, 0, 2, 3 ,1, 7]
count = 0
maxVal = 0
for n in series:
    if n > 0:
        count +=1
        if count > maxVal:
            maxVal = count
    else:
        count = 0
# print(maxVal)
print(max((list(g) for k, g in groupby(series, key=lambda i: i > 0)), key=len))

