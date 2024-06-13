# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 14:12:07 2024

@author: barath
"""

"""Q1"""

#A

import numpy as nm
import matplotlib.pyplot as plt
x=nm.linspace(-20,20,1000)
y=1/(1+nm.e**(-x))
plt.plot(x,y)
plt.title('Sigmoid function')
plt.xlabel('z values')
plt.ylabel('sigma(z)')
plt.show()
print('In binary classification problems, the sigmoid is particularly is useful\
 in the output layer. It can turn arbitary real-valved numbers into probabilities,\
which are easier to interpret.')


#B
h_x=nm.linspace(0.000001,0.9999999,1000)
fig=plt.figure(figsize=(12,6))
ax=fig.add_subplot(121)
c1=-(nm.log(h_x))
plt.plot(h_x,c1)
plt.title('-log function (y=1)')
plt.xlabel('values')
plt.ylabel('-log')

ax=fig.add_subplot(122)
c2=-(nm.log(1-h_x))
plt.plot(h_x,c2)
plt.title('-log(1-z) function (y=0)')
plt.xlabel('values')
plt.ylabel('-log(1-z)')
plt.show()

print('b) Cross entropy cost funct. is convex,a variety of local optimisation schemes\
      can be more easily used to properly minimize it. For this reason, this\
          cross entropy cost funct. is used more often in logistic regression than in linear regression.')

#C
x=[1,2,3,4,5,6,7,8,9,10]
y=[0,0,0,0,0,1,1,1,1,1]
plt.plot(x,y)

#linear regression

m=len(y)
w=nm.zeros(2) #w_o and w_1
def h(x,w):
    y_n=list()
    for i in x:
        y_n.append(w[0]+w[1]*i)
    return y_n
def J(x,y,w):
    y_n=h(x,w)
    j=0
    for i in range(m):
        j+=(y[i]-y_n[i])**2
    return j/(2*m)
def grad_j(x,y,w):
    y_n=h(x,w)
    d_j=nm.zeros(2)
    for i in range(m):
        d_j[0]+=(y_n[i]-y[i])/m
        d_j[1]+=(y_n[i]-y[i])*x[i]/m
    return d_j
W=[]
cost=[]
for i in range(1000):
    j=J(x,y,w)   
    W.append(w)
    cost.append(j)
    w=w-0.01*nm.array(grad_j(x,y,w))
    if J(x,y,w)>j:
        break
print('w =',w,'\nThe loss = ',J(x,y,w))
W0=[]
for i in W:
   W0.append(i[0])
W1=[]
for i in W:
   W1.append(i[1])
               
plt.plot(W1,cost)
plt.title('Cost function J(w1)')
plt.xlabel('w1 values')
plt.ylabel('J(w1)')
plt.show()

fig=plt.figure(figsize=(12,6))
ax=fig.add_subplot(121,projection='3d')
A,B=nm.meshgrid(W0,W1)
w=[A,B]
C=J(x,y,w)
ax.plot_surface(A,B,C)
ax.set_xlabel('W0')
ax.set_ylabel('W1')
ax.set_zlabel('J(W0,W1)')
plt.show()    
    
fig=plt.figure(figsize=(12,6))
ax=fig.add_subplot(111)
cp=plt.contour(W0,W1,C)
plt.clabel(cp)
ax.set_xlabel('W0')
ax.set_ylabel('W1')
ax.set_title('Contour plot of J(w0,w1)')
plt.show()
    
#logistic regression

x=[1,2,3,4,5,6,7,8,9,10]
y=[0,0,0,0,0,1,1,1,1,1]
plt.scatter(x,y)

m=len(y)
w=[0,0]
def h(x,w):
    y_n=[]
    for i in x:
       y_n.append(1/(1+(nm.e**(-(w[0]+w[1]*i)))))
    return y_n

def J(x,y,w):
    y_n=h(x,w)
    j=0
    for i in range(m):
        if y[i]==0:
            j+=(-nm.log(1-y_n[i]))
        else:
            j+=(-nm.log(y_n[i]))
    return j/m

def grad_j(x,y,w):
    y_n=h(x,w)
    d_j=[0,0]
    for i in range(m):
        d_j[0]+=(y_n[i]-y[i])/m
        d_j[1]+=(y_n[i]-y[i])*x[i]/m
    return d_j

W=[]
cost=[]
for i in range(1000):
    j=J(x,y,w)   
    W.append(w)
    cost.append(j)
    w=w-0.01*nm.array(grad_j(x,y,w))
    if J(x,y,w)>j:
        break

print('w =',w,'\nThe loss = ',J(x,y,w))

W0=[]
for i in W:
   W0.append(i[0])
W1=[]
for i in W:
   W1.append(i[1])
               
plt.plot(W1,cost)
plt.title('Cost function J(w1)')
plt.xlabel('w1 values')
plt.ylabel('J(w1)')
plt.show()


fig=plt.figure(figsize=(12,6))
ax=fig.add_subplot(121,projection='3d')
A,B=nm.meshgrid(W0,W1)
l=[A,B]
C=J(x,y,l)
ax.plot_surface(A,B,C)
ax.set_xlabel('W0')
ax.set_ylabel('W1')
ax.set_zlabel('J(W0,W1)')
plt.show()    
    
fig=plt.figure(figsize=(12,6))
ax=fig.add_subplot(111)
cp=plt.contour(W0,W1,C)
plt.clabel(cp)
ax.set_xlabel('W0')
ax.set_ylabel('W1')
ax.set_title('Contour plot of J(w0,w1)')
plt.show()
