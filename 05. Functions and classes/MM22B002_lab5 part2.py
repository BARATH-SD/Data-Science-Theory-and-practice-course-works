# -*- coding: utf-8 -*-
"""
Created on Wed Feb 21 18:34:08 2024

@author: barath
"""
"""Q5"""

class Bank_Account:
    def __init__(self,name,num,adrs,bal):
        self._account_holder_name=name
        self._account_number=num
        self._address=adrs
        self._balance=bal
    
    def deposit(self,d):
        self._balance+=d
        
    def withdraw(self,w):
        self._balance-=w
        
    def check_balance(self):
        return self._balance
    
    def update_details(self,name,adrs):
        self._account_holder_name=name
        self._address=adrs
        
    def display_details(self):
        print('Account holder name: ',self._account_holder_name)
        print('Account_number: ',self._account_number)
        print('Address: ',self._address)
        print('Balance: ',self._balance)

a=Bank_Account('Mike Wheeler',1985,'2350 Mapple street,Hawkins,Indiana',150300.35)
b=a.check_balance()
print('Current balance=',b)

d=float(input('Enter the amount to be deposited: '))
a.deposit(d)
print('Current balance=',a.check_balance())

w=float(input('Enter the amount to be withdrawn: '))
a.withdraw(w)
print('Current balance=',a.check_balance())

nam=input('Enter new name: ') # Michael Wheeler
adrs=input('Enter new address: ') # 2351 Mapple street,Hawkins,Indiana
a.update_details(nam,adrs)

a.display_details()


"""Q6"""
import random
class Matrix:
    def __init__(self,m,n):
        self._rows=m
        self._cols=n
        self._matrix=[]               # starting the matrix as a empty list 
        for i in range(m):            # and then appending each row..
            l=[]
            for i in range(n):
                l.append(random.randint(1,10))
            self._matrix.append(l)
    
    def show(self):
        print(self._matrix)
    
    def __add__(self,other):
        if self._rows==other._rows and self._cols==other._cols:
            s=Matrix(self._rows,self._cols)        # (mxn)+(mxn) = (mxn)   
            for i in range(self._rows):
                for j in range(self._cols):
                    s._matrix[i][j]=self._matrix[i][j]+other._matrix[i][j]
            return s._matrix
    
    def __sub__(self,other):
        if self._rows==other._rows and self._cols==other._cols:
            s=Matrix(self._rows,self._cols)        # (mxn)-(mxn) = (mxn)
            for i in range(self._rows):
                for j in range(self._cols):
                    s._matrix[i][j]=self._matrix[i][j]-other._matrix[i][j]
            return s._matrix
    
    def __mul__(self,other):                      # (mxn) * (nxp) = (mxp)
        if self._cols==other._rows:
           s=Matrix(self._rows,other._cols)
           for m in range(self._rows):
               for p in range(other._cols):
                   a=0
                   for n in range(self._cols):
                       a=a+self._matrix[m][n]*other._matrix[n][p]
                   s._matrix[m][p]=a    
           return s._matrix
        
    def element_by_element_mul(self,other):
        if self._rows==other._rows and self._cols==other._cols:
            s=Matrix(self._rows,self._cols)
            for i in range(self._rows):
                for j in range(self._cols):
                    s._matrix[i][j]=self._matrix[i][j]*other._matrix[i][j]
            return s._matrix
    
    def scalar_mul(self,c):
        for i in range(self._rows):
           self._matrix[i]=list(map(lambda x:x*c,self._matrix[i]))
        return self._matrix


M1=Matrix(2, 2)
M2=Matrix(2, 2)
M1.show()
M2.show()
M3=M1+M2 ; print(M3)
M4=M1-M2 ; print(M4)
M5=M1*M2 ; print(M5)
M6=M1.element_by_element_mul(M2) ; print(M6)
M7=M1.scalar_mul(2) ; print(M7)



"""Q7"""
class Time:
    def __init__(self,h,m,s):
        if 0<=h<=23 and 0<=m<=59 and 0<=s<=59:
            self._hour=h
            self._min=m
            self._sec=s
        else:
            print('Give proper time')
    
    def __str__(self):
        print(self._hour,':',self._min,':',self._sec,sep='')
        
    def set_time(self,h,m,s):
        self._hour=h
        self._min=m
        self._sec=s
        print('Time has been updated...')
    
    def get_time(self):
        print('The time is ',self._hour,':',self._min,':',self._sec,sep='')
        
    def add_seconds(self,s):
        self._sec+=s
        if self._sec>=60:
            m=self._sec//60
            self._sec-=60*m
            self._min+=m
        if self._min>=60:
            h=self._min//60
            self._min-=60*h
            self._hour+=h
        if self._hour>=24:
            self._hour-=24
        print('Added seconds...')

t=Time(6,35,30)
t.__str__()
t.set_time(23, 55, 30)
t.get_time()
t.add_seconds(3600)
t.get_time()

"""Q8"""
import math
class Geometry:
    def circle_area(r):
        return math.pi*r*r if r>0 else print('Only positive numbers')
    def rectangle_area(l,b):
        return l*b if l>0 and b>0 else print('Only positive numbers')
    def square_area(a):
        return a*a if a>0 else print('Only positive numbers')
    
    def circle_perimeter(r):
        return math.pi*r*2 if r>0 else print('Only positive numbers')
    def rectangle_perimeter(l,b):
        return 2*(l+b) if l>0 and b>0 else print('Only positive numbers')
    def square_perimeter(a):
        return 4*a if a>0 else print('Only positive numbers')
    

Geometry.circle_area(-3)
print(Geometry.circle_area(3))
print(Geometry.rectangle_area(6,3))
print(Geometry.square_area(4))

print(Geometry.circle_perimeter(7))
print(Geometry.rectangle_perimeter(13,6))
print(Geometry.square_perimeter(8))
