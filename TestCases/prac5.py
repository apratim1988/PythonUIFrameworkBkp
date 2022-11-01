import copy

# #json.dumps method can convert a Python object into a JSON string.
# import json
# dictionary = {
#     "id": "04",
#     "name": "sunil",
#     "department": "HR"}
# json_object = json.dumps(dictionary, indent=4)
# print(json_object)
# #json.dump method can be used for writing to JSON file
# dictionary = {
#     "name": "sathiyajith",
#     "rollno": 56,
#     "cgpa": 8.6,
#     "phonenumber": "9976770500"}
# with open("sample.json", "w") as outfile:
#     json.dump(dictionary, outfile)
# #json.loads method can be used to parse a valid JSON string and convert it into Dictionary
# with open("json_data.json", "r") as content:
#   print(json.loads(content.read()))
# #json.load takes a file object and returns the json object
# with open("/xyz/json_data.json", "r") as content:
#   print(json.load(content))


# mylist=[15,6,7,10,12,10,20,10]
# count = 0
# num = 10
# for i in mylist:
#     if i == num:
#         count = count+1
#
# print(count)

# str1 = "Welcome to python programming"
# str2 = "python"
# count = 0
# lst1 = str1.split(" ")
# for i in lst1:
#     if i == str2:
#         count = count+1
# print(count)

# num = int(input("inpt yhe number: "))
# for i in range(1,11):
#     print(i*num)

# str1 = str(input("input the string: "))
# str2 = str1.title()
# lst1 = str2.split(" ")
# lst2 = []
# for i in lst1:
#     lst2.append(i[0:-1]+i[-1].upper())
# str3 = " ".join(lst2)
# print(str3)


# list1 = [[1,2,3],[4,5,6]]
# list2 = list1.copy()
# list2[0][1] = 100
# print(list1)
# print(list2)


# list1 = [[1,2,3],[4,5,6]]
# list2 = copy.deepcopy(list1)
# list2[0][1] = 100
# print(list1)
# print(list2)


# lst1 = [1,2,3,4,5,6]
# first = lst1.pop(0)
# last = lst1.pop(-1)
# lst1.insert(0,last)
# lst1.append(first)
# print(lst1)

#converting a list into dictionary
# lst = ['a', 1, 'b', 2, 'c', 3]
# res_dct = {lst[i]: lst[i + 1] for i in range(0, len(lst), 2)}
# print(res_dct)

#Method Overloading
# class student:
#     def __init__(self,m1,m2):
#         self.m1 = m1
#         self.m2 = m2
#     def sum(self,a=None,b=None,c=None):
#         s=0
#         if a != None and b != None and c != None:
#             s=a+b+c
#         elif a != None and b != None:
#             s=a+b
#         else:
#             s=a
#         return s
# s1 = student(5,6)
# print(s1.sum(5,6,7))
#
# #Method overriding
# class A:
#     def test1(self):
#         print("test1")
#     def test2(self):
#         print("test2")
# class B(A):
#     def test3(self):
#         print("test3")
#     def test1(self):
#         print("updated test1")

# # obj = B()
# print(obj.test1())

# dict1={0:'1',1:'2',3:[1,2,3]}
# print("Given Dictionary:",dict1)
# #new dictionary
# dict2={}
# for i in dict1:
#     dict2[i]=dict1[i]







