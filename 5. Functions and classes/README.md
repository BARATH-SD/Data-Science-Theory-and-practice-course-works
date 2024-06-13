PART 1

1. Write a program(WAP) using loops and recursion: 

a) Factorial of n where n is a non negative integer. 

b) For calculating the Nth Fibonacci number.

c) To calculate a^b where a>0, b>=0.

2. Query for 2 integers N and M from the user where 0<=N<=100 and 0<=M<=9. These will be the inputs to your function. Using recursion, compute the number of times the integer M occurs in all non-negative integers less than or equal to N.
example: For N=13 and M=1, count=6 (numbers 1,10,11,12,13).

3. Programs using lambda function.

a) Given a list of names, use map to create a list where each name is prefixed with "Hello, ".

Example Input: ['Alice', 'Bob', 'Charlie']
Example Output: ['Hello, Alice', 'Hello, Bob', 'Hello, Charlie']
b) Use filter and a lambda function to extract all even numbers from a given list.

Example Input: [1, 2, 3, 4, 5, 6]
Example Output: [2, 4, 6]
c) Use reduce and lambda to concatenate all strings in a given list.

Example Input: ['Python', 'is', 'awesome']
Example Output: 'Pythonisawesome'
4.  Define a class Complex that defines a complex number with attributes real and imaginary (as we did in the class). Define operators for addition, subtraction, multiplication and division (Do with both operator overloading as well as without overloading). While printing the output, print in the form of complex number form like ( a + ib)  - 10 marks ( 1 mark each for each of the operations with and without operator overloading)

PART2

5. WAP to implement a class called "Bank_Account" representing a person's bank account.
The class should have the following attributes: account_holder_name (str), account_number(int), address (str) and balance (float).
The class should have methods to implement the following:
    deposit - Deposits a given amount into the account
    withdraw - Withdraws a given amount from the account
    check_balance - To get the current balance
    update_details - To update the name and address from the user and displays a message indicating successful update
    display_details - To display the details of the account.

6.  Define a Matrix class of dimensions m X n (the values for m and n can be taken as input). Demonstrate matrix addition, subtraction, multiplication, element-by-element multiplication, scalar multiplication (use map here). Use operator overloading wherever possible. (Hint: In the constructor, use 'random' and create list of list using list comprehension. In the arguments of constructor, send the number of rows and columns)
Ensure that your implementation follows best practices for class design and encapsulation in Python. Comment your code to explain the functionality of each method.

7. Create a Python class named Time that represents a moment of time. The class should have attributes hour, minute, and second. Include the following features:
    A constructor that initializes hour, minute, and second, with validation to ensure each attribute is within its correct range (hours: 0-23, minutes: 0-59, seconds: 0-59).
    A __str__() method that returns the time in a format hh:mm:ss.
    Methods set_time(hour, minute, second) and get_time() to update and access the time, respectively.
    An add_seconds(seconds) method that adds a given number of seconds to the current time object, adjusting the hour, minute, and second attributes accordingly.

8.  Create a class named Geometry that provides static methods for various geometric calculations, such as area and perimeter, for different shapes (circle, rectangle, square). Include:
Static methods like circle_area(radius), rectangle_area(length, width), and square_area(side).
Static methods for perimeter calculations for the above shapes.
Ensure that methods check for valid inputs (e.g., positive numbers).

