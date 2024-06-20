PART 1
1. Explore the use and syntax of common built-in functions: 

range(), 

iter(), 

eval(), 

enumerate(), 

zip(), 

lambda, 

input(), 

map(), 

filter(), 

next()

reduce()

Include a short description and a practical code example for each, ensuring clarity through comments.


2. Write a Python function that sorts a dictionary based on the length of values.

Sample:

Input: {'lemon':'yellow','apple':'red'} output: {'apple':'red','lemon':'yellow'}

3. Develop a Python program that executes the following tasks with a user-provided string:

a. Prompt the user to input a string.

b. Create a dictionary from the string where each key is a unique alphabet character and the corresponding value is the frequency of that character's occurrence in the string.

c. Generate a sorted list of tuples from the dictionary based on character frequency (values).

d. Generate a sorted list of tuples from the dictionary based on the alphabet characters (keys).

e. Identify the three most frequently occurring characters. In the event of a frequency tie, prioritize characters in lexicographical order.

Your program should showcase proficiency in dictionary operations, sorting mechanisms, and handling of ties in frequency counts. Comment your code to outline the process and decisions made.

sample:

input = 'GOOGLE'

Here, the most repeated characters are G:2, O:2. But, L,E are occurring only a single time which is tied for the third position here, so here we take E as it comes first in the lexicographical order.


4. Write a function called lookup_student that takes a dictionary representing student records, where names are keys and roll numbers are values. The function should search for a specified student name and return the corresponding roll number if found; otherwise, it should return "Not Found" 

Example:

records = { "Alice" : "AB111", "Bob" : "EE200", "David" : "XY333"}

print(lookup_student(records, "Bob")) : Should print "EE200"

print(lookup_student(records, "John")) : Should print "Not Found"


5. Given a list of integers, write a Python program to:

a) Find the frequency of each integer in the list and store the result in a dictionary.

b) Print the maximum integer and its frequency.

c) Remove duplicates from the list and print the new list without changing the order of elements. Do this operation without using the set data type.

d) Remove duplicates from the list and print the new list. Do this operation using the set data type.

PART 2
6. Store the employee IDs, names, salaries, and years of experience using nested dictionaries (the key of the highest level dictionary can be the employee ID). 

a) Sort this dictionary using the salary value. 

b) Add a new employee to the dictionary in the correct position (sorted as mentioned above).

7. You are given two Python dictionaries, A and B, with keys as alphabets and values as random integers. Write a Python function to create a third dictionary C, that combines A and B. For common keys, the value in C should be the sum of values from A and B. 

For example, if dictionary A is {"a": 3, "b": 5, "c": 7} and dictionary B is {"b": 2, "c": 4, "d": 6}, the function should return a dictionary C that looks like {"a": 3, "b": 7, "c": 11, "d": 6}.

 8. Assume you have a list of lists, where each inner list contains two elements: a key and a value. Write a Python function that takes the list of lists as input and returns a list of dictionaries, where each dictionary contains a key-value pair from the original input list.

9. Illustrate the usage of positional and keyword arguments using suitable examples.

10. Write a function to find the maximum of n numbers using variable length positional arguments.

11. Write a function to concatenate n strings using variable length keyword arguments.
