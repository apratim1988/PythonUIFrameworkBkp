import random
import copy
# lst1 = [1,2,3,4,4,5,6,5]
# lst2 = []
# for i in lst1:
#     if i not in lst2:
#         lst2.append(i)
# print(lst2)

# lst1 = [1,2,3,4,4,5,6,5]
# print(lst1.count(4))

# lst1 = [1,2,3,4,4,5,6,5]
# lst2 = []
# for i in lst1:
#     if lst1.count(i) > 1:
#         lst2.append(i)
# print(set(lst2))

# a = [1, 2, 3]
# print(a[-3])

# a = [1,2,3,4,5,6]
# print(random.choice(a))

# a = range(1,101)
# sum = 0
# for i in a:
#     sum = sum+i
# print(sum)

# a = [1,2,3,4,5,6,7]
# print(a[:])
# leng = len(a)
# sum = 0
# for i in a:
#     sum = sum + i
# print(sum)
# avg = sum/leng
# print(avg)

# num = int(input("input the number: "))
# str1 = str(num)
# print(str1[::-1])

# num = int(input("input the number: "))
# str1 = str(num)
# lst1 = list(str1)
# print(len(lst1))

# num = int(input("input the number: "))
# a = range(1,11)
# for i in a:
#     print(num,"x", i, "=", i*num)

# num = int(input("input the number: "))
# lst1 = []
# for i in range(2,num):
#     if num % i == 0:
#         lst1.append(i)
# if len(lst1) == 0:
#     print("prime")
# else:
#     print("not prime")

# num = int(input("input the number: "))
# str1 = str(num)
# sum = 0
# for i in str1:
#     sum = sum + int(i)**3
# if sum == num:
#     print("armstrong")
# else:
#     print("not armstrong")


# num = int(input("input the number: "))
# lst1 = []
# for i in range(1,num):
#     if num % i == 0:
#         lst1.append(i)
# sum = 0
# for j in lst1:
#     sum = sum+j
# if sum == num:
#     print("perfect")
# else:
#     print("not perfect")


# lst1 = [1,2,3,4,5,6,0]
# first = lst1.pop(0)
# last = lst1.pop(-1)
# lst1.insert(0,last)
# lst1.append(first)
# print(lst1)


# str1 = str(input("input the string: "))
# vowels = "aeiouAEIOU"
# lst1 = []
# for i in str1:
#     if i in vowels:
#         lst1.append(i)
# print(len(lst1))

# lst1 = [[1,2,3,4],[5,6,7,8]]
# lst2 = lst1.copy()
# # lst2 = copy.deepcopy(lst1)
# lst1[0][0] = 100
# print(lst1)
# print(lst2)

# num = int(input("input the number: "))
# lst = []
# for i in range(2,num):
#     if num % i == 0:
#         lst.append(i)
# print(lst)
# if len(lst) == 0:
#     print("prime")
# else:
#     print("not prime")


# str = "test"
# str2 = str.replace("e","a")
# print(str2)

# a = [1,2,3,4,5,6,7]
# print(a[:])

# num = int(input("input the number: "))
# lst1 = []
# for i in range(1,num):
#     if num % i == 0:
#         lst1.append(i)
# print(lst1)

# x = lambda a,b : a+b
# print(x(2,3))

dic = {"otp": "495537"}
print(dic["otp"])