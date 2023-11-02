# name="Aryan Tiwari"
# print(name)
# print(len(name))
# age=25
# if age>=18:
#     print("you are an adult")
# else:
#     print("you are a minor")

# score=85
# if score>=90:
#     print("A")
# elif score>=80:
#     print("B")
# elif score>=70:
#     print("C")
# else:
#     print("D")
# a=True
# b=False
# if a:
#     print("Bring an umbrella.")
#     if b:
#       print("Wear a jacket")
# number=0
# if number>0:
#    print("The number is positive")
# elif number<0:
#    print("The number is negative")         
# else :
#    print("The number is zero")

# sets 
# s=set(map(int,input().split()))
# b=set(map(int,input().split()))
# print(s.union(b))
# print(s&(b))
# print(s.difference(b))

# def inter(a,b):
#     c=a.intersection(b)
#     return c

# s=set(map(int,input().split()))
# s1=set(map(int,input().split()))
# c=inter(s,s1)
# print(c)
# s.add(5)
# print(s)
# s.remove(5)
# print(s)
# s.discard(5)
# print(s)
# s.pop()
# print(s)

# class greating:
#     def __init__(self,name):
#         self.name=name
#         print("Good morning",name)
# dog1=greating("raju bhai")
# class Employee:
#     Name="raju"
#     id=6767
#     roll="programmer"
# c=Employee
# print(c.Name)    
# c.Name="panju"
# print(c.Name) 

# class Car:
#     def __init__(self,make,model):
#         self.make=make
#         self.model=model
#         print(make,model)
# car1=Car("honda","ka")        
# car2=Car("toyota","camry")
# print(car1.make,car1.model)        
# print(car2.make,car2.model)        
# print(car2)        

# class Animal:
#     def __init__(self,name):
#         self.name=name
#     def speak(self):
#         pass

# class Dog(Animal):
#     def speak(self):
#         return "woof"
    
# class Cat(Animal):
#     def speak(self):
#         return "Meow"
# dog=Dog("raju")    
# cat=Cat("Bheem")
# print(dog.name,dog.speak())    
# print(cat.name,cat.speak())    
           
# employees=["corey","jin","steven","April","judy","john","jane"]
# gym_member=["April","john","corey"]
# developers=["judy","corey","steven","jane","April"]
# e=set(employees)
# y=set(gym_member)
# d=set(developers)
# h=e&y
# x=h&d
# print(x)


# s={1,3}
# s1={1,4}
# s2={5,1}
# s3=s.intersection(s1,s2) # it use to take the intersection between multiple set 
# print(s3)
# d={}
# d["Dog"]="uday"
# # print(d)
# student={
#     "name":"uday",
#     "age":25,
#     "grade":"A",
# }
# student[0] it will return error
# student.update({"uday":"pavan"})
# for i in student:
#     print(i)
# student["Gender"]="Trans"    
# student["roll"]="student"    
# for j in student:
    # print(student[i])    
# print(student.get("name"))
# print(student.get("nam"))
# print(student)
# print(student.keys())
# print(student.values())
# for c,d in student.items():
#     print(c,d)
#     print()
# squares={num: num**2 for num in range(1,6)}   
# cubes={i: i**3 for i in range(1,6)}   
# print(squares) 
# print(cubes) 
# grade=student.get("grade","N/A")
# print(grade)
# phone=student.get("phone","N/A")
# p=student.get("village")
# print(p)
# print(phone)

# d["username"]="uday"
# d["age"]=19
# d["Id"]="2315800093"
# print(d)
# n=int(input())
# d={}
# for i in range(n):
#     key=input()
#     value=input()
#     d[key]=value
# print(d)

# d1={}
# d2={}
# d3={}
# d4={}
# d1["age"]="45"
# d1["cricket"]="nice"
# d2["age"]="45"
# d2["cricket"]="nice"
# d3["age"]="45"
# d3["cricket"]="nice"
# d4["age"]="45"
# d4["cricket"]="nice"
# print(d1)
# print(d2)
# print(d3)
# print(d4)
# d1.update(d2)
# print(d1)

# 111
# ********************
# color_dict={"red":"#FF0000","black":"#008000","white":"#FFFFFF"}
# d={}
# z=sorted(color_dict)
# for i in z:
#     d[i]=color_dict[i]
# print(d)    
# *************

# 222
# m={"data1":100,"data2":-54,"data3":247}
# z=m.values()
# q=sum(z)
# print(q)

# # 33
# b={}
# for i in range(1,15):
#     b[i]=i**2
# print(b)
# # 44 
# ha={"x":10,"y":20,"z":30}
# for i in ha:
#     print({i:ha[i]}) 

# # 55
# hh=int(input())
# zz={}
# for i in range(1,hh+1):
#     zz[i]=i**2
# print(zz)

def key(d):
    if 3 in d:
      return "Yes"
    else:
       return "No"
    
    # return a 
d={1:10,2:20,3:30,4:40,5:50,6:60}
# k=d.keys()
print(key(d))
    





