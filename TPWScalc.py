#16.10.18 Hackathon Manchester Oxford Rd
#Train Protection Warning System Calculator
import os
import math
print("TPWS Calculator")
#Input Variables
print("Input Variables")
#linespeed
linespeedmph=float( input("What is the Line Speed? (mph) "))
print("line Speed =",linespeedmph,"mph")
gradient=float( input("What is the Gradient? (1 in ?)  (+=Rising, -=Falling) "))
print("")
print
#Calculate Gradient as a percentage
gradper=round((100/gradient),3)
#Gradient in degrees
graddeg=float(math.degrees(math.atan(1/gradient)))
gradrad=float(math.atan(1/gradient))
print("Gradient = 1 in ",gradient, "Or", gradper, "% Or", graddeg, "degrees")

#Braking Characteristics
brakechar=float( input("What are the Braking Characteristics (% of g) "))
print("Braking Characteristics =",brakechar, "% of g")

#Safe Over Run
safeorun=float( input("What is the Safe Over Run Distance? (m) "))
print("Safe Over Run =",safeorun, "m")

#Trainmass
carridges=float( input("How Many Carridges does the Train Have? "))
mass=float(carridges*100000)
print("Train Weight =",mass, "kg", "Or", mass/1000, "tons")

#Calculations

#speed in m/s
linespeed=linespeedmph*0.44704

#Mass Sloping
gravity=float(9.81)
massslope=float(gravity*(math.sin(gradrad)))
print("Mass Slope",massslope, "m/s^-2")

#Net Decelleration
decel=float(((brakechar/100)*gravity)+massslope)
print(decel, "decel")
print((brakechar/100)*gravity, "brakechar")

#now have v=0, u=start, a so find t, then use that to find s(distance)
#Test editing line 
#os.system('cls')
