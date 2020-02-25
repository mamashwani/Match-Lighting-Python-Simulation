#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Muhammad Mashwani
PeopleSoft ID: 1378052
Homework #3
"""

def GCD(a,b): # Compute the GCD of the two numbers
    while b > 0:
        a,b = b, a%b # What is this? We'll learn about it in 2 weeks!
    return a

def get_char(x,y): # Get the character for some coordinate         
    if x == 0 and y == 0: # Is this point at the origin?
        return 'L' # The laser goes there
    if GCD(x,y) == 1: # Wow that was easy!
        return '*'
    else:
        return '.'
    
# To Do: Put this into a function!
def get_width():
    while True: # Loop until we get an answer
        try: # Just try this out and hope nothing goes wrong
            width = int(float(input("Please enter the width of the of the field: "))) # Get an integer size
            break # If we make it to here, we got a size, not problem
        except ValueError: # Oops, there was a problem
            print("Invalid value, Please try again.") # Let the user know there was a problem
            # The while loop is done here    
    return width
def get_height():
    while True:
        try:
            height = int(float(input("Please enter the height of the of the field: ")))
            break
        except ValueError:
            print("Invalid value, Please try again.")
    return height
            
print("Laser field simulation… ")
output_file = input("Please enter the name of the output file: ")
width = get_width()
height = get_height()
total = 0
field = [] # This holds the field that we are simulating, a list of rows
for y in range(height): # This is how many rows we are going to simulate
    line = [] # This holds one line or row at a time
    for x in range(width): # This is how many columns there are in each row
        line.append(get_char(x,y)) # Here we build up each line given the x and y position
        
    # The x-loop is done here    
    field.append(line) # Here we add the row in with the rest to build the field
    total += line.count("*")
# The y-loop is done here
unlit_matches = (width*height) - total - 1
field.reverse() # Why did we do this? In order to bring the laser to the bottom left corner because the
                # field each line gets appended to field in a top-down format

# To Do: Put this into a function!
def print_field():
    for line in field: # Look at all the lines in the field, one at a time
        print("".join(line)) # Join them together and print them out

if height < 80 and width < 80:
    print_field()
    output = open(output_file, "w")
    for line in field:
        output.writelines(line)
        output.write("\n")
    output.close() 
elif height >= 80 or width >= 80:
    output = open(output_file, "w")
    output.write("The total of lit matches is {}.\n".format(total))
    output.write("The total of unlit matches is {}.\n".format(unlit_matches))
    output.close()
    
#print("The total of lit matches is {}.".format(total))# This outputs the total, we'll need this
#print("The total of unlit matches is {}.".format(unlit_matches)) #outputs the total of unlit matches

print("Simulation complete!")

"""
for 1000x1000 field:
The total of lit matches is 607585.
The total of unlit matches is 392414.
"""