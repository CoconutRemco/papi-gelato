from papigelatofunctions import *
herhalen =  True
totaalbolletjes = 0
smakenbolletjestotaal = []
verpakkingen = []
showintro()
while herhalen == True:
    bolletjes=aantalbolletjes()
    for i in range(bolletjes):
        smakenbolletjes=smaken(i)
        for smaak in smakenbolletjes:
            smakenbolletjestotaal.append(smaak)
    verpakkingbolletjes = verpakking(bolletjes)
    print("Hier is uw "+str(verpakkingbolletjes)+" met "+str(bolletjes)+" bolletje(s).")
    nognkeer=meerbestellen()
    if nognkeer == True:
        herhalen = True
    else:
        herhalen = False
    totaalbolletjes+=bolletjes
    verpakkingen.append(verpakkingbolletjes)
bonnetje(totaalbolletjes,verpakkingen,smakenbolletjestotaal)
totziens()




    