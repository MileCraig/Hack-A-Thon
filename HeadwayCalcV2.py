#WSP Hackathon #2
#HeadWay Calc
#Created 30/10/2018 by:
#Will Hastie, Steve Burrows, Jonathan Craigmile, Chris Gregory, Jack Atherton.
#Purpose: Calculate the Headway of trains through a defined section of track for a four aspect signalling system.
import os
import math
print("Headway Calculator\n")

#Define Variables
#linespeed
linespeedmph=float( input("What is the Line Speed? (mph) "))
linespeedms=round(linespeedmph*(1609/3600),2)
sightingpoint=linespeedms*9
print("Line Speed =",linespeedmph,"mph",linespeedms, "ms^-1","with a sighting point at", sightingpoint,"(m) before signal\n")

#trainlength
trainlength=float( input("What is the train length? (m) "))
print("Headway calculation for trains",trainlength, "(m) long\n")
print("Signal Definition: 4 Signals")
#signun=int(input("How many signals do you wish to input?"))
#SignalName=0

#Signal 1
print("\n Signal 1")
s1_name=str(input("Signal 1: Please name the signal? "))#
s1_location=int(input("Signal 1: What is Engineering Line Reference position? (m) "))
s1_overlap=int(input("Signal 1: What is the overlap length? (m) "))
s1_dist2next=int(input("Signal 1: What is the distance to the next signal? (m) "))
s1_sighting=s1_location-sightingpoint
print("\n Signal:",s1_name,"\n ELR Location:", s1_location,"(m)","\n Overlap length:",s1_overlap,"(m)","\n Distance to next signal:",s1_dist2next,"(m)", "\n Signal Sighting Point:",s1_sighting,"(m)")

#Signal 2
print("\n Signal 2")
s2_name=str(input("Signal 2: Please name the signal? "))#
s2_location=int(input("Signal 2: What is Engineering Line Reference position? (m) "))
s2_overlap=int(input("Signal 2: What is the overlap length? (m) "))
s2_dist2next=int(input("Signal 2: What is the distance to the next signal? (m) "))
s2_sighting=s2_location-sightingpoint
print("\n Signal:",s2_name,"\n ELR Location:", s2_location,"(m)","\n Overlap length:",s2_overlap,"(m)","\n Distance to next signal:",s2_dist2next,"(m)", "\n Signal Sighting Point:",s2_sighting,"(m)")

#Signal 3
print("\n Signal 3")
s3_name=str(input("Signal 3: Please name the signal? "))#
s3_location=int(input("Signal 3: What is Engineering Line Reference position? (m) "))
s3_overlap=int(input("Signal 3: What is the overlap length? (m) "))
s3_dist2next=int(input("Signal 3: What is the distance to the next signal? (m) "))
s3_sighting=s3_location-sightingpoint
print("\n Signal:",s3_name,"\n ELR Location:", s3_location,"(m)","\n Overlap length:",s3_overlap,"(m)","\n Distance to next signal:",s3_dist2next,"(m)", "\n Signal Sighting Point:",s3_sighting,"(m)")

#Signal 4
print("\n Signal 4")
s4_name=str(input("Signal 4: Please name the signal? "))#
s4_location=int(input("Signal 4: What is Engineering Line Reference position? (m) "))
s4_overlap=int(input("Signal 4: What is the overlap length? (m) "))
s4_dist2next=int(input("Signal 4: What is the distance to the next signal? (m) "))
s4_sighting=s4_location-sightingpoint
print("\n Signal:",s4_name,"\n ELR Location:", s4_location,"(m)","\n Overlap length:",s4_overlap,"(m)","\n Distance to next signal:",s4_dist2next,"(m)", "\n Signal Sighting Point:",s4_sighting,"(m)")

#Signal 1 Headway Calc
s1_brakedist=s4_location-s1_location
s1_distnext=s1_dist2next+s2_dist2next+s3_dist2next
#check
if s1_brakedist==s1_distnext:
    print("True")            # No Error in input distances
else:
    print("False")           # Some of Individuals != Total Distance
#Sigal to overlap distance
s1_sigtoover=(s1_sighting+s1_brakedist+s4_overlap+trainlength)
s1_headway=s1_sigtoover/linespeedms
print("\nSignal 1 sighting to overlap distace: ", s1_sigtoover, " (m)","\nSignal 1 Headway:",s1_headway," (s)")
