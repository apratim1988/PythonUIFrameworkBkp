# list = [1, 2, 1, 2, 3, 4, 5, 1, 1, 2, 5, 6, 7, 8, 9, 9]
# new = []
# for a in list:
#     n = list.count(a)
#     if n > 1:
#         if new.count(a) == 0:
#             new.append(a)
# print(new)
#
# iterable_value = 'Geeks'
# iterable_obj = iter(iterable_value)
# while True:
#     try:
#         item = next(iterable_obj)
#         print(item)
#     except StopIteration:
#         break
#
# a = range(1,10)
# b = []
# for num in a:
#     if all(num % i !=0 for i in range(2,num)):
#         b.append(num)
# print(b)


# str1 = str(input("input the string: "))
# str2 = str1.title()
# str3 = str2[0:-1]+str2[-1].upper()
# print(str3)

# a = range(1,10,2)
# for i in a:
#     print(i)