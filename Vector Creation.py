"""
Created on Wed Oct 30 15:02:00 2018

@author: UKJTA001

Exploring the generation of a vector for use in 
"""

length = int(input("How long do you want your vector? \n"))

# Creating a row of 'l' columns
a = ([0] * length)         # Creates a row of 0s 'l' characters long

# Creates an array 'l' long with with entries 1 to 'l'
for i in range(length):    # Creates for loop between 1 and 'l'
    a[i]=i+1               # States the 'i'th entry of a is 'i'
    
print(a)

