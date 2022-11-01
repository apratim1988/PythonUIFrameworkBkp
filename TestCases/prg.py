from collections import Counter

# letter = "Apratim"
# vowels = "aeiouAEIOU"
# list1 = []
#
# for i in letter:
#     if i in vowels:
#         list1.append(i)
# print(Counter(list1))
#
# sentence = "My Name is Apratim"
# words = sentence.split(" ")
# rev = []
# print(words)
# for i in words:
#     rev.append(i[::-1])
# print(rev)
# revsentence = " ".join(rev)
# print(revsentence)
#
# number = 18
# lst1 = []
# for i in range(2, number):
#     if (number % i) == 0:
#         lst1.append(i)
# if len(lst1) == 0:
#     print("prime")
# else:
#     print("not prime")
#
# number1 = [8,7,9,5,10]
# number1.sort(reverse=True)
# print(number1[1])


# str1 = str(input("input the string: "))
# lst1 = str1.split(" ")
# lst2 = []
# for i in lst1:
#     lst2.append(i[::-1])
# str2 = " ".join(lst2)
# print(str2)

# num = int(input("input the number: "))
# lst1 = []
# for i in range(2,num):
#     if num % i == 0:
#         lst1.append(i)
# if len(lst1) == 0:
#     print("prime")
# else:
#     print("not prime")

# str1 = str(input("input the string: "))
# str2 = str(input("input the string: "))
#
# if sorted(str1,reverse=True) == sorted(str2,reverse=True):
#     print("anagram")
# else:
#     print("not anagram")


# num = int(input("input the number: "))
# sum = 0
# for i in str(num):
#     sum = sum + int(i)
# print(sum)


# lst1 = [1,2,3,4,5,6]
# lst2 = lst1.copy()
# for i in lst2:
#     lst1.remove(i)
# print(lst1)


# str1 = str(input("inpuy the string: "))
# char = "a"
# lst1 = list(str1)
# lst2 = []
# for i in lst1:
#     if i != char:
#         lst2.append(i)
# str2 = "".join(lst2)
# print(str2)

# str1 = str(input("input the character: "))
# if str1.isdigit():
#     print("digit")
# else:
#     print("not")

str1 = "abcde"
str2 = str1.replace("b","1")
print(str2)