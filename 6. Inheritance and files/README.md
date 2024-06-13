PART 1
1.Design a class named Polygon that initializes with the length of a side. Then, derive a class named Square from the Polygon class. Utilize the side length defined in the Polygon class for the Square class. Within the Square class, implement a method called findArea() that calculates and returns the square's area based on its side length. Use __init__() for necessary initialization

     2.  (a)  Create a class Father with attributes

                    - father_name (string), father_age (int), father_talents (set of strings)

                Create a class Mother with attributes:

                    - mother_name (string), mother_age (int), mother_talents (set of strings)

                 Create a class Child that inherits both father and mother with attributes: 

                    - child_name (string), child_age (int), child_gender(string)

           (b) Create a function getChildDetails() in Child to input the details of the child, it’s father and mother and printChildDetails() to print the details using     printChildDetails()

          (c) Create an object of class Child and read the details by invoking getChildDetails() and display the details entered.

          (d) Create a function displayTalents() in class Child that displays the talents of the child inherited from father and mother. A talent is inherited to a child if both

              the parents possess it.



     3.  Text File Input Output

         Create a .txt (text) file and use the pledge of India as the content of the text file.

         Write a python program that reads this text file, processes it by counting the number of occurrences of each word in the file, and then writes the result back to a          new text file.



    4.  For a restaurant, create a parent class ‘Bill’ which has the properties as ‘Customer  name’, ‘Table Number’ and ‘Order’ of which the name, order are strings and table  number is a positive integer. Define a method to extract the order details from the string and return a 2-D array of ordered items & their number. Create a child class ‘ 'Restaurant Bill’ which has a property called ‘Price list’ of the items and has a method to calculate the total bill amount by using the price list and order details. Also have a   method to print the complete bill for the customer including taxes and service charges.

     The strings will be of the following format:

     #Name: “Akshay” (Name of the customer)

     #Table Number: 7 (Table Number)

     #Order: “Item1x1,Item2x3,Item3x1,…” (ItemxNumber needed)

     #Price List: “Item1-100,Item2-70,Item3-250,...” (Item-Price)



    5. For the previous question( restaurant Bill) - take name, table no, order details from a file, price list from another file and print the whole bill to the new file.

PART 2

6.    Create a base class Vehicle with the following attributes:

         make (string)

         model (string)

         year (int)

       Create a method initialize_vehicle to set the above attributes. Also, create a method display_vehicle to print these attributes.

       Create a class Car inherited from Vehicle with the following additional attribute:

         fuel_type (string)

       Create a method get_car_details to initialize the above attribute along with Vehicle attributes.

       Also, create a method display_vehicle to print these attributes along with Vehicle attributes.

       Create a class Bike inherited from Vehicle with the following additional attribute:

           gear_count (int)

      Create a method get_bike_details to initialize the above attribute along with Vehicle attributes.

      Also, create a method display_vehicle to print these attributes along with Vehicle attributes.

      Create two different objects for Car and Bike and demonstrate each of the methods.

     Example -1:

         my_car = Car()

        my_car.get_car_details("Toyota", "Camry", 2020, "Petrol")

        my_car.display_vehicle()

        Output:

           Make: Toyota, Model: Camry, Year: 2020

           Fuel Type: Petrol

          Example -2 :

           my_bike = Bike()

           my_bike.get_bike_details("Yamaha", "YZF R1", 2021, 6)

           my_bike.display_vehicle()

          Output:

             Make: Yamaha, Model: YZF R1, Year: 2021

             Gear Count: 6



7. Suppose you are building a Python program to manage a school's student data. You need to create a Student class that contains information such as the student's name, age, grade, and class schedule. Additionally, there are some attributes that are shared by all students, such as the school name, the total number of students, and the number of classes offered.

How can you use class variables in Python to define these shared attributes of the Student class? What are the advantages of using class variables in this scenario? Can you provide an example program that demonstrates the use of class variables in the Student class? 



8. Class Inheritance in Python: Finding GCD (greatest common divisor) and LCM (least common multiple) of Numbers and Handling Composite Numbers.


a) Create a Numbers class with a, b, find_gcd(), and find_lcm() methods.

b) Create an EvenNumbers class that inherits from Numbers and overrides find_lcm() to handle even numbers.

c) Create an OddNumbers class that inherits from Numbers and overrides find_lcm() to handle odd numbers.

d) Create a CompositeNumbers class that inherits from EvenNumbers and OddNumbers and overrides find_gcd() to handle composite numbers.

e) Create a CompositeNumbers object with a = 12 and b = 9, and call its find_lcm() and find_gcd() methods.



9. WAP to manage the collections of books in a library in the following  manner:

 Create a Python script that can both read from and write to a CSV file, containing details about each book. Each book's information will include its title, author, publication year, and ISBN number. Your script should be capable of adding new books to the CSV file and listing all the books currently stored in the file.

The program should begin by checking if the CSV file exists. If it does not, your script should create it and initialize it with the appropriate headers. Then, there should be 2 options: to add a new book or to display all books. When adding a new book, the user should be prompted to enter the title, author, publication year, and ISBN number. This new book should then be added to the CSV file without overwriting the existing entries. When choosing to display all books, the script should read from the CSV file and print each book's details.

10. WAP to create a pandas dataframe with a list of words and sort them in ascending order. The sorted words should be copied to a new file.

