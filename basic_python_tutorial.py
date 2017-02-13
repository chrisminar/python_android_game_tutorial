# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 01:17:02 2017

@author: Chris Minar
"""

#
# Variables / Members
#
print "Variable section"
print '-'*50
#Make a variable a equal to the integer 5
a = 5
#print a and the type of a
print a, type(a)

#set a to be a floating point number
a = 5.5
print a, type(a)

#set a to be a boolean
a = False
print a, type(a)

#set a to be a sting
a = 'hello'
print a, type(a)

#set a to be a list
a = [0,2,4]
print a, a[1], type(a)
#change one value of a
a[2] = 3
print a
#add an element to the end of a....
a.append(5)
print a

#Now you try...
#make your own list of integers
#try to access the different elements of the list, remember the first element of the list is spot 0
#What happens if you try to access a number lower than 0? e.g. -1
#What happens if you try to access a number that isn't an integer? e.g. 1.5
#Try to make with different data types in it, i.e. a list with both integer elements and float elements
#Can you make a list of lists?

#
# Math in python
#
print "\nMath section"
print '-'*50
#In python 2.7 division, if both numbers are integers then the output will also be an integer
print 1/2

#this can be fixed several ways
print 1/2.0, 1/2., 1.0/2, 1./2

# if you enter the line: from __future__ import division you can do division between two ints without any problems
#print 1/2

# instead of ^ for an exponent symbol, python uses **
print 2**2, 2**3, 2**4

#the modulus function can be used to get the remainder of a division
print 5%4
print 6%4

#More advanced math require you to import functions from the math library, more on functions later
import math
#accessing the math library is done with a math.something
#for example we can tak the cosine of pi by...
print math.cos(math.pi)

#
# Statements and loops
#
print "\nStatement and loops section"
print '-'*50
#if statements can be used to test things
a = 5
if a > 0:
    print "a is greater than 0!"
    
#for loops are used to 'loop' over a know ammount of iterations
for i in range(10):
    print i
    
#you can combine loops and statements
for i in xrange(10):
    #if i is less than 5...
    if i < 5:
        print "less than 5"
    #else if i is 5...
    elif i == 5:
        print "i is 5"
    #in all other cases...
    else:
        print "i is greater than 5"

#while loops are used when you have an unknown number of iterations
i = 2
count = 0
while i < 256:
    #multiply i by 2
    i = i * 2
    #count how many times we step though the while loop
    count = count + 1
print count


#Now you try...
#make a for loop that counts by 2 from 0 to 100
#do the same thing with a while loop
#make a for loop that counts by 1 from 0 to 100 but only prints if its devisible by two



#
# Functions / Methods
#
print "\nFunction section"
print '-'*50
# you can define a funciton that will do tasks
#the classic, hello world
#define the function
def say_hello():
    print "Hello World!"
#call the function
say_hello()

#let's make a function to add two numbers together
def addition(x,y):
    return x+y
#call the function
z = addition(2,2)
#test if the function was correct
if z == 4:
    print "the function worked correctly!"
else:
    print "the function didn't work :("
    
#Now you try...
#make and call a function that multiplies two numbers
#bonus problem: (hint: do this in the order it is presented)
    #make a list with 10 numbers in it
    #make a funciton that compares two numbers and returns True if the second number is larger and False is the first number is larger
    #make a second function that takes a list as an input and returns a differnet list of booleans that compares each number in the input array using the previous function
    
    
#lets talk about scope
def addition(d,e):
    f = d + e #this is the first line in the scope of the function addition
    return f #this is the last line in the scope of the function addition
    
#everything inside of a scope is lost after we move out of the function
#for example if we call the function addition now, like so
print addition(5,3)
#we can't access the variable f
try:
    print f
except NameError:
    print 'The name f is not defined'
    



