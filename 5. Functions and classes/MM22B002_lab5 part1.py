# -*- coding: utf-8 -*-
"""
Created on Wed Feb 21 14:00:17 2024

@author: barath
"""

"""Q1"""
n=int(input('Enter a non negative integer: '))

##loops
#A
fact=1
for i in range(1,n+1):
    fact*=i
print('The factorial of',n,'is',fact)

#B
#  0,1,1,2,3,5,8,11,... I've considered the series starting from zero
f=[0,1]
for i in range(n-2):
    f.append(f[i]+f[i+1])
print('The',n,'th fibonacci number is',f[n-1])

#C
a=int(input('Enter a postive number: '))
b=int(input('Enter the above number\'s exponent(>=0): '))
c=1
for i in range(b):
    c*=a
print(a,'^',b,'=',c)

##recursion
#A
def fact(n):
    if n==1:
        return 1
    else:
        return n*fact(n-1)

print('The factorial of',n,'is',fact(n))

#B
def fib(n):
    if n==1:
        return 0
    elif n==2:
        return 1
    else:
        return fib(n-1)+fib(n-2)

print('The',n,'th fibonacci number is',fib(n))

#C
def exp(a,b):
    if b==1:
        return a
    else:
        return a*exp(a,b-1)
    
print(a,'^',b,'=',exp(a,b))


"""Q2"""
n=int(input('Enter a value for N such that 0<=N<=100: '))
m=int(input('Enter a value for M such that 0<=M<=9: '))

def fun(n,m):
    if n==-1:
        return 0
    else:
        return str(n).count(str(m))+fun(n-1,m)
print(fun(n,m))

"""Q3"""
#A
l=eval(input('list of names: ')) #['Alice','Bob','Charlie']
L=map(lambda x:'Hello,'+x,l)
print(list(L))

#B
l=eval(input('list of numbers: ')) # [1,2,4,3,5,6,8,7,9]
L=filter(lambda x:x%2==0,l)
print('All even numbers from a given list: ',list(L))

#C
l=eval(input('list of strings: ')) # ['Python','is','awesome']
from functools import reduce
L=reduce(lambda x,y:x+y,l)
print(L)

"""Q4"""

class Complex:
    def __init__(self,r=0,im=0):
        self._real=r
        self._imag=im
        
        
    def add_comp(self,other):            #(a+ib)+(c+id)=(a+c)+i(b+d)
        c=Complex()
        c._real=self._real+other._real
        c._imag=self._imag+other._imag
        return c
    def __add__(self,other):            #OPERATOR OVERLOADING
        c=Complex()
        c._real=self._real+other._real
        c._imag=self._imag+other._imag
        return c
    
    
    def sub_comp(self,other):            #(a+ib)-(c+id)=(a-c)+i(b-d)
        c=Complex()
        c._real=self._real-other._real
        c._imag=self._imag-other._imag
        return c
    def __sub__(self,other):            #OPERATOR OVERLOADING
        c=Complex()
        c._real=self._real-other._real
        c._imag=self._imag-other._imag
        return c
    
    def mul_comp(self,other):            #(a+ib)*(c+id)=a*c-b*d+i(a*d+b*c)
        c=Complex()
        c._real=(self._real*other._real)-(self._imag*other._imag)
        c._imag=(self._real*other._imag)+(self._imag*other._real)
        return c
    def __mul__(self,other):            #OPERATOR OVERLOADING
        c=Complex()
        c._real=(self._real*other._real)-(self._imag*other._imag)
        c._imag=(self._real*other._imag)+(self._imag*other._real)
        return c
    
    
    def div_comp(self,other):            #(a+ib)/(c+id)=[(a+ib)*(c-id)]/(c^2+d^2)
        mag=other._real**2+other._imag**2
        other_conj=Complex()
        other_conj._real=other._real
        other_conj._imag=-other._imag
        c=self.mul_comp(other_conj)
        c._real=c._real/mag
        c._imag=c._imag/mag
        return c
    def __truediv__ (self,other):            #OPERATOR OVERLOADING
        mag=other._real**2+other._imag**2
        other_conj=Complex()
        other_conj._real=other._real
        other_conj._imag=-other._imag
        c=self.mul_comp(other_conj)
        c._real=c._real/mag
        c._imag=c._imag/mag
        return c
    

    def print_comp(self):
        print(self._real,' + i',self._imag)
    
       

c1=Complex(5,7)
c2=Complex(4,3)
c3=Complex() ;c4=Complex() ;c5=Complex() ;c6=Complex()
c1.print_comp() ; c2.print_comp()
c3=c1.add_comp(c2) ; print('SUM        :',end='  ') ; c3.print_comp()
c4=c1.sub_comp(c2) ; print('DIFFERENCE :',end='  ') ; c4.print_comp()
c5=c1.mul_comp(c2) ; print('PRODUCT    :',end='  ') ; c5.print_comp()
c6=c1.div_comp(c2) ; print('QUOTIENT   :',end='  ') ; c6.print_comp()

C3=Complex() ;C4=Complex() ;C5=Complex() ;C6=Complex() 
C3=c1+c2 ; C3.print_comp()
C4=c1-c2 ; C4.print_comp()
C5=c1*c2 ; C5.print_comp()
C6=c1/c2 ; C6.print_comp()
