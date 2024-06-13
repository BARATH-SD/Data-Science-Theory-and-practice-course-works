# -*- coding: utf-8 -*-
"""
Created on Wed Jan 24 14:00:12 2024

@author: barath
"""
import numpy as np
'''Q1'''

# 7*ln(3)*[ln(5)+ln(e^3)]
print(7*np.log(3)*(np.log(5)+(np.log((np.e)**3))))

#Difference in area between two concentric circles of diameter 5m and 3m.
R=5/2
r=3/2
p=np.pi
print('Difference in area =',p*(R**2-r**2))

'''Q2'''
e=int(80/2)-int(7/2)
o=(80-7+1)-e
print(f'The number of odd numbers between 7 and 80 (both inclusive) is {o}. ',end='')
print(f'And the number of even numbers is {e} ')

'''Q3'''
'''There are different kinds of data types in python such as:numeric,sequence,boolean,set,dictionary.
Numeric datatypes includes int,float and complex.
Sequence datatypes includes string,list and tuple.

int-It contains positive or negative whole numbers (without fractions or decimals).
float-It is a real number with a floating-point representation. It is specified by a decimal point.
complex–It is specified as real part + imaginary part(j).
str-It is a collection of one or more characters put in a single quote, double-quote.
tuple-It is a immutable ordered collection of items.
list-It is a mutable ordered collection of items.
dict-It stores data values in key value pairs.
bool-Represents one of the two values,True or False.
'''
import sys
l=(12,14.5,23+4j,'qwerty',(1,2,3,45),True,[123,345,456],{1:'tom',2:'sam'})
d={}
for i in l:
    size=sys.getsizeof(i)
    d[size]=i
s=list(d.keys())
s.sort()
for i in s:
    print(d[i],'is of the datatype:',type(d[i]),'and of size:',i)


'''Q4'''
import random
n=int(input('Enter the seed value:'))
random.seed(n)
a=random.randint(10,100)
b=random.randint(10,100)
c=random.randint(10,100)
s=2*(a*b+b*c+c*a)
print('the surface area of a cuboid with sides',a,b,c,'=',s)

'''Q5'''
print('ax^2+bx+c=0')
a=int(input('Enter the the value of "a" in the above equation: '))
b=int(input('Enter the the value of "b" in the above equation: '))
c=int(input('Enter the the value of "c" in the above equation: '))
x=((-b)+(b*b-4*a*c)**0.5)/(2*a)
y=((-b)-(b*b-4*a*c)**0.5)/(2*a)
print('Solutions of the equation is',x,'and',y)

'''Q6'''
l=input('Enter two numbers seperated by a space: ')
a,b=l.split()
a,b=int(a),int(b)
print('Addition',a,'+',b,'=',a+b)
print('Subtraction',a,'-',b,'=',a-b)
print('Multiplication',a,'x',b,'=',a*b)
print('Division',a,'/',b,'=',a/b)
print('Exponent',a,'^',b,'=',a**b)

'''Q7'''
l,p,i,f='Learning','python','is','fun'
s=' '.join([l,p,i,f])
print(s+'.')
print(s.replace('python','datascience')+'.')
print(s.upper()+'.')
s=s.lower()
l=s.split()
l.reverse()
print(' '.join(l)+'.')

for i in range(4):
    l[i]=l[i][::-1]
    
print(' '.join(l)+'.')

'''Q8'''
''' Python is a free and open source language which supports GUI.And it is a Integrated and Interpreted Language.
The code  written in python can also run on different platforms
'''

'''Q9'''
'''Python's built-in-functions are the functions that are readily available for the users in python.
These functions can be accessed directly without importing any modules or libraries.
print()-Prints the values to a stream.
len()-Return the number of items in a container.
abs()-Return the absolute value of the argument.
chr()-Return a Unicode string of one character.
ord()-Return the Unicode code point for a one-character string.
'''

'''Q10'''
s=(input('Enter a word: ')).lower()
l=('a','e','i','o','u')
n=0
for i in s:
    if i in l:
        n+=1
print(f'Number of vowels in {s} is {n}')

s=(input('Enter a word: ')).lower()
if s==s[::-1]:
    print(f'{s} is a palindrome')
else:
    print(f'{s} is not a palindrome')
