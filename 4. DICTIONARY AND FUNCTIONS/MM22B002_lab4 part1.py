# -*- coding: utf-8 -*-
"""
Created on Wed Feb 14 13:47:45 2024

@author: barath
"""


"""Q1"""
a=range(5) # Return an object that produces a sequence of integers from start (inclusive)
l=list(a)  # to stop (exclusive) by step.
print(l)

b=iter(l) # Returns an iterator object.
print(next(b)) #Return the next item from the iterator.

c=eval(input('Enter ')) #Reads input from the user.
print(type(c))

for i in enumerate(l):  # Returns tuples containing an index and value from an iterable.
    print(i)
    
t=10,20,30,40,50
d=zip(l,t)   #Combines multiple iterables into a single iterable of tuples.
print(list(d))

f=lambda x: x**3 #Creates an anonymous function.
print(f(5))

g=map(lambda x:x**2,l)  # Make an iterator that computes the function using arguments from 
print(list(g))     # each of the iterables.  Stops when the shortest iterable is exhausted.

filter, # Return an iterator yielding those items of iterable for which function(item)
            # is true

from functools import reduce
j=reduce(lambda x,y:x+y,l) #  Applies a rolling computation to sequential pairs of values 
print(j)                   #  in a list.



a
"""Q2"""
ip={'lemon':'yellow','apple':'red','orange':'orange'}

val=[]
for i in ip.values():
    val.append(i)
    
length=[]
for i in val:
    length.append(len(i))
length.sort()

v=[]
for i in length:
    for j in val:
        if i==len(j) and j not in v:
            v.append(j)
            break

op={}
for i in v:
    for j in ip:
        if i==ip[j]:
            op[j]=i
print('Ouput:',op)


"""Q3"""
#A
s=input('Enter a string: ')

#B
d=dict.fromkeys(s)
for i in s:
    d[i]=s.count(i)
print(d)

#C
v=list(d.values())
v.sort()

l1=[]
for i in v:
    for j in d:
        if i==d[j] and (j,i) not in l1:
            l1.append((j,i))

i=0
while i<(len(l1)-1):
    if l1[i][1]==l1[i+1][1]:
        if l1[i][0]<l1[i+1][0]:
            i+=1
            continue
        else:
            l1[i],l1[i+1]=l1[i+1],l1[i]
            i=0
    else:
        i+=1

print('Sorted list of tuples based on frequency: ',l1)

#D
k=list(d.keys())
k.sort()
l2=[]
for i in k:
    l2.append((i,d[i]))
    
print('Sorted list of tuples based on alphabets: ',l2)

#E
l3=[]
for i in v:
    for j in d:
        if i==d[j] and (j,i) not in l3:
            l3.append((j,i))

i=0
while i<(len(l3)-1):
    if l3[i][1]==l3[i+1][1]:
        if l3[i][0]>l3[i+1][0]:
            i+=1
            continue
        else:
            l3[i],l3[i+1]=l3[i+1],l3[i]
            i=0
    else:
        i+=1
l3.reverse()
print('The most occuring three: ')
for i in range(3):
    print(l3[i],end=' ')
print()


"""Q4"""

def lookup_student(d,n):
    if n in d:
        return d[n]
    else:
        return ('Not Found')

records = { "Alice":"AB111","Bob":"EE200","David":"XY333"}

print(lookup_student(records,"Bob"))

print(lookup_student(records,"John")) 


"""Q5"""
l=[1,2,3,4,6,4,3,1,3,5,7,7,5,3,2,1,4,6,7,8,7]

#A
d=dict.fromkeys(l)
for i in d:
    d[i]=l.count(i)
print('The frequency of each integer: ',d)

#B
print('The maximum integer is',max(d),'and its frequency is =',d[max(d)])

#C
L1=[]
for i in l:
    if i not in L1:
        L1.append(i)
print('The list after removing the duplictes: ',L1)

#D
s=set()
for i in l:
    s.add(i)
    print(s)
print('The list after removing the duplictes: ',list(s))




