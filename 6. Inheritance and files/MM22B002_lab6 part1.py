# -*- coding: utf-8 -*-
"""
Created on Wed Feb 28 14:00:58 2024

@author: barath
"""

"""Q1"""

class Polygon:
    def __init__(self,s):
        self._side=s

class Square(Polygon):
    def __init__(self, s):
        super().__init__(s)
    def findArea(self):
        print('The area of the square is',self._side**2)

a=Square(5)
a.findArea()

"""Q2"""
#A

class Father:
    def __init__(self,n,a,t):
        self._father_name=n
        self._father_age=a
        self._father_talents=t

class Mother:
    def __init__(self,n,a,t):
        self._mother_name=n
        self._mother_age=a
        self._mother_talents=t

class Child(Father,Mother):
    def __init__(self,n,a,g):
        self._child_name=n
        self._child_age=a
        self._child_gender=g
        
    def getChildDetails(self):               #B
        f_n=input('Enter the father\'s name: ')
        f_a=input('Enter the father\'s age: ')
        f_t=eval(input('Enter a set of father\'s talents: '))  # {'Dancing','Drawing'}
        m_n=input('Enter the mother\'s name: ')
        m_a=input('Enter the mother\'s age: ')
        m_t=eval(input('Enter a set of mother\'s talents: '))  # {'Singing','Dancing'}
        Father.__init__(self,f_n,f_a,f_t)
        Mother.__init__(self,m_n,m_a,m_t)
        
    def printChildDetails(self):
        print('Child\'s name     : ',self._child_name)
        print('Child\'s age      : ',self._child_age)
        print('Child\'s gender   : ',self._child_gender)
        print('Father\'s name    : ',self._father_name)
        print('Father\'s age     : ',self._father_age)
        print('Father\'s talents : ',self._father_talents)
        print('Mother\'s name    : ',self._mother_name)
        print('Mother\'s age     : ',self._mother_age)
        print('Mother\'s talents : ',self._mother_talents)
        
    def displayTalents(self):                                #D
        l=[]
        for i in self._father_talents:
            if i in self._mother_talents:
                l.append(i)
        print('The talents inherited are',set(l))


#C
C=Child('Harry',8,'Boy')
C.getChildDetails()

C.printChildDetails()

C.displayTalents()

"""Q3"""

with open('a.txt','w') as f:
    f.write('''India is my country,
All Indians are my brothers and
I love my country,
I am proud of its rich and varied heritage,
I shall always strive to be worthy of it,
I shall give my parents, teachers and all elders, respect, and treat everyone with courtesy,
To my country and my people, I pledge my devotion,
In their well being and prosperity alone, lies my happiness.''')

with open('a.txt','r') as f:
    s=f.read()
    l=s.replace(',',' ').replace('.',' ').split()
    d=dict.fromkeys(l)
    for i in d:
        d[i]=l.count(i)

with open('b.txt','w') as f:
        s=str()
        for i in d:
            s=s+i+' -> '+str(d[i])+',  '
        f.write(s)

with open('b.txt','r') as f:
    print(f.read())


"""Q4"""

class Bill:
    def __init__(self,c_n,t_n,o):
        self._Customer_name=c_n
        self._Table_Number=t_n
        self._Order=o
    def extract_oder(self):
        s=self._Order
        l=s.split(',')
        Order_array=[]
        for i in l:
            Order_array.append(i.split('x'))   # DarkChoclatex1,BlackCurrantx3,Butterscotchx2
        return(Order_array)
        
c_n=input('Enter Customer name: ')
t_n=int(input("Enter table number: "))
o=input('Order(ItemxNumber needed): ')

b=Bill(c_n,t_n,o)
order=b.extract_oder()
print(order)

p=input('Enter price list(Item-Price): ')     # DarkChoclate-40,BlackCurrant-45,Butterscotch-50
l=p.split(',')
price_array=[]
for i in l:
    price_array.append(i.split('-'))
print(price_array)


class Restaurant_Bill(Bill):
    def __init__(self,p):
        super().__init__(c_n,t_n,o)
        self._Price_list=p
    
    def amount(self):
        orders=self.extract_oder()
        prices=self._Price_list
        Amount=0
        for i in orders:
            for j in prices:
                if j[0]==i[0]:
                    Amount+=int(i[1])*int(j[1])
                    break
        print('The total amount is Rs',Amount)
      
    def print_bill(self):
        print('_______________THE BILL____________________')
        print('Customer name:',self._Customer_name)
        print('Table number:',self._Table_Number)
        print('_____________________________________________')
        print('Item name      Price per item x Quantity = Price')
        orders=self.extract_oder()
        prices=self._Price_list
        Amount=0
        for i in orders:
            for j in prices:
                if j[0]==i[0]:
                    Amount+=int(i[1])*int(j[1])
                    print(i[0],j[1],i[1],int(i[1])*int(j[1]),sep='          ')
                    break
        print('_____________________________________________')
        print('The total amount = ',Amount)
        print('Service charges  =  50')
        tax=Amount*0.018
        print('Tax amount       =',tax)
        print('The total bill amount(including taxes):',Amount+50+tax)


        
am=Restaurant_Bill(price_array)
am.amount()
am.print_bill()

"""Q5"""

with open('order.txt','w') as f:
    f.write('Customer_name: Dustin\n')
    f.write('Table_number: 2\n')
    f.write('Order: DarkChoclatex1,BlackCurrantx3,Butterscotchx2\n')
with open('order.txt','r') as f:
    s=f.read()
l=s.split()
for i in range(len(l)):
    if l[i]=='Customer_name:':
        c_n=l[i+1]
    elif l[i]=='Table_number:':
        t_n=l[i+1]
    elif l[i]=='Order:':
        o=l[i+1]
        break     

with open('price.txt','w') as f:
    s=f.write('DarkChoclate-40,BlackCurrant-45,Butterscotch-50')
with open('price.txt','r') as f:
    s=f.read()

l=s.split(',')
price_array=[]
for i in l:
    price_array.append(i.split('-'))
print(price_array)


b=Bill(c_n,t_n,o)
order=b.extract_oder()
print(order)

class Restaurant_Bill(Bill):
    def __init__(self,p):
        super().__init__(c_n,t_n,o)
        self._Price_list=p
    
    def amount(self):
        orders=self.extract_oder()
        prices=self._Price_list
        Amount=0
        for i in orders:
            for j in prices:
                if j[0]==i[0]:
                    Amount+=int(i[1])*int(j[1])
                    break
        print('The total amount is Rs',Amount)
      
    def print_bill(self):
        with open('bill.txt','w') as f:
            f.write('_______________THE BILL____________________\n')
            f.write(f'Customer name: {self._Customer_name} \n')
            f.write(f'Table number: {self._Table_Number} \n')
            f.write('_____________________________________________\n')
            f.write('Item name      Price per item  x  Quantity =   Price\n')
            orders=self.extract_oder()
            prices=self._Price_list
            Amount=0
            for i in orders:
                for j in prices:
                    if j[0]==i[0]:
                        Amount+=int(i[1])*int(j[1])
                        f.write(f'{i[0]}           {j[1]}           {i[1]}           {int(i[1])*int(j[1])} \n')
                        break
            f.write('_____________________________________________\n')
            f.write(f'The total amount = {Amount} \n')
            f.write('Service charges  =  50\n')
            tax=Amount*0.018
            f.write(f'Tax amount       ={tax}\n')
            f.write(f'The total bill amount(including taxes): {Amount+50+tax}')
            
am=Restaurant_Bill(price_array)
am.amount()
am.print_bill()

with open('bill.txt','r') as f:
    print(f.read())
    
