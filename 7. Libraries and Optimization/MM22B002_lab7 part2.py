# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 21:39:03 2024

@author: barath
"""

"""Q6"""
import matplotlib.pyplot as plt
import numpy as nm
t=nm.linspace(0,10*nm.pi,1000)
x,y=nm.cos(t),nm.sin(t)
z=t

fig = plt.figure(figsize=(12,6))
ax = fig.add_subplot(121, projection='3d')
ax.scatter(x,y,z,label='Helical Wave')
ax.set_xlabel('X(Cos(t)')
ax.set_ylabel('Y(Sin(t)')
ax.set_zlabel('Z(t)')
ax.set_title('Helical Wave(Scatter)')
ax.legend()


ax = fig.add_subplot(122, projection='3d')
ax.plot(x,y,z,c='r',label='Helical Wave')
ax.set_xlabel('X(Cos(t)')
ax.set_ylabel('Y(Sin(t)')
ax.set_zlabel('Z(t)')
ax.set_title('Helical Wave(Line)')
ax.legend()
plt.show()



"""Q6"""
import pandas as pd
c= {
    "1": {"Country": "New Country 1",
          "Capital": "New Capital 1",
          "Population": "123,456,789"},
    "2": {"Country": "New Country 2",
          "Capital": "New Capital 2",
          "Population": "987,654,321"},
    "3": {"Country": "New Country 3",
          "Capital": "New Capital 3",
          "Population": "111,222,333"}
}
print(pd.DataFrame(c).T)

"""Q7"""
s='''Date;Event;Cost
    10/2/2011;Music;10000
    11/2/2011;Poetry;12000
    12/2/2011;Theatre;5000
    13/2/2011;Comedy;8000
    '''
l=s.split()
d=[i.split(';') for i in l]
df=pd.DataFrame(d[1:],columns=d[0])
print(df)

"""Q8"""
m=nm.array([[1,2,3],[4,5,6],[7,8,9]])
print('Transpose of the matrix\n',m.transpose())
print('The flattend form\n',m.flatten())

"""Q9"""
i={'Name': ['john', 'bODAY', 'aNa', 'Peter', 'nicky'], 'Education': ['masters', 'graduate', 'graduate', 'Masters', 'Graduate'], 'Age': [27, 23, 21, 23, 24]}
df=pd.DataFrame(i)
l=df['Name']
L=[]
for j in list(l):
    L.append(j.title())
df['Name']=L
print(df)

d=df.to_dict('list')
print(d)


"""Q10"""
def f(x):
    return(3*x**2 + 2*x)

def first_der(x,h):
    return(f(x+h)-f(x-h))/(2*h)
def second_der(x,h):
    return(f(x+h)+f(x-h)-2*f(x))/(h**2)

x=1
h=0.1
print(first_der(x,h))
print(second_der(x,h))



