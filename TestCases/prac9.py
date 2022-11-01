# str1 = str(input("input the string: "))
# str2 = str1[0:2]+str1[-2:]
# print(str2)


# str1 = str(input("input the string: "))
# fch = str1[0]
# str2 = str1.replace(fch,"6")
# str3 = fch+str2[1:]
# print(str3)

# str1 = str(input("input the string: "))
# print(len(str1))
# if len(str1) == 0:
#     print("provide valid string")
# elif len(str1) <= 3:
#     print(str1)
# else:
#     print(str1 + "ing")

# lst1 = ["test","testing","tst"]
# longest = max(lst1,key=len)
# print(longest)

# str1 = str(input("input the string: "))
# fch = str1[0]
# lch = str1[-1]
# str2 = lch + str1[1:-1] + fch
# print(str2)


# string1 = "abcdef"
# string2 = string1[0::2]
# print(string2)

# lst1 = [1,2,3,4,"a"]
# sum = 0
# for i in lst1:
#     if str(i).isdigit():
#         sum = sum+int(i)
# print(sum)


# """ takes a number"""
# print(__doc__)

# str1 = "abc"
# str2 = "xyz"
# str3 = str1[0:2]+str2[-1] + " " + str2[0:2] + str1[-1]
# print(str3)
a = ["one", "two", "third", "four"]
# max1 = len(a[0])
# temp = a[0]
# for i in a:
#     if (len(i) > max1):
#         max1 = len(i)
#         temp = i
# print(temp,"length is ", max1)
# string1 = "abcdef"
# string2 = string1[0::2]
# print(string2)
# #word count
# str1 = "My name is apratim"
# counts = dict()
# words = str1.split()
# for word in words:
#     if word in counts:
#         counts[word] += 1
#     else:
#         counts[word] = 1
# print(counts)
# #duplicate elements in a string/list
# str1 = "apratim"
# lst1 = list(str1)
# lst2 = []
# for i in lst1:
#     n = lst1.count(i)
#     if n > 1:
#         if lst2.count(i) == 0:
#             lst2.append(i)
# print(lst2)
# lst1 = [1,2,2,3,4,4,5]
# lst2 = []
# for i in lst1:
#     if i not in lst2:
#         lst2.append(i)
# print(lst2)

# str = str(input("input the string: "))
# lst = str.split(" ")
# lst1 = []
# for i in lst:
#     lst1.append(i[::-1])
# str2 = " ".join(lst1)
# print(str2)


a = range(1,11,2)
for i in a:
    print(i)


