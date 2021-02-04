import datetime
print("Hello World")
# a=str("123")
# A=int(1234)
# print(a)
# print(a[0])
# print(a[1])
# print(a[2])

# x, y, z = "Orange", "Banana", "Cherry"
# print(x)
# print(y)
# print(z)
# def funcion():
#     global x
#     x="aaaaa"
#     print(x+y+z)
# funcion()
# print("124",type(x))

#

# lish=["1","2","3"]
# print(lish)
# print(lish[0])
# print(lish[1])
# print(lish[2])
# print(len(lish))

# lish=["a","b","c","d"]
# # for l in range (len(lish)):
# #     print(lish[l])
# # for l in lish:
# #     print(l)

# a=10
# print(a**10)

# a=range(10)
# for i in a:
#     print(i)

# lish=["a","b","c","d"]
# i=0
# while i<len(lish):
#     print(lish[i])
#     i=i+1

# thislist = ["apple", "banana", "cherry"]
# [print(x) for x in thislist]

# list=["1","2","3","4"]
# list1=[]
# for l in list:
#     if int(l)<4:
#         list1.append(l)
# print(list1)

# list=["1","2","3","4"]
# list1=[x for x in list if int(x) < 3]
# print(list1)

# list=["1","4","3","2"]
# list.sort(reverse = True)
# print(list)

# def myfunc(n):
#   return abs(n - 50)
#
# thislist = [100, 50, 65, 82, 23]
#
# thislist.sort(key = myfunc)
#
# print(thislist)

# list=["1","a","3","2"]
# list1=list.copy()
# print(list1)

# list1 = ["a", "b", "c","a"]
# list2 = [1, 2, 3]
# list3 = list1 + list2
# print(list1.count("a"))

# t=("1","2","3")
# print(type(tuple))
# list=list(t)
# list[0]="5"
# t=tuple(list)
# print(t)

# thisset = set(("1", "2", "3"))
# print(thisset)

# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# if "model" in thisdict:
#   print("Yes, 'model' is one of the keys in the thisdict dictionary")

# def say(message, times=1):
#     print(message+times)
#
# say('Hello',"qqqq")
# say('World', "123")


# def myfunc(n):
#   return lambda a : a * n
#
# mydoubler = myfunc(2)
#
# print(mydoubler(111))


# class MyClass:
#   def __init__(self,name):
#     self.name=name
#
#   x = 10
#   def m(self,a,b,c):
#       return a*b*c*10
#
# p1 = MyClass(12)
# print(p1.m(10,11,10))

# class Person:
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age
#
# p1 = Person("John", 36)
#
# print(p1.name)
# print(p1.age)

# for i in range(1,20,):
#     print(i,end='')

# sequence = ['p', 'a', 's', 's']
# for val in sequence:
#     print(val)
#     pass
#     print("ass")

# def outerFunction():
#     global a
#     a = 50
#
#     def innerFunction():
#         global a
#         a = 30
#         print('a =', a)
#     innerFunction()
#
#
# a = 10;
# outerFunction()
# print('a =', a)

# x = datetime.datetime.now()
# print(x)
# print(x.year)
# print(x.month)
# print(x.day)
# print(x.hour)
# print(x.minute)
# print(x.second)
# print(x.microsecond)
