import random

# lst1 = ["a","b","c","d"]
# statusrunning = 1
# statusstop = 0
# for i in lst1:
#     if i.status == statusrunning:
#         print("running")
#     elif i.status == statusstop:
#         print("stopped")
#     else:
#         print("no status")

#1 to check the number of systems running.
#we can get a count
#2 to check the number of systems stopped.we can get a count
#3 to check the number of systems are in "no status"
#200
#201
#400
#401
#404
#503

# username = "myname"
# password = "mypass"

# dic1 = {"a":"stop","b":"running","c":"running","d":"stop"}
# for i,j in dic1.items():
#     if j == "stop":
#         print(i + ":" + j)

# num = int(input("input the number: "))
# str1 = str(num)
# sum = 0
# for i in str1:
#     sum = sum + int(i)
# print(sum)


# lst1 = [1,2,3,4,5,6]
# first = lst1.pop(0)
# last = lst1.pop(-1)
# lst1.insert(0,last)
# lst1.append(first)
# print(lst1)

# iterable_value = 'Geeks'
# iterable_obj = iter(iterable_value)
# while True:
#     try:
#         # Iterate by calling next
#         item = next(iterable_obj)
#         print(item)
#     except StopIteration:
#         # exception will happen when iteration will over
#         break

# lst1 = [1,2,3,4,5,6,1]
# for i in lst1:
#     if i == 1:
#         lst1.remove(i)
# print(lst1)

# dic1 = {"a":"stop","b":"running","c":"running","d":"stop"}
# del dic1["a"]
# print(dic1)

# lst1 = [1,2,3,4,5,6,1]
# for i in enumerate(lst1):
#     print(i)

# dic1 = {"a":"stop","b":"running","c":"running","d":"stop"}
# for i,j in dic1.items():
#     print(type(i))

# lst1 = [1,2,3,4,5,6]
# first = lst1.pop(0)
# last = lst1.pop(-1)
# lst1.insert(0,last)
# lst1.append(first)
# print(lst1)

# num = int(input("input the number: "))
# lst1 = []
# for i in range(2,num):
#     if num % i == 0:
#         lst1.append(i)
# if len(lst1) == 0:
#     print("prime")
# else:
#     print("not prime")

# lst1 = [1,2,3,4,5,6]
# print(lst1[-1:-4])
list = [1, 2, 1, 2, 3, 4, 5, 1, 1, 2, 5, 6, 7, 8, 9, 9]
new = []
for a in list:
    n = list.count(a)
    if n > 1:
        if new.count(a) == 0:
            new.append(a)
print(new)

