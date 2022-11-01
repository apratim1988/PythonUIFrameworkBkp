# data = {
# 'Student 1': {'Name': 'Bobby', 'Id': 1, "Age": 20},
# 'Student 2': {'Name': 'Sanvi', 'Id': 2, "Age": 22},
# 'Student 3': {'Name': 'Rohith', 'Id': 3, "Age": 25},
# }
#
# for i,j in data.items():
#     if j["Age"] > 20:
#         print(j["Name"])


# a = [1,2,3,4,5,7]
# b = [2,5,6,7,8]
# c = []
# for i in a:
#     if i in b:
#         c.append(i)
# print(c)

# num = int(input("input the number: "))
# str = str(num)
# lst1 = []
# sum = 0
# for i in str:
#     lst1.append(int(i)*int(i)*int(i))
# for j in lst1:
#     sum = sum + j
# if sum == num:
#     print("its armstrong")
# else:
#     print("not armstrong")

# num1 = int(input("input the number: "))
# str1 = str(num1)
# lst1 = []
# for i in str1:
#     if int(i) == 0 or int(i) == 1:
#         lst1.append(i)
# str2 = "".join(lst1)
# if str1 == str2:
#     print("binary")
# else:
#     print("not binary")

a = 10
b = 20
c = a
a = b
b = c

# num = int(input("input the number: "))
# lst1 = []
# sum = 0
# for i in range(1,num):
#     if num % i == 0:
#         lst1.append(i)
# for j in lst1:
#    sum = sum + j
# if sum == num:
#     print("perfect")
# else:
#     print("not perfect")


# num = int(input("input the number: "))
# fact = 1
# for i in reversed(range(1,num+1)):
#     fact = fact*i
# print(fact)

# num = int(input("input the number: "))
# result = 1
# exponent = num
# for i in range(exponent,0,-1):
#     result *= num
# print(result)

# str1 = "apratim"
# str2 = str1.replace("p","")
# print(str2)

# lst1 = [1,2,3,4,5,6,7,8,9,10]
# lst2 = [i for i in lst1 if i % 2 == 0]
# print(lst2)

# str1 = str(input("input string1: "))
# str2 = str(input("input string2: "))
#
# if sorted(str1) == sorted(str2):
#     print("anagram")


