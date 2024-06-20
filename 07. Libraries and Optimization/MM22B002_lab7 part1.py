# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 14:00:20 2024

@author: barath
"""

"""Q1"""
import numpy
import matplotlib.pyplot as plt
import pandas as pd

print('Ax^4 + Bx^3 + Cx^2 + Dx + E')
A=float(input('Enter the value of A :'))
B=float(input('Enter the value of B :'))
C=float(input('Enter the value of C :'))
D=float(input('Enter the value of D :'))
E=float(input('Enter the value of E :'))

x=numpy.arange(-100,100,1)
y=A*x**4+B*x**3+C*x**2+D*x+E
plt.plot(x,y,'r')
plt.xlabel('Input')
plt.ylabel('Output')

"""Q2"""
sales_data = {
    'Product': ['A', 'B', 'A', 'C', 'B', 'C', 'A', 'B', 'C'],
    'Month': ['Jan', 'Jan', 'Feb', 'Feb', 'Mar', 'Mar', 'Apr', 'Apr', 'Apr'],
    'Sales': [100, 150, 200, 120, 180, 220, 90, 110, 130]
    }

sales_df=pd.DataFrame(sales_data)
prod=sales_df.Product
sal=sales_df.Sales
a=b=c=0
for i in range(len(prod)):
    if prod[i]=='A':
        a+=sal[i]
    elif prod[i]=='B':
        b+=sal[i]
    elif prod[i]=='C':
        c+=sal[i]
        
x=['A','B','C']
y=[a,b,c]
plt.bar(x,y)

"""Q3"""
import math
x=numpy.linspace(-10,10,101)

#1
y=numpy.cos(x)
plt.plot(x,y,'g')
plt.xlabel('x')
plt.ylabel('cos(x)')
plt.title('Graph of cos(x)')

#2
y=math.e**x
plt.plot(x,y,'r')
plt.xlabel('x')
plt.ylabel('e^x')
plt.title('Graph of e^x')

#3
y=[]
X=[]
for i in x:
    if i>0:
        X.append(i)
        y.append(math.log(i))
plt.plot(X,y,'r')
plt.xlabel('x (x>0)')
plt.ylabel('log(x)')
plt.title('Graph of log(x)')

#1 z = cos(sqrt(x^2+y^2)
x=numpy.linspace(-10,10,101)
y=numpy.linspace(-10,10,101)
X,Y=numpy.meshgrid(x,y)
z=(X**2+Y**2)**0.5
Z=numpy.cos(z)
fig=plt.figure()
ax=fig.add_subplot(111,projection='3d')
ax.plot_surface(X,Y,Z)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')


#2 z = e^(-(x^2+y^2))
Z=math.e**(-1*(X**2+Y**2))
fig=plt.figure()
ax=fig.add_subplot(111,projection='3d')
ax.plot_surface(X,Y,Z)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

#3 z= log(x^2+y^2) where x^2+y^2>0
x=numpy.linspace(-10,10,101)
y=numpy.linspace(-10,10,101)
Z=numpy.log(X**2+Y**2)
fig=plt.figure()
ax=fig.add_subplot(111,projection='3d')
ax.plot_surface(X,Y,Z)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')


"""Q4"""
# J(w) = w^2 + (54/w) let a=1 b=10 n=9
def J(w):
    return(w**2+52/w)

def brkt(a,b,n):
    x=(b-a)/n
    w1=a
    w2=w1+x
    w3=w2+x
    for i in range(n):
        if J(w1)>=J(w2)<=J(w3):
                return w1, w3
        else:
            w1=w2
            w2=w3
            w3=w2+x
            
c=sum(brkt(1,10,9))/2
print('The approx minimum is :',c)


