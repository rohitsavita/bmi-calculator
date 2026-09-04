#print("start learning python on 11/07/2026 12pm")
'''a="12"numerical value use when str convert in int or float 
a=int(a)
print (type(a))'''
"""a="11"
a=float (a)
print (type(a))"""
 
#false valuse always give result false 
"""1.False
2.0
3.0.0
4." "
5.[]
6.()
7.{}
"""
"""formating string """
'''name ="rohit"
age="23"
print("hello my name is",name,"and my age is ",age)
print(f"my name is {name} and my age is {age}")'''
# age=int(input("my age is "))
# price=float(input("food price is"))
# name=str(input("my name is"))
# items=list(input())

# print(age)
# print(name)
# money=int(input("please provive amount of:"))
# if money==10:
#     print("purchase toy")
# elif money==20:
#     print("purchase phone")
# elif money == 30:
#     print("purchase laptop")        
# else :
#     print("prchase car")    
# num1=int(input("tell me your first number"))
# num2=int(input("tell me your second number"))
# if num1>num2:
#     print(f"{num1} is grater than {num2}")  
# elif num2>num1:
#     print(f"{num2} is greater than {num1}")    
# else:
#     print(f"both the number ar same")  
"""gen=input("tell me your gender M or f: ")
if gen=="M" or gen=="m":
    print("hello sir")
elif gen=="F" or gen=="f":
    print("hello mam")
else :
    print("gender is not defined ")"""
# num=int(input("tell me your number:"))
# if num%2==0:
#     print("even bumber ")
# else:
#     print("number is odd")    
"""num = int(input("Enter a number: "))
if num<=1:
    print("number is not prime ")
else:
    for i in range (2,num):
        if num % i==0:
            print("not a prime number")
            break
    else:
        print("prime number")"""
# name=input("tell me your name:")
# age=int(input("tell me your age:"))
# if age>=18:
#     print(f"hello {name} you are valid voter")
# else:
#     year_left=18-age
#     print(f"{name} you are not valid voter")    
#     print(f"you can vote after {year_left} year")
# year=int(input( "tell me year "))
# if year%100==0 and year %400==0:
#     print("year is leap year ")
# elif year%100!=0 and year %4==0:  
#     print("it is a leap year ")  
# else:
#     print("year is not leap year ")    
# year=int(input("tell me year:"))
# if year%4==0:
#     print("it is a leap year")
# else:
#     print("it is not leap year ")   
# year = int(input("Enter a year: "))

# if year % 400 == 0:
#     print("Year is a leap year.")
# elif year % 100 == 0:
#     print("Year is not a leap year.")
# elif year % 4 == 0:
#     print("Year is a leap year.")
# else:
#     print("Year is not a leap year.")


#CORRECT 
# year = int(input("Tell me the year: "))

# if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#     print("Year is a leap year.")
# else:
#     print("Year is not a leap year.")

# n=int(input("which table you want:"))
# for i in range(n,n*10+1,n):
#     print(i)
# # for i in range(5,50,5):
# #     print(i)  
# for i in range(1,21):
#     if i==15:
#      print("BREAK STATEMENT IS EXECUTED")
#      break
#     print(i)
# else:
#    print("break statement is not executed")    
# n=int(input("enter your number:-")) 
# for i in range(n):
#     print("rohit kumar savita") 

# n=int(input("enter your number:-"))
# for i in range(n,0,-1):
#     print(i)
# n=int(input("enter number for table"))
# for i in range(n,(n*10)+1,n):
#     print(i)
# n=int(input("enter number for table: "))
# for i in range(1,11):
#     print(f"{n} * {i} = {n*i}")
# n=int(input("sum of number upto n term:"))
# sum =0
# for i in range(1,n+1):
#     sum=sum+i
# print(f"your sum is  {sum}")
# n=int(input("your number:"))
# fact  = 1
# for i in range(1,n+1):
#     fact=fact*i
# print(f"your factorial is  {fact}")
# n=int(input("tell your number: "))
# even=0
# odd=0
# for i in range(1,n+1):
#     if i%2==0:
#         even = even + i
#     else:
#         odd =  odd + i    
# print(f"your even and odd sum are {even},{odd}")        
# n=int(input("which number factor you want:"))
# for i in range(1,n+1):
#     if n%i==0:
#         print(i)
# n=int(input("check your number is perfect or not:"))
# sum=0
# for i in range(1,n):
#     if n%i==0:
#         sum=sum+i
# if sum==n:
#     print("number is perfect")
# else :
#     print("not perfect")  
# n=int(input("check your number is prime or not"))
# count=0
# for i in range(1,n+1):
#     if n%i==0:
#           count=count+1
  
# if count == 2:
#     print("prime number")
# else:
#     print("not prime number")    
# a=input("enter a string: ")
# if a==a[::-1]:
#     print("palindrome")
# else:
#     print("not a palindrome")
# a=int(input("enter your number: "))
# while a > 0:
#     print(a%10)
#     a=a//10
# a=int(input("tell your number "))
# rev=0
# while a>0:
#     rev=rev*10 + a%10 
#     a=a//10
# print(rev) 
# a=int(input("tell your number "))
# copy=a
# rev=0
# while a>0:
#     rev=rev*10 + a%10 
#     a=a//10
# if copy ==rev:
#     print("pallindrom number")
# else:
#     print("not pallindrom number")    

# import random
# num=random.randint(1,10)
# tries=0
# while True:
#     guess=int(input("please guess your number "))

#     if num==guess:
      
#       print(f"you are right you guessed  the number is {tries} tries ")
#       tries +=1
#       break

#     elif num< guess:
#         print("go to little lower ")
#         tries +=1

#     elif num > guess:
#         print("go to little higher  ")
#         tries +=1


#     else :
#         tries +=1
#         print("you are wrong")
        

# def sum(a,b):
#     print(f"sum of your number is {a+b}")
# sum(4,8)    
# sum(67,99)

# def add(a,b):
#     return a +b
# print(add(3,4))

# def hello(name,age):
#     print(f" your name is {name} and your age is {age}")
# hello(name="rohit",age=24)

# a=input("enter a string: ")
# def  pallindrome(st):
#     if st==st[::-1]:
#      print(f"{st} pallindrome")
#     else:
#      print(f"{st} not a pallindrome")

# pallindrome("naman")     
# pallindrome("rohit")     

# def hello():
#     return "hello rohit"
# print(hello())
# def hello(name):
#     print(f"hello,{name}!")
# hello("rohit")    

# a=[1,3,2,6,7,9,7]

# for i in range (len(a)):
#     print(a[i])
# print(dir(list))
# number=["banana","apple","orange"]
# x=number.index("banana")
# print(x)

# a=[1,8,7,9,2,3,4,5,5,5,6,7]
# # number=number.count(5)
# # print(number)
# number.reverse()
# print(number)
# b=a.copy()
# c=a.copy()
# print(a)
# print(b)
# print(c)
# a.clear()
# print(a)

# l=[12,12,24,15,27,18,5,9,-22,-44,-45]
# print("positive elements are:")
# for i in l:
#     if i>=0:
#           print(i)
# print("neagtive elements are:")  
# for i in l:
#      if i<=0:
#           print(i)     
# print("dublicate elements ")    
# for i in l:
#      if l.count(i)>1:
#           print(i)
# l=[20,30,60,40,50]
# print(sum(l))
# print(sum(l)/len(l))
# sum =0
# for i in l:
#     sum =sum +i
# print (sum/len(l))    
# l=[200,560,400,320,420]
# largest=l[0]
# index=0
# for i in range(len(l)):
#     if l[i]>largest:
#         largest=l[i]
#         index=i
# print(f"largest numbes is {largest} at index {index}")  
      
# l=[10,20,40,90,25,75,80,200,150]
# largest=l[0]
# largest_index=0
# sec_largest=l[0]
# sec_largest_index=0
# for i in range(len(l)):
#     if l[i]>largest:
#         sec_largest=largest
#         largest=l[i]
#         largest_index=i
#     elif l[i]>sec_largest:
#         sec_largest=l[i] 
#         sec_largest_index=i   

# print(f"largest number is {largest} at index {largest_index}")
# print(f"sec_largest number is {sec_largest} at index {sec_largest_index}")

# l=[200, 560, 400, 320, 420]
# largest=l[0]
# sec_largest=l[0]
# for i in l:   
#     if i>largest:
#         sec_largest=largest
#         largest=i
#     elif i>sec_largest and i !=largest:
#         sec_largest=i    

# print("Largest number:", largest)
# print("Second largest number:", sec_largest)       

# a=[12,13,14,15,16]
# for i in range(len(a)):
#     if a[i]<a[i+1]:
#         continue
#     else:
#         print("your list not sorted")
#         break
# else:
#     print("your list is sorted")    


#SET
# Union (A | B ) 
#intersection (A & B)
#Difference (A - B)
# Symmetric Difference (A ^ B)

# a={1,2,3,4}
# b={4,5,6,7}
# s1=a|b #a.union(b)
# s2=a&b #a.intersection(b)
# s3=a-b #a.difference(b)
# s4=a^b #a.symmetric_difference(b)
# print(s1)
# print(s2)
# print(s3)
# print(s4)

#CRUD
# d={10:100,20:200,30:300,40:400}
# d[10]=1000 # update
# d[50]=500 #create
# del d[30] #delete

# for i in d.values():
#     print(i) 

# help(dict)
# print(dir(dict()))
# a=[1,2,3,4,5]
# b=a.copy()
# b[0]=100
# print(b)

# d1={10:100,20:200,40:300}
# d2={40:400,50:500,60:600}
# for i in d2:
#     d1[i]=d2[i]
# print(d1)    
# d1={10:100,20:200,30:300}
# sum=0
# for i in d1:
#     sum=sum +d1[i]
# print (sum)   
# a=[1,1,1,3,4,5,5,5,5]
# count=0
# for i in a:
#     if i==1:
#         count=count+1
# print(count)        

# a=[1,2,3,4,5,1,1,1,1,2,2,3,5,5,6,7,7]
# d={}
# for i in a:
#     if i in d.keys():
#         d[i]=d[i]+1
#     else:
#         d[i]=1
# print(d)     
# d1={10:100,20:200,40:300}
# d2={40:400,50:500,60:600}
# for i in d2:
#     if i in d1.keys():
#         d1[i]=d1[i]+d2[i]
#     else:
#         d1[i]=d2[i]
# print(d1)          

# a=int(input("tell me your number: "))
# try:
#     print(10/a)
# except Exception as err:
#     print(f"sorry there is an err as {err}")
# else:
#     print("there is no exception ")    
# finally:
#     print("i will run no matter")    
# print("ok i have don division ")    


# age=int(input("tell your age: "))
# try:
#     if age<5 or age>18:
#         raise ValueError("YOUR AGE MUST ME BETWEEN 5 AND 18")
#     else:
#         print("you can take admission in our scool ")
             
   
# except Exception as err:
#     print(f"error raise as {err}")

# print("your welcome")      
# p=open(r'C:\Users\rohit\OneDrive\Desktop\New Text Document.txt')
# print(p.read())
# r=open('rohit_s.txt','w')
# r=open('rohit_s.txt','a')
# r=open('rohit_S.txt','x')
# r.write("rohit is best teacher")
# r.close()
# OOPS 
#imperative approach 
# a=20
# b=30
# print(a+b)  

#Functional Approach
# def addition(a,b):
#     return a + b
# print(addition(24,24))
# print(addition(25,46))

#OOP approach
# create object then use object for calculation
#code reusable,execute multiple things together,provide security, use for management systems like bank management and library management
#inside class
#classes- it is a blue print for creating objects

# attributes : variables defined inside the class 

# Methods - Function defined insidea class are Methods 
# class Factory:
#     a=12 #attribute
#     def hello(self):    #method
#         print("how are you") 
#     print("i am initialised")
# print(Factory().a)    call attribute
# Factory().hello()    call method

# class Factory:
#     a=32
#     def hello(self):
#         print("good")
# obj=Factory()
# print(obj.a)
# obj.hello()

# what is oop
# used class
# through class we create obj
# save details of obj in memory delf

# class student:
#     def __init__(self,name,age,gender):
#         self.name=name
#         self.age=age
#         self.gender=gender
#     def show(self):
#         print(f"student details are: {self.name},{self.age},{self.gender}")  
# class_10=student("rohit",24,"male")
# class_10.show()
# a=student("rohit",24,"male" )
# print(a.name)
# print(a.gender)
# print(a.age)           
            
# class Animal:
#     name="lion" #class Attribute 
#     def __init__(self,age):
#         self.age=age #instance attribute
    
#     def show(self): #INSTANCE METHOD
#         print(f"age of aniaml is {self.age}") 

#     @classmethod
#     def hello(cls):
#         print("how are you")
#     @staticmethod
#     def static():
#         print("i am good")         
# obj=Animal(12) 
# obj.show()            
# obj.hello()
# obj.static()        
# Constructor = a special method used to initialize an object's data when the object is created.

#INHERITANCE  
# class FactoryPune:
#     a="introduction"
#     def hello(self):
#         print(" hello rohit how are you")
# class FactoryMumbai(FactoryPune):
#     pass

     
# obj2=FactoryMumbai()
 
# obj2.hello()
# print(obj2.a)

# class Person:
    
#     def __init__(self,name):
#         self.name=name
      
#     def show(self):
#          print(f"name of person is:{self.name}") 

# class Human(Person):
#     pass

# obj=Person("rohit")
# obj.show()
# obj1=Human("kumar")
# obj1.show()
 
#SINGLE 
# class Men: parent
#     def __init__(self,name):
#         self.name=name
        
#     def show(self):
#         print(f"name of person is: {self.name}")
# class Person(Men  ): child
#     def __init__(self,name,age):
#         super().__init__(name)
#         self.age=age
#     def show(self):
#         print(f"name of men is: {self.name} and age is: {self.age}")    

# obj=Person("rohit",24)    
# obj.show()    

# obj1=Men("rohit")
# obj1.show()

#MULTIPLE 
# class Motorola: parent 
#     name1="rohit"
  
# class Samsung:  parent
#     name2="kumar"
   
# class Redmi(Motorola,Samsung): child
#     name="savita"

# obj=Redmi()
# print(obj.name1)                    
# print(obj.name2)                    
# print(obj.name3)                    


# class Father:
#     def hello(self):
#         print("Coding")
    
# class Mother:
#     def skills(self):
#         print("driving")
# class child(Father,Mother):
#     def show(self):
#         print("I have multiple skill")
# obj=child()
# obj.hello()
# obj.skills()
# obj.show()

#MULTILEVEL 
# class Dibiyapur:
#     def __init__(self,bag,chain):
#         self.bag=bag
#         self.chain=chain
#     def show(self):
#         print(f"company made bags of {self.bag} brand and chain {self.chain} brand")
# class Kanpur(Dibiyapur):
#     def __init__(self, bag, chain,design):
#         super().__init__(bag, chain)
#         self.design=design
#     def hello(self):
#         print(f"company made bag {self.design} quality")    
# class Auraiya(Kanpur):
#     def __init__(self, bag, chain, design,color):
#         super().__init__(bag, chain, design) 
#         self.color=color
#     def skill(self):
#         print(f"company made bag in {self.color} color")    

# obj=Auraiya("indian","star","best","blue")
# obj.show()
# obj.hello()
# obj.skill()

#HIERARCHICAL
# class Parent:
#     def show(self):
#         print("I am Parent")


# class Son(Parent):
#     def son(self):
#         print("I am Son")


# class Daughter(Parent):
#     def daughter(self):
#         print("I am Daughter")


# s = Son()
# s.show()
# s.son()

# d = Daughter()
# d.show()
# d.daughter()        
 
#POLYMORPHISM 

#Mehod over riding

# class Boy:
#     def show(self):
#         print("hello my name is rohit")
# class Child(Boy):
#     def show(self):
#         print("hello muy name is ratan")

# obj=Child()
# obj.show()        

#Duck Typing
# class Boy:
#     def show(self):
#         print("hello my name is rohit")
# class Child():
#     def show(self):
#         print("hello muy name is ratan")
# obj=Boy()
# obj.show()
# obj=Child()
# obj.show()        

#Encapsulation

#Private Attributes and Method
# class Boy:
#     __a="rohit"
#     def show(self):
#         print(Boy.__a)


# obj=Boy()
# obj.show()       

# class Demo:

#     def __init__(self):
#         self.age = 24

#     def __show(self):
#         print("Age is", self.age)


# obj = Demo()
# obj.__show()

# class Demo:
#     def __init__(self):
#         self.age=24
#         self.name="rohit"

#     def show(self):
#         print("name of person is:",self.name)   
#         print("age of person is age:",self.age) 
# obj=Demo()
# obj.show()        

#There is no need for @abstractmethod because we are not creating a rule for child classes.
# ABC → Abstract Base Class
# abstractmethod → Used to create a method that child classes must implement means The child class must write the actual code for that method.

#ABSTRACTION

# from abc import ABC, abstractmethod

# class Abstract(ABC):

#     @abstractmethod
#     def perimeter(self):
#         pass

#     @abstractmethod
#     def area(self):
#         pass


# class Square(Abstract):

#     def __init__(self, side):
#         self.side = side

#     def perimeter(self):
#         print(f"Perimeter of square: {4 * self.side}")

#     def area(self):
#         print(f"Area of square: {self.side * self.side}")


# class Circle(Abstract):

#     def __init__(self, radius):
#         self.radius = radius

#     def perimeter(self):
#         print(f"Perimeter of circle: {2 * 3.14 * self.radius}")

#     def area(self):
#         print(f"Area of circle: {3.14 * self.radius * self.radius}")


# obj = Square(10)
# obj.perimeter()
# obj.area()

# obj2 = Circle(7)
# obj2.perimeter()
# obj2.area()

#A decorator is used to add extra functionality to an existing function without changing the original function's code.

# from abc import ABC,abstractmethod

# class Abstract(ABC):

#     @abstractmethod
#     def area(self):
#         pass
#     @abstractmethod
#     def perimeter(self):
#         pass


# class Square(Abstract) :
#           def __init__(self,side):
#                self.side=side

#           def area(self):
#                print(f"area of square: {self.side*self.side}")

#           def perimeter(self):
#                print(f"perimeter of square:{4*self.side}")

# class Circle(Abstract):
#           def __init__(self,radius):
#                self.radius=radius

#           def area(self):
#                print(f"area of circle:{3.14*self.radius *self.radius} ")

#           def  perimeter(self):
#                print(f"perimeter of circle: {2*3.14*self.radius}")


# obj=Square(4)
# obj.area()
# obj.perimeter()

# obj1=Circle(7)
# obj1.area()
# obj1.perimeter()
                    
#  A dunder method is a special method in Python whose name starts and ends with double underscores (__). Python uses these methods automatically to define how an object behaves with built-in operations.       
           

        
# | Dunder Method | Purpose                  | Triggered By     |
# | ------------- | ------------------------ | ---------------- |
# | `__init__`    | Initialize an object     | `Person()`       |
# | `__str__`     | Human-readable string    | `print(obj)`     |
# | `__repr__`    | Developer representation | `repr(obj)`      |
# | `__len__`     | Object length            | `len(obj)`       |
# | `__getitem__` | Indexing                 | `obj[0]`         |
# | `__setitem__` | Assign to an index       | `obj[0] = value` |
# | `__iter__`    | Make object iterable     | `for x in obj`   |
# | `__next__`    | Iterator next value      | `next(iterator)` |
# | `__eq__`      | Equality comparison      | `obj1 == obj2`   |
# | `__lt__`      | Less-than comparison     | `obj1 < obj2`    |     
# | `__add__`     | Addition                 | `obj1 + obj2`    |
# | `__call__`    | Make object callable     | `obj()`          |
    
    
# | Module        | Used for                             |
# | ------------- | ------------------------------------ |
# | `math`        | Mathematical operations              |
# | `random`      | Generate random numbers              |
# | `datetime`    | Date and time                        |
# | `os`          | Operating system operations          |
# | `sys`         | Python/system information            |
# | `time`        | Time-related operations              |
# | `calendar`    | Working with calendars               |
# | `statistics`  | Mean, median, mode, etc.             |
# | `json`        | Working with JSON data               |
# | `re`          | Regular expressions                  |
# | `collections` | Special data structures              |
# | `functools`   | Functions and functional programming |
# | `itertools`   | Iteration tools                      |
# | `pathlib`     | Working with files and directories   |
# | `csv`         | Working with CSV files               |
# | `pickle`      | Store/load Python objects            |
# | `sqlite3`     | Work with SQLite databases           |
# | `logging`     | Create application logs              |


# import random
# num=random.randint(1,10)
# tries=0
# while True:
    # guess=int(input("please guess your number "))

    # if num==guess:
      
    #   print(f"you are right you guessed  the number is {tries} tries ")
    #   tries +=1
    #   break

    # elif num< guess:
    #     print("go to little lower ")
    #     tries +=1

    # elif num > guess:
    #     print("go to little higher  ")
    #     tries +=1


    # else :
      
    #     print("you are wrong")
    #     tries +=1       

# class Name:
#     def __init__(self,name,age):
#         self.age=age
#         self.name=name
#     def __str__(self):
#         return f"My name is {self.name} and age is {self.age}"
    
    
# obj=Name("rohit",24) 
# print(obj)    

# class Name:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age

#     def __add__(self, other):
#         return f"your sum of ages are {self.age + other.age} and sum of name is {self.name } + { other.name}"
        
# obj=Name("rohit",24)
# obj1=Name("harsh",24)
# print(obj + obj1)

# class Name:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
    
#     def __add__(self, other):
#         sum=0
#         for i in other:
#             sum=sum+i.age

#         return f"your sum of ages are {self.age + sum} "
        
# obj=Name("rohit",24)
# obj1=Name("harsh",24)
# obj2=Name("sandy",23)
# obj3=Name("shashank",23)
# print(obj + (obj1,obj2,obj3))

# class rohit:
#     @property
#     def hello(self):
#         print("how are you:")
# obj=rohit()
# obj.hello        
# def decorate(func):
#     def wrapper():
#         print("print this line before hello function ")
#         func()
#         print("print this line after hello functio")
#     return wrapper


# @decorate
# def Hello():
#     print("hello i am rohit ")
# Hello()    
# def decorate(func):
#     def wrapper(a,b):
#         print("hello print sum of digits")
#         func(a,b)
#         print("OK")
#     return wrapper    




# @decorate
# def addition(a,b):
#     print(f"sum of digit is:  { a + b }")
# addition(30,40)    

# class Num:
#     def __init__(self,numbers):
#         self.numbers=numbers
#     def __add__(self,other):
#         sum=0 
#         for i in other:
#             sum = sum + i.numbers
#         return f"sum of numbers are {self.numbers + sum}"    

# obj=Num(20)
# obj1=Num(30)
# obj2=Num(50)
# obj3=Num(25)
# print(obj + (obj1,obj2,obj3))           

# args means Positional  arguments. The * collects multiple Positional  values into a tuple.

# kwargs means keyword arguments. The ** collects multiple keyword and arguments into a dictionary.

# def addition(*args):
#     total=0
#     for i in args:
#         total=total+i
#     print(total)    

    
# addition(20,30,405,78,60)    


# def information(**kwargs):
#     print("your in formation is: ")
#     for i in kwargs:
#         print(f"{i} : {kwargs[i]}")

    
# information(a=20,b=30,c=60) 

# def decorate(func):
#     def wrapper(*args,**kwargs): 
#         print("hello print sum of digits")
#         func(*args,**kwargs)
#         print("OK")
#     return wrapper    




# @decorate
# def addition(a,b):
#     print(f"sum of digit is:  { a + b }")
# addition(40,50)    

# a=13
# print("even" if a%2==0 else "odd")    
   
# age = 20
# result= "Adult" if age >= 18 else "Teenager" if age >= 13 else "Child"

# print(result)   

# l=[i**2 for i in range(1,11) if i % 2 == 0]
# print(l)
# d={i:i**2 for i in range(1,11) if i%2 ==0}
# print(d)
# s={i**2 for i in range(1,11) if i%2 ==0 }
# print(s)

# l=[]
# for i in range(1,11):
#     if i%2 ==0:
#         l.append(i)
# print(l)        

# d={}
# for i in range(1,11):
#     if i%2 ==0: 
#         d[i]=i**2
    
# print(d)    
    
# s=set()
# for i in range(1,11):
#     if i%2 ==0:
#         s.add(i**2)
# print(s)        

# addition=lambda a,b:a+b    

# print(addition(11,33))

# check_even=lambda a: "even" if a%2==0 else "odd"

# print(check_even(22))


# The map() function is used to apply a function to every item in a list, tuple, or other iterable.
# # Lambda is used to create a function in a single line, without using def.  

# l=[1,2,3,4,5]

# result=map(lambda i : i *2, l)
# print(list(result))
# a=[1,2,3,4,5]
# def double(x):
#     return x*2
# result=map(double,a)
# print(list(result))

# def even(x):
#     if x%2==0:
#         return True
#     else:
#         return False
# l=[1,2,3,4,5,6,7,8]
# result=filter(even, l)
# print(list(result)) 
# l=[1,2,3,4,5,6,7,8]    
# result=filter(lambda x : True if x%2==0 else False,l)
# print(list(result)) 
# import maths
# from maths import addition,multiplication
# print (addition(12,22)) 
# print (multiplication(12,22)) 
# json.dump() is used to write/save Python data into a JSON file, and json.load() is used to read JSON data from the file and convert it into Python data.

# And yes, after load() you can read, change, or update the Python data, and then use dump() again to save the changes.
#   Python program updates the data and saves it using json.dump(), and later the Python program can use json.load() to read the updated data and show it to the client.2
# But just changing data is not enough. You must run json.dump() to save the change.
# data.json is a JSON (JavaScript Object Notation) file used to store data in a structured format that is easy for both humans and programs to read.

# In Python, we commonly use json.dump() to write data into data.json and json.load() to read data from it
# main.py → json.dump() → data.json → json.load() → main.py
# flutter used to developed ui part of application like sign in or sign out
# and firebase used to developed backend of part of application storage and authentication 

# name=input("what is your name: ")
# print(len(name))
# glass1 = "milk"
# glass2 = "juice"
 
# temp = glass1 
# glass1 = glass2  
# glass2 = temp 
# # glass1, glass2 = glass2, glass1
# print(glass1,glass2)

# print("welcome band")
# name_city=input("name of city: ")

# name_pet=input("what is your pet name: ")

# print(f"your band name could be {name_city} {name_pet}")

# print("welcome to the calculator!")

# total_bill=float(input("what was the total bill: "))
# tip=float(input("how much tip would you to like: 10, 12 or 15: "))
# people=int(input("how many people to split the bills: "))


# tp=(total_bill * tip) / 100
# s2=(total_bill+tp)/people

# print(f"Each person should pay {s2:.2f}")

# print("Welcome to the calculator!")

# total_bill = float(input("What was the total bill: "))

# tip = float(input("How much tip would you like (0 to 100): "))

# if tip < 0 or tip > 100:
#     print("Please enter a tip between 0 and 100.")
# else:
#     people = int(input("How many people to split the bill: "))

#     tp = (total_bill * tip) / 100

#     s2 = (total_bill + tp) / people

#     print(f"Each person should pay {s2:.2f}")
# name =input("enter your name")
# # lenght=len(name)
# print(len(name))

# print("number of letter in your letter:"  ,  len(input("enter your name: ")))
# print(type("rohit"))
# print(type(233))
# print(type(22.33))
# print(type(True))

# PEMDAS
# Parentheses ()
# exponents **
# multiplication
# division
# add
# sub

# BODY MASS INDEX

W=float(input("enetr weight of person in kg : "))

H=float(input("enter height of person in cm : "))
H=H/100

BMI=W/(H**2)
print(f"your BMI is: {BMI:.2f}")


if BMI <18.5:
    print("underweight")
    

elif BMI >=18.5 and BMI<25:
    print("healthy")  

elif BMI >=25.0 and BMI<30:
    print("overweight")
   

else:
    print("obesity") 
   