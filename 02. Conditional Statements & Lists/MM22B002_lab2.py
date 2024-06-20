# -*- coding: utf-8 -*-
"""
Created on Wed Jan 31 14:05:29 2024

@author: barath
"""

#Q1
#a
print('Using conntinue statement')
for i in range(1,1001):
    if i%7!=0 or i%8!=0:
        continue
    print(i,end=' ')
print()
#b
print('Using pass statement')
i=1
while i<=1000:
    if i%7==0 and i%8==0:
        print(i,end=' ')
    i+=1
    pass
print()

#Q2
n='34567222541147'
e=0
o=0
for i in n:
    i=int(i)
    if i%2==0:
        e+=i
    else:
        o+=i
print('The sum of all even digits =',e)
print('The sum of all odd digits = ',o)


#Q3
import random
l=[random.randint(0,100) for i in range(10)]
print('The list is',l)

MAX=MIN=l[0]
for i in l:
    if i<MIN:
        MIN=i
    if i>MAX:
        MAX=i
print('Maximum & minimum numbers from the list using conditional expression are',MAX,'and',MIN)
if MAX==max(l) and MIN==min(l):
    print('Verified using max() and min() functions.')

#Q4
import math
n=int(input('Enter the no. of rows needed for the pascal\'s triangle '))
for i in range(n):
    for j in range(n+1-i):
        print('',end=' ')
    for j in range(i+1):
        print(int(math.factorial(i)/(math.factorial(j)*math.factorial(i-j))),end=' ')
    print()

#Q5
#A
n=input('Enter a number: ')
if n==n[::-1]:
    print('TRUE, it is a palindrome')
else:
    print('No, it is not a palindrome')

#B
s=input('Enter a sentence: ')
s=s.lower()
Str=''
for i in s:
    if i.isalpha():
        Str+=i
print('TRUE, it is a palindrome') if Str==Str[::-1] else print('no')


#Q6
print('The Unicode of "A" is',ord('A'))
print('The Unicode of "A" is',ord('A'))
print('122 is the Unicode of "',chr(122),'"')
print('63 is the Unicode of "',chr(63),'"')
n=int(input('Enter the no. of lines for the pattern: '))
A=ord('A')
for i in range(n):
    print((chr(i+A))*(i+1))
    
#Q7
l=['Virat Kohli','Rohit Sharma','Chris Gayle','Steve Smith']
a=[]
b=[]
for i in l:
    ll=i.split()
    a.append(ll[0])
    b.append(ll[1])
    n=l.index(i)
    l[n]=ll[1]+' '+ll[0]
print('a)',a)
print('b)',b)
print('c)',l)
l.sort()
for i in l:
    ll=i.split()
    n=l.index(i)
    l[n]=ll[1]+' '+ll[0]
print('d)',l)
    
#Q8 WAP to find the minimum of 3 numbers using
a,b,c=random.randint(0, 1000),random.randint(0, 1000),random.randint(0, 1000)
print('The numbers are: ',a,b,c)

#a
print('BY USING CONDITIONAL EXPRESSIONS,',end=' ')
if a<=b and a<=c:
    print(a,'is the minimum.')

if b<=a and b<=c:
    print(b,'is the minimum.')

if c<=b and c<=a:
    print(c,'is the minimum.')
    
#b
print('BY USING NESTED CONDITIONAL EXPRESSIONS,',end=' ')
if a<b:
    if a<c:
        print(a,'is the minimum.')
    else:
        print(c,'is the minimum.')
else:
    if b<c:
        print(b,'is the minimum.')
    else:
        print(c,'is the minimum.')

#c
d=(random.randint(0, 1000))
print('Now the list of 4 numbers are: ',a,b,c,d)
if a<b:
    if a<=d and a<=c:
        print(a,'is the minimum of the four numbers.')

    elif d<=a and d<=c:
        print(d,'is the minimum of the four numbers.')

    elif c<=d and c<=a:
        print(c,'is the minimum of the four numbers.')
else:   
    if d<=b and d<=c:
        print(d,'is the minimum of the four numbers.')
    
    elif b<=d and b<=c:
        print(b,'is the minimum of the four numbers.')
    
    elif c<=b and c<=d:
        print(c,'is the minimum of the four numbers.')

#Q9
l=['Metallurgical and Materials engineering','Mechanical engineering','Electrical engieering','Engineering design','Civil engineering','Engineering Physics','Chemical engineering']
#append
l.append('Aero space engineering')
print('After appending',l,sep='\n')
#remove
l.remove('Engineering Physics')
print('After removing',l,sep='\n')
#pop
l.pop()
print('After poping',l,sep='\n')
#insert 
l.insert(3,'Biological engineering')
print('After inserting',l,sep='\n')
#reverse
l.reverse()
print('The reversed list is',l,sep='\n')
#sort
l.sort()
print('The sorted list is',l,sep='\n')
#count
print('The no. of times Mechanical engineering has occured is',l.count('Mechanical engineering'))
#index
print('THe index of Electrical engieering is',l.index('Electrical engieering'))
#extend
L=['Engineering Physics','Aero space engineering']
l.extend(L)
print(l)
#slice
l[1:3]
#clear
l.clear()
print('After clearing',l)




















