# Finding polynomial using lagrange interpolation
from scipy.interpolate import lagrange

# Specify the x and f(x) data sets in array
n=int(input("Enter the number of datapoints :"))
x=[]
y=[]
for i in range(n):
    x1=int(input("Enter the value of x :"))
    x.append(x1)
for i in range(n):
    y1=int(input("Enter the value of f(x):"))
    y.append(y1)
# Using in_build lagrange function on a variable  to find polyomial
f=lagrange(x,y)

# Printing the polynomial
print("The unique polynomial using lagrange interpolation is")
print(f)