# -*- coding: utf-8 -*-
"""
Created on Wed Feb  7 14:00:59 2024

@author: barath
"""

"""#Q1"""
#a
l=[['J.K.ROWLING', 'HARRY POTTER', 299031, 2001, 3407],
 ['ROBERT FROST', 'THE ROAD NOT TAKEN', 299105, 1915, 522],
 ['WILLIAM SHAKESPEARE', 'ROMEO AND JULIET', 123321, 1999, 1550]]

#b
print('Pls enter the details of the new book')
a_n=input('Enter author\'s name: ')
b_t=input('Enter book title: ')
i_n=int(input('Enter ISBN number: '))
p_y=int(input("Enter publication year: "))
n_p=int(input("Enter the number of pages: "))
l.append([a_n,b_t,i_n,p_y,n_p])

y=[]
for i in l:
    y.append(i[3])
y.sort()
L=[]
for i in y:
    for j in l:
        if i==j[3] and j not in L:
            L.append(j)
print(L)

#C
n=int(input("Enter the isbn number of the book to be deleted: "))
for i in L:
    if n==i[2]:
        L.remove(i)
print(L)
#D

print('Pls enter the details of the new book to be added')
a_n=input('Enter author\'s name: ')
b_t=input('Enter book title: ')
i_n=int(input('Enter ISBN number: '))
p_y=int(input("Enter publication year: "))
n_p=int(input("Enter the number of pages: "))
L.append([a_n,b_t,i_n,p_y,n_p])

#E
n=[]
for i in L:
    n.append(i[2])
    
for i in n:
    r=n.count(i)
    if r>1:
        n.remove(i)
        for j in L:
            if j[2]==i:
                L.remove(j)
                break
print(L)
#F
l=L
n=[]
for i in l:
    n.append(i[-1])
n.sort(reverse=True)
L=[]
for i in n:
    for j in l:
        if i==j[-1] and j not in L:
            L.append(j)
print(L)
"""Q2"""
#A
l1=[1,2,3,4,5]
l2=[20,40,50,70,90]

l3=[l1[i]+l2[i] for i in range(len(l1))]
print(l3)

#B
l4=[l1[i]*l2[i] for i in range(len(l1))]
print(l4)

#C
s=input('Give a string: ')
l5=[]
for i in s:
    if i not in l5:
        l5.append(i)
print('The unique charecters present are:',l5)


"""3"""
m1=[[1,2,3],[4,5,6],[7,8,9]]
m2=[[10,20,30],[40,55,60],[70,80,90]]

m=[]
for i in range(len(m1)):
    z=zip(m1[i],m2[i])
    z=list(z)
    m.append(z)

#A
m3=[]
for i in m:
    l=[]
    for j in i:
        l.append(j[0]+j[1])
    m3.append(l)
print(m3)
    
#B
m4=[]
for i in m:
    l=[]
    for j in i:
        l.append(j[0]*j[1])
    m4.append(l)
print(m4)


"""Q4"""
#let us take the same lists m1 defined above
print('The square matrix is ',m1)

#A
for i in range(len(m1)):
    print('The row',i+1,'sum = ',sum(m1[i]))
    
for i in range(len(m1)):
    s=0
    for j in range(len(m1)):
        s+=m1[j][i]
    print('The column',i+1,'sum = ',s)

t=0
for i in range(len(m1)):
    t+=m1[i][i]
print('Trace of the matrix= ',t)

#B
t=[]
for i in range(len(m1)):
    s=[]
    for j in range(len(m1)):
        s.append(m1[j][i])
    t.append(s)
print('The tranpose of the matrix is',t)

#C
if t==m1:
    print('The matrix is symmetric')
else:
    print('The matrix is not symmetric')

#D
I=[[1,0,0],
   [0,1,0],
   [0,0,1]]
x=[[1],
   [2],
   [3]]
xt=[1,2,3]
l1=[]
for i in range(3):
    s=0
    for j in range(3):
        s+=I[i][j]*xt[i]
    l1.append(s)
s=0
for i in range(3):
    s+=l1[i]*xt[i]
print(s)


"""Q5"""
p= [[3], [1, 3, 2], [0, 1, 9, 3, 5, 7], [9, 10], [13, 14, 16, 17]]
r=list(range(1,6))
w=[]
for i in p:
    for j in i:
        if j not in r:
            w.append(i)
            break
for i in w:
    p.remove(i)
    
print('After removing the sublists ',p)



















    
 















