PART 1
1.Write a program (WAP) to implement the following operations on a collection of library books:

(a) Construct a catalog of books, with each book having an author's name, book title, ISBN number, publication year, and number of pages.

(b) Add a new book to the catalog, ensuring that the books are kept in ascending order based on the publication year.

(c) Locate a book by its ISBN number and delete the book's entry from the catalog.

(d) Insert a new book entry at the end of the catalog using the provided book information.

(e) Identify and remove any duplicate entries in the catalog, preserving only one copy of each book based on its ISBN number.

(f) Reorganize the entire catalog so that the books are sorted in descending order by the number of pages.


2. Write a program using list comprehension

a) To add the corresponding elements of two lists and print the new list.

b) To perform element wise multiplication of two lists and print the new list.

c) To create a list of the unique characters of a given string. 

Eg: input = “hello” , output = [‘h’, ‘e’, ‘l’, ‘o’]


3. Using the zip function, WAP

a) To add the elements of 2 matrices (Define matrices as per your wish).

b) To perform element wise multiplication on 2 matrices.


 4. List of List : Given a square matrix represented as a list of lists, 

a) WAP to print the row sum, column sum and trace of the matrix 

b) WAP to print the transpose of the matrix.

c) WAP to check whether the given matrix is symmetric or not.

d) WAP to check whether the Identity matrix (I) is positive definite or not by using Quadratic form method (x^T*I*x > 0), where x is any non zero vector.

5.  List of Lists : WAP to remove sub lists from a given list of lists that contain an element outside a given range.

Example :

Input : [[3], [1, 3, 2], [0, 1, 9, 3, 5, 7], [9, 10], [13, 14, 16, 17]]  Range: 1, 5

Output : [[3], [1, 3, 2]]

Explanation : If a sublist has a number that is other than 1, 2, 3, 4, 5, remove the sublist from the list of lists and print the remaining sublists as a lists of lists

PART 2

6. List comprehension  : Given two lists of equal length, list1 contains the integers and list2 contains alphabets. Using list comprehension, WAP

a) To generate a list containing the squares of elements from list1.

b) To generate a list containing pairwise corresponding elements in the form of tuple.

c) To generate a list containing all possible combinations of elements from the two lists.

d) To generate a list containing elements of list1 and list2 alternatively.

Example:

Input:

list1 = [1,2]   list2 = ['a','b']

Output:

a) [1, 4]

b) [(1,'a'), (2,'b')]

c) [(1,'a'),(1,'b'),(2,'a'), (2,'b')]

d) [1,'a',2,'b']

7. Find out the applicable methods for the list but not tuples. List them out.

8. Write a code snippet in Python that takes a string as input and returns a tuple of tuples. Each inner tuple should contain a character from the input string and its corresponding ASCII value.

Sample example: Input_string = "Design",  Output_tuple = (('D', 68), ('e', 101), ('s', 115), ('i', 105), ('g', 103),('n', 110) )

9. Create a program that takes a list of tuples containing student name and roll number and returns a new list of tuples containing only those tuples whose first element is a vowel (a, e, i, o, u, A, E, I, O, U).

Sample example: list_of_tuples = [("aditi", 1), ("tanya", 2)], Output_list_of_tuples = [("aditi", 1)]

10.  Create a set of all numbers between 1 and 20 that are either divisible by 3 or 5, using set comprehension.

11. What is a frozenset()? Give examples.

