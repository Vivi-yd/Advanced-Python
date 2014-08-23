# some usages - Vivi and ashu
from math import sqrt

# distance between 2 points in 2D plane
dis2pt = lambda x, y : sqrt((x[0] - x[1])**2 + (y[0] - y[1])**2)

print dis2pt((0, 0), (0, 1))


# kinetic energy of an object with mass m and speed v.
E_k = lambda m, v : (m*(v**2))/2.0

print E_k(2, 1)

print "==============================="


print "lambda with Mapping"

# map being applied to one sequence 

seq = range(1, 11)
d = map(lambda x: x**5, seq)
print d

print "------------------"


# map being applied to three sequences - sequences have to be of same length

even = [2, 4, 6, 8, 10]
odd = [1, 3, 5, 7, 9]
prime = [11, 13, 17, 19, 23]

new_list = map(lambda x,y,z: (x+y) * z, even, odd, prime)
print(new_list)

print "------------------"

mass = [1, 2, 3, 4, 5]
height = [10, 20, 30, 40, 100]

# calculating the potential energy of given mass at given height

potential_energies = map(lambda m, h: m*h*9.8, mass, height)
print potential_energies

print "==================================="

print "lambda with Filtering"

# filtering a sequence after applying lambda funtion

weight_in_lb = [1/3, 1, 2, 3, 4, 5, 10, 100]

# return a list of weight greater than 2kg
two_kg_up = filter(lambda lb : lb/2.2 > 2.0, weight_in_lb)

# return a list of weight smaller than 1kg
one_kg_down = filter(lambda lb : lb/2.2 < 1.0, weight_in_lb)

print two_kg_up
print one_kg_down

print "================================="

print "lambda with Reducing"

# reducing continually apply the function to the sequence and return a single value.

lst1 = range(1, 6)
lst2 = range(1, 11)
factorial_six = reduce(lambda m, n: m*n, lst1)
factorial_ten = reduce(lambda m, n: m*n, lst2)

print factorial_six
print factorial_ten

