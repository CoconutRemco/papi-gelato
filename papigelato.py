from papigelatofunctions import *
herhalen =  True
totaalbolletjes = 0
smakenbolletjestotaal = []
verpakkingen = []
toppings = 0
showintro()
while herhalen == True:
    zakelijkofparticulier=zakelijkeklant()
    if zakelijkofparticulier == True:
        liters=aantalbolletjes(zakelijkofparticulier)
        for i in range(liters):
            smakenbolletjes=smaken(i,zakelijkofparticulier)
            smakenbolletjestotaal.append(smakenbolletjes)
        herhalen = False
        totaalbolletjes+=liters
    else:
        bolletjes=aantalbolletjes(zakelijkofparticulier)
        for i in range(bolletjes):
            smakenbolletjes=smaken(i,zakelijkofparticulier)
            smakenbolletjestotaal.append(smakenbolletjes)
        verpakkingbolletjes = verpakking(bolletjes)
        topping=toppingkiezen(verpakkingbolletjes)
        toppings+=topping
        print("Hier is uw "+str(verpakkingbolletjes)+" met "+str(bolletjes)+" bolletje(s).")
        nognkeer=meerbestellen()
        if nognkeer == True:
            herhalen = True
        else:
            herhalen = False
        totaalbolletjes+=bolletjes
        verpakkingen.append(verpakkingbolletjes)
bonnetje(totaalbolletjes,verpakkingen,smakenbolletjestotaal,toppings,zakelijkofparticulier)
totziens()




    