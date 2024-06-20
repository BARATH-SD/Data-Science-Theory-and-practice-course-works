# -*- coding: utf-8 -*-
"""
Created on Wed Feb 14 18:14:32 2024

@author: barath
"""

"""Q6"""
d={1322:{'Name':'Mike','Salary':40000,'Years of experience':5},
   1566:{'Name':'Munson','Salary':30000,'Years of experience':1},
   3443:{'Name':'Max Mayfield','Salary':35000,'Years of experience':3}}

#A
l=[]
for i in d.values():
    l.append(i['Salary'])
l.sort()

d1={}
for i in l:
    for j in d:
        if i==d[j]['Salary'] and j not in d1:
            d1[j]=d[j]
            break
print('Sorted dictionary using their salaries:',d1)

#b
a=[1244,{'Name':'Billy','Salary':45000,'Years of experience':2}]
l=list(d1.items())
for i in l:
    if a[1]['Salary']<=i[1]['Salary']:
        l.insert(l.index((i)),a)
        break
    elif a[1]['Salary']>l[-1][1]['Salary']:
        l.append(a)
        break
d2=dict(l)
print(d2)

"""Q7"""

A={'a':3,'b':5,'c':7}
B={'b':2,'c':4,'d':6}

C=dict(A)
for i in B:
    if i in C:
        C[i]+=B[i]
    else:
        C[i]=B[i]
print('The dictionary C is',C)


"""Q8"""
l=eval(input('Enter the list of list each of 2 elements: ')) #[[1,'q'],[2,'w'],[3,'e']]
d={}
for i in l:
    d[i[0]]=i[1]
print(d)

"""Q9"""
#Positional arguments are passed to a function based on their position in the function call.
#Keyword arguments, on the other hand, are identified by their parameter names.
def f1(i,f,s):
    return i+f,s.upper()

a,b,c=1,2.2,'abc'
print(f1(a,b,c)) #calling the function using postional arguments
print(f1(s='hola',i=12,f=33.3))  #calling the function using keyword arguments

"""Q10"""
def maximum(*args):
    if len(args)!=0:
        m=args[0]
        for i in args:
            if i>m:
                m=i
        return m
print(maximum(34,56,54,3,2234,56,789,8754))

"""Q11"""
def concat(**kwargs):
    if len(kwargs)!=0:
        s=''
        for i in kwargs.values():
            s+=i
        return s

concat(i='HOLA',j=' ',k='MADDY')


