#File orgininally created by J Craigmile, Please use this only for reference purposes as it is imperfect and incomplete
#Currently this uses many assumptions that are completely inaccurate for use in the real world.

# -*- coding: utf-8 -*-
"""
Created on Wed Oct 17 07:43:31 2018

@author: UKJXC014
"""

#Headways calculator


#import numpy as np
#import openpyxl as xl
import time

print("headways calculator")

fouraspect=input("do you require 4 aspect signalling? (Y/N) ... ")
   
#def tableDisplay():
#    print("Signal" + "|" + "Headway")
#    t=np.matrix([(siglist),(headwayslist)])
#    p=np.matrix.transpose(t)
#    print(p)

#def fin():   
#    export=input("review data before export to xl? (Y/N)")
#    if export.upper=="Y":
#        tableDisplay()
#    else:
#        printToXL()
#        return("file created")

#def printToXL():
#    sheettitle=input("what would you like to name your data?")
#    wb=xl.Workbook()
#    wb.sheetnames()
#    sheet=wb.active
#    sheet.title=str(sheettitle)
#    sheet['A1']="Signal"
#    sheet['B1']="Distance"
#    sheet['C1']="OL"


    
signum=float(input("how many signals are in the route ... "))  

siglist=[]
aspectlist=[]
signumend=0
while float(signumend) < float(signum):
#    time.sleep(0.5)
    if fouraspect.upper()=="N":
        signumend=signumend+1
        sig=input("enter signal number "+str(signumend)+" ... ")
        siglist=siglist+[str(sig)]
    elif fouraspect.upper()=="Y":
            signumend=signumend+1
            sig=input("enter signal number "+str(signumend)+" ... ")
            siglist=siglist+[str(sig)]
            aspect=input("enter aspect number for signal "+str(sig)+" ... ")
            aspectlist=aspectlist+[aspect]

distlist=[]
distnumend=0
while float(distnumend+1) < float(signum):
#    time.sleep(0.5)
    distnumend=distnumend+1
    dist=input("enter distance between signal "+str(siglist[distnumend-1])+" and "+str(siglist[distnumend])+" ... ")
    distlist=distlist+[float(dist)]
#distlist=distlist+[" - "]

OLlist=[]
OLnumend=0
while float(OLnumend) < float(signum):
#    time.sleep(0.5)
    OLnumend=OLnumend+1
    oLap=input("enter the overlap for signal "+str(siglist[OLnumend-1]+" ... "))
    OLlist=OLlist+[float(oLap)]

datumlist=[]
datumend=0
datum=0
while float(datumend)<float(signum):
    if datumend==0:
        datumlist=datumlist+[float(0)]
        datumend=datumend+1
    elif float(datumend) >0:
        datum=float(datum)+float(distlist[datumend-1])
        datumlist=datumlist+[float(datum)]
        datumend=datumend+1
    else:
        break
    
int1=0
OLdatumlist=[]
while int1<len(datumlist):
    datum=datumlist[int1]+OLlist[int1]
    OLdatumlist=OLdatumlist+[datum]
    int1=int1+1

speedlist=[float(0)]
loclist=[]
psr=""
print("\n your first PSR needs to be at a distance of 0m from the first signal or the code will not work \n")
time.sleep(2)
while True:
    psr=input("would you like to add a PSR (Y/N) ... ").upper()
    if psr =="N":
        break
    elif psr=="Y":
        speed=input("input a PSR speed (mph) ... ")
        loc=input("input the distance (m) from signal "+str(siglist[0])+" ... ")
        speedlist=speedlist+[float(speed)*(4/9)]
        loclist=loclist+[float(loc)]
    elif psr != "Y" or "N":
        print("only Y or N please")
loclist.append((datumlist[len(datumlist)-1])+OLlist[len(OLlist)-1]) 

psrint=0
psrtimelist=[]
while psrint<(len(loclist)-1):
    if psrint==0:
        psrtimelist=psrtimelist+[float(0)]
        psrint=psrint+1
    elif psrint>0:
        psrtime=psrtimelist[psrint-1]+((loclist[psrint]-loclist[psrint-1])/speedlist[psrint])
        psrtimelist=psrtimelist+[psrtime]
        psrint=psrint+1
        
int1,int2=1,0
acceltimelist=[]
while int1<(len(speedlist)-1):
    if float(speedlist[int1+1])-float(speedlist[int1])>0:
        acceltime=(float(speedlist[int1+1])-float(speedlist[int1]))/float(0.5883) #6%g
        acceltimelist=acceltimelist+[float(acceltime)]
        int1=int1+1
    elif float(speedlist[int1+1])-float(speedlist[int1])<0:
        acceltime=(float(speedlist[int1+1])-float(speedlist[int1]))/float(-0.5883) #6%g
        acceltimelist=acceltimelist+[float(acceltime)]
        int1=int1+1
        
int1,int2=1,0
acceldistlist=[]
while int1<(len(speedlist)-1):
    if float(speedlist[int1+1])-float(speedlist[int1])>0:
        acceldist=(float(speedlist[int1+1])**2-float(speedlist[int1])**2)/(float(0.5883)*2) #6%g
        acceldistlist=acceldistlist+[float(acceldist)]
        int1=int1+1
    elif float(speedlist[int1+1])-float(speedlist[int1])<0:
        acceldist=(float(speedlist[int1+1])**2-float(speedlist[int1])**2)/(float(-0.5883)*2) #6%g
        acceldistlist=acceldistlist+[float(acceldist)]
        int1=int1+1

int1,int2=0,0
timelist=[]
while int1<(len(datumlist)) and int2<len(loclist):
    if datumlist[int1]==0:
        timelist=timelist+[float(0)]
       # print("int1 "+str(int1))
       # print("int2 "+str(int2))
       # print("initial")
        int1=int1+1
    elif loclist[int2]<=datumlist[int1]<=loclist[int2+1]:
        time=psrtimelist[int2]+(datumlist[int1]-loclist[int2])/speedlist[int2+1]
        timelist=timelist+[time]
       # print("int1 "+str(int1))
       # print("int2 "+str(int2))
      #  print("loop1")
        int1=int1+1
    elif datumlist[int1]==loclist[int2]:
        time=psrtimelist[int2]+(datumlist[int1]-loclist[int2])/speedlist[int2]
        timelist=timelist+[time]
        #print("int1 "+str(int1))
       # print("int2 "+str(int2))
        int1=int1+1
        #print("loop2")
    else:
        #print("int1 "+str(int1))
        #print("int2 "+str(int2))
        int2=int2+1
        #print("else")

int1,int2=0,0
OLtimelist=[]
while int1<(len(OLdatumlist)) and int2<len(loclist):
    if OLdatumlist[int1]==0:
        OLtimelist=OLtimelist+[float(0)]
        #print("int1 "+str(int1))
        #print("int2 "+str(int2))
        #print("initial")
        int1=int1+1
    elif loclist[int2]<=OLdatumlist[int1]<=loclist[int2+1]:
        time=psrtimelist[int2]+(OLdatumlist[int1]-loclist[int2])/speedlist[int2+1]
        OLtimelist=OLtimelist+[time]
        #print("int1 "+str(int1))
        #print("int2 "+str(int2))
        #print("loop1")
        int1=int1+1
    elif OLdatumlist[int1]==loclist[int2]:
        time=psrtimelist[int2]+(OLdatumlist[int1]-loclist[int2])/speedlist[int2]
        OLtimelist=OLtimelist+[time]
        #print("int1 "+str(int1))
        #print("int2 "+str(int2))
        int1=int1+1
        #print("loop2")
    else:
        #print("int1 "+str(int1))
        #print("int2 "+str(int2))
        int2=int2+1
        #print("else")


int1=0
headwayslist=[]
if fouraspect.upper()=="Y":
    deadsigs=3
elif fouraspect.upper()=="N":
    deadsigs=2
while int1<(len(datumlist)-deadsigs):
    if fouraspect.upper()=="N":
        headway=OLtimelist[int1+2]-timelist[int1]
        headwayslist=headwayslist+[round(headway,1)]
        int1=int1+1
    elif fouraspect.upper()=="Y":
        if aspectlist[int1]==int(4):
            headway=OLtimelist[int1+3]-timelist[int1]
            headwayslist=headwayslist+[round(headway,1)]
            int1=int1+1
        elif aspectlist[int1]!=int(4):
            headway=OLtimelist[int1+2]-timelist[int1]
            headwayslist=headwayslist+[round(headway,1)]
            int1=int1+1
            
spaces=len(siglist)-len(headwayslist)
if spaces==int(2):
    headwayslist.append("NA")
elif spaces == int(3):
    headwayslist.append("NA")
    headwayslist.append("NA")

siglist.insert(0,"Sig")
headwayslist.insert(0,"Hwys")
res = "\n".join("{} {}".format(x, y) for x, y in zip(siglist, headwayslist))
print(res)
