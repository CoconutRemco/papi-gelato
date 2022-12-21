from papigelatofunctions import *
## Variabelen
herhalen =  True
totaalbolletjes = 0
smakenbolletjestotaal = []
verpakkingen = []
toppings = 0
nognkeer = True
## Begin van het programma
showintro()
## Loop voor het bestellen
while herhalen == True:
    if nognkeer ==True:
## Kiezen van zakelijk of particulier
        zakelijkofparticulier=zakelijkeklant()
## Zakelijk programma
    if zakelijkofparticulier == True:
        liters=aantalbolletjes(zakelijkofparticulier)
        for i in range(liters):
            smakenbolletjes=smaken(i,zakelijkofparticulier)
            smakenbolletjestotaal.append(smakenbolletjes)
        herhalen = False
        totaalbolletjes+=liters
## Particulier programma
    else:
        bolletjes=aantalbolletjes(zakelijkofparticulier)
        for i in range(bolletjes):
            smakenbolletjes=smaken(i,zakelijkofparticulier)
            smakenbolletjestotaal.append(smakenbolletjes)
        verpakkingbolletjes = verpakking(bolletjes)
        topping=toppingkiezen(verpakkingbolletjes)
        toppings+=topping
        print("Hier is uw "+str(verpakkingbolletjes)+" met "+str(bolletjes)+" bolletje(s).")
## Vragen of je nog meer wilt bestellen
        nognkeer=meerbestellen()
        if nognkeer == True:
            herhalen = True
        else:
            herhalen = False
        totaalbolletjes+=bolletjes
        verpakkingen.append(verpakkingbolletjes)
        nognkeer=False
## Printen van bonnetje
bonnetje(totaalbolletjes,verpakkingen,smakenbolletjestotaal,toppings,zakelijkofparticulier)
## Printen van tot ziens
totziens()




    