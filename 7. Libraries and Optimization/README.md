PART 1

1. Write a program that takes coefficients A, B, C, D, and E as inputs representing a 4th degree polynomial in the form Ax^4 + Bx^3 + Cx^2 + Dx + E. Calculate the values of this polynomial for x in the range from -100 to 100, with constant discrete intervals.

Store the resulting x and y values as a NumPy array, where x represents the input values, and y represents the corresponding output values of the polynomial. Finally, use Matplotlib to plot the graph using the generated NumPy array.

2. Suppose you have a dictionary containing information about monthly sales for different products over a period of time. The dictionary has the following structure.

sales_data = {

    'Product': ['A', 'B', 'A', 'C', 'B', 'C', 'A', 'B', 'C'],

    'Month': ['Jan', 'Jan', 'Feb', 'Feb', 'Mar', 'Mar', 'Apr', 'Apr', 'Apr'],

    'Sales': [100, 150, 200, 120, 180, 220, 90, 110, 130]

}

Write a Python script to convert this dictionary into a pandas DataFrame, calculate the total sales for each product over the entire period, and then create a bar plot using matplotlib to visualize the total sales for each product.

3. Create visualizations for the following mathematical functions using Matplotlib:

Plot the following single-variable functions over the range 

[−10,10], and include a title and labels for the axes:

(1) y = cos(x)

(2) y = e^x

(3) y = log(x), where x>0


Generate surface plots for these multi-variable functions over the range 

x=[−10,10] and y=[−10,10] , ensuring to add a title and labels for all axes:

(1) z = cos(sqrt(x^2+y^2)

(2) z = e^(-(x^2+y^2))

(3) z =  log(x^2+y^2) where x^2+y^2>0

4. For the function J(w) = w^2 + (54/w), implement the bracketing method (choose your own a, b, n).

PART 2

5. WAP to plot a 3-d graph of the helical wave signal using the scatter method and normal line method. Plot them separately and specify legend.

6.

countries = {

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

Make a data frame using pandas from dictionary of dictionary.

7.

StringData = ‘’’Date;Event;Cost

    10/2/2011;Music;10000

    11/2/2011;Poetry;12000

    12/2/2011;Theatre;5000

    13/2/2011;Comedy;8000

    ‘’’

Make a data frame using pandas from string.

8.Take a N X M integer array matrix with space separated elements ( N = rows and M  = columns). Your task is to print the transpose and flatten results using numpy

9. WAP to capitalize a column of names in a Pandas Dataframe.

Eg : Input : {'Name': ['john', 'bODAY', 'aNa', 'Peter', 'nicky'], 'Education': ['masters', 'graduate', 'graduate', 'Masters', 'Graduate'], 'Age': [27, 23, 21, 23, 24]}

Output : {'Name': ['John', 'Boday', 'Ana', 'Peter', 'Nicky'], 'Education': ['masters', 'graduate', 'graduate', 'Masters', 'Graduate'], 'Age': [27, 23, 21, 23, 24]}

10. Use the central difference method to find the first and second order derivatives of the function. Use the following function for testing the result. And also verify the result manually (Write on paper and upload jpg). Refer to section 2.5.1 of “Optimization for Engineering Design: Algorithms and Examples” by KALYANMOY DEB, 2nd edition


f(x) = 3x**2 + 2x


