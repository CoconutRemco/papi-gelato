from papigelatofunctions import *
herhalen =  True
showintro()
while herhalen == True:
    bolletjes=aantalbolletjes()
    if bolletjes >4:
        print("Dan krijgt u van mij een bakje met "+str(bolletjes)+" bolletjes.")
        verpakkingbolletjes = 'bakje'
    else:
        verpakkingbolletjes = verpakking(bolletjes)
        print("Hier is uw "+str(verpakkingbolletjes)+" met "+str(bolletjes)+" bolletje(s).")
    nognkeer=meerbestellen()
    if nognkeer == True:
        herhalen = True
    else:
        herhalen = False
bonnetje(bolletjes,verpakkingbolletjes)
totziens()





    