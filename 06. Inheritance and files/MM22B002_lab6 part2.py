# -*- coding: utf-8 -*-
"""
Created on Thu Feb 29 15:29:52 2024

@author: barath
"""
"""Q6"""

class Vehicle:
    def __init__(self):
        self._make=None
        self._model=None
        self._year=None
    def initialize_vehicle(self,mk,md,yr):
        self._make=mk
        self._model=md
        self._year=yr
    def display_vehicle(self):
        print('Make  :',self._make)
        print('Model :',self._model)
        print('Year  :',self._year)

class Car(Vehicle):
    def __init__(self):
        super().__init__()
        self._fuel_type=None
    def get_car_details(self,mk,md,yr,ft):
        self._make=mk
        self._model=md
        self._year=yr
        self._fuel_type=ft
    def display_vehicle(self):
        print('Make:',self._make,end=', ')
        print('Model:',self._model,end=', ')
        print('Year:',self._year)
        print('Fuel type:',self._fuel_type)

class Bike(Vehicle):
    def __init__(self):
        super().__init__()
        self._gear_count=None
    def get_bike_details(self,mk,md,yr,gc):
        self._make=mk
        self._model=md
        self._year=yr
        self._gear_count=gc
    def display_vehicle(self):
        print('Make:',self._make,end=', ')
        print('Model:',self._model,end=', ')
        print('Year:',self._year)
        print('Gear count:',self._gear_count)


my_car = Car()
my_car.get_car_details("Toyota", "Camry", 2020, "Petrol")
my_car.display_vehicle()

my_bike = Bike()
my_bike.get_bike_details("Yamaha", "YZF R1", 2021, 6)
my_bike.display_vehicle()

"""Q7"""

class Student:
    sc_name='XYZ SCHOOL'
    students=0
    classes=8
    def __init__(self,name,age,grade,class_schedule):
        self._name=name
        self._age=age
        self._grade=grade
        self._class_schedule=class_schedule
        Student.students+=1
    def print_det(self):
        print('Student name:',self._name)
        print('Age:',self._age)
        print('Shcool name:',Student.sc_name)
        print('Grade:',self._grade)
        print('Class shedule:',self._class_schedule)
        print('Total classses offered:',Student.classes)
        print('Total no. of students:',Student.students)
        
student1=Student("Alison",15,10,["Math", "Science", "English"])
student1.print_det()
student2=Student("Bill",14,9,["History", "Geography", "Art"])
student2.print_det()
print(Student.sc_name)
"""In Python, class variables (also known as class attributes) are shared across all 
instances (objects) of a class. They belong to the class itself, not to any specific
instance.""" 
"""Q8"""
#A
class Numbers:
    def __init__(self,a,b):
        self._num1=a
        self._num2=b
    def find_gcd(self):
        a=self._num1
        b=self._num2
        if a>b:
            for i in range(b,0,-1):
                if a%i==0 and b%i==0:
                    print('The GCD is',i)
                    break
        else:
            for i in range(a,0,-1):
                if a%i==0 and b%i==0:
                    print('The GCD is',i)
                    break
    def find_lcm(self):
        a=self._num1
        b=self._num2
        if a>b:
            i=1
            while True:
                if (a*i)%b==0:
                    print('LCM  is ',a*i)
                    break
                else:
                    i+=1
        else:
            i=1
            while True:
                if (b*i)%a==0:
                    print('LCM  is ',b*i)
                    break
                else:
                    i+=1
                    
n=Numbers(12,9)
n.find_gcd()
n.find_lcm()

#B
class EvenNumbers(Numbers):
    def __init__(self,a,b):
        super().__init__(a,b)
    def find_lcm(self):
        a=self._num1
        b=self._num2
        if a%2==0 and b%2==0:
            return super().find_lcm()
        else:
            print('Both the numbers are not even')
            
#C
class OddNumbers(Numbers):
    def __init__(self,a,b):
        super().__init__(a,b)
    def find_lcm(self):
        a=self._num1
        b=self._num2
        if a%2!=0 and b%2!=0:
            return super().find_lcm()
        else:
            print('Both the numbers are not odd')

#D
class CompositeNumbers(EvenNumbers,OddNumbers):
    def __init(self,a,b):
        super().__init__(a,b)
    def find_gcd(self):
        return super().find_gcd()

c=CompositeNumbers(12,9)
c.find_gcd()
c.find_lcm()

"""Q9"""
import csv
try:
    with open('books.csv','r') as f:
        r=csv.reader(f)
        print('Current items')
        for i in r:
            print(i)
except:
   with open('books.csv','w') as f:
       r=csv.writer(f)
       r.writerow(['Title','Author','Publication year','ISBN number'])

c=(input('Do you wanna add a book(y/n) :')).lower()
if c=='y':
    t=input('Enter the book title :')
    a=input('Enter the author\'s name :')
    y=input('Enter the year of plublicatiion :')
    n=input('Enter the ISBN number ')
    with open('books.csv','a') as f:
        r=csv.writer(f)
        r.writerow([t,a,y,n])

c=(input('Do you wanna see the books(y/n) :')).lower()
if c=='y':        
    with open('books.csv','r') as f:
        r=csv.reader(f)
        print('Current items')
        for i in r:
            if len(i)!=0:
                print(i)

"""Q10"""
import pandas as pd
words=['banana','apple','grape','orange','pineapple']
df=pd.DataFrame(words,columns=['Words'])
dfs=df.sort_values(by='Words')
dfs.to_csv('sorted.txt',index=False,header=False)
with open('sorted.txt','r') as f:
    print(f.read())





