# -*- coding: utf-8 -*-
"""
Created on Wed Feb  7 19:21:52 2024

@author: barath
"""

"""Q6"""
l1 = [1,2,3]
l2 = ['a','b','c']

a=[i**2 for i in l1]

b=[(l1[i],l2[i]) for i in range(len(l1))]#b=list(zip(l1,l2))

c=[(l1[i],l2[j]) for i in range(len(l1)) for j in range(len(l1))]

d=[i for j in b for i in j]

print('a)',a)
print('b)',b)
print('c)',c)
print('d)',d)

"""Q7"""
l=[0,1,2,3,4,5,6,7,8,9,0]
print('Orginal ',l)
l[-1]=10
print('Updated ',l)
l.append(11)
print('Appended',l)
l.extend((12,13))
print('Extended',l)
l.pop()
print('Popped  ',l)
l.pop(0)
print('Popped 0',l)
l.remove(12)
print('Removed ',l)
l.reverse()
print('Reversed',l)
l.sort()
print('Sorted  ',l)
l.clear()
print('CLeared ',l)





"""Q8"""
s=input('Enter a string: ')
l=[]
for i in s:
    l.append((i,ord(i)))
t=tuple(l)
print('Output_tuple =',t)


""""Q9"""
l=eval(input('Enter a list of tuples containing student name and roll number: '))  #[('aditi', 1), ('tanya', 2)]
v=('a','e','i','o','u','A','E','I','O','U')
L=[]
for i in l:
    if i[0][0] in v:
        L.append(i)
t=tuple(L)
print('Output_list_of_tuples =',t)


"""Q10"""
s={i for i in range(1,20) if i%3==0 or i%5==0}
print(s)

"""Q11"""
f=frozenset()
print(f,type(f))
d={'Name':'Ram','Age':25,'City':'Chennai'}
f=frozenset(d)
print(f)

























