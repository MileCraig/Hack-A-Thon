#Headway Calc
#test

signum=input("What is the num ber of signals required?")
siglist=[]
signumend=0
while float(signumend) < float(signum):
      signumend=signumend+1
      sig=input("enter signal number "+str(signumend)+" ... ")
      siglist=siglist+[str(sig)]
print(siglist)
