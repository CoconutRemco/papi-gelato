from papigelatofunctions import *
herhalen =  True
showintro()
bestellingtotaal = []
while herhalen == True:
    bolletjes=aantalbolletjes()
    if bolletjes >4:
        print("Dan krijgt u van mij een bakje met "+str(bolletjes)+" bolletjes.")
        verpakkingbolletjes = 'bakje'
        nognkeer=meerbestellen()
        if nognkeer == True:
            herhalen = True
        else:
            herhalen = False
    else:
        verpakkingbolletjes = verpakking(bolletjes)
        print("Hier is uw "+str(verpakkingbolletjes)+" met "+str(bolletjes)+" bolletje(s).")
        nognkeer=meerbestellen()
        if nognkeer == True:
            herhalen = True
        else:
            herhalen = False
    bestellingtotaal.append(bestelling(bolletjes,verpakkingbolletjes))
print(bestellingtotaal)

    