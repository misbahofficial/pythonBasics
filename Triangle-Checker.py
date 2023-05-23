'''
Determine if the given lengths can form a triangle,
you need to apply the triangle inequality theorem.
According to this theorem, in a triangle,
the sum of the lengths of any two sides must be greater
than the length of the third side.

Let's say you have three line lengths: a, b, and c.
To check if they can form a triangle, you need to verify the following conditions:

a + b > c
a + c > b
b + c > a

If all three conditions are satisfied,
then the lengths a, b, and c can form a triangle.
If any one of the conditions is not met,
then it is not possible to form a triangle with those lengths.

'''


def is_triangle(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        return True
    else:
        return False

# Example usage
length1 = float(input("Enter the length of the first side: "))
length2 = float(input("Enter the length of the second side: "))
length3 = float(input("Enter the length of the third side: "))

if is_triangle(length1, length2, length3):
    print("The lengths can form a triangle.")
else:
    print("The lengths cannot form a triangle.")



