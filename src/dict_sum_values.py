'''
Created on Jul 7, 2014

@author: viejoemer

How to sum all the values from a dict in Python?

¿Cómo sumar todos los valores de un dict en Python?

Sums start and the items of an iterable from left to 
right and returns the total. start defaults to 0. The 
iterable‘s items are normally numbers, and the start 
value is not allowed to be a string.
'''

#Creating a dictionary.
seq = ("value_one", "value_two", "value_three")
d = dict.fromkeys(seq,40)
print(d)

#Sum all the values from a dict.
s = sum(d.values())
print(s)
