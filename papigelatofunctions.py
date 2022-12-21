## Variabelen voor prijzen
prijsLiter= 9.80
prijsBolletje= 0.95
prijsHoorntje= 1.25
prijsbakje= 0.75
toppingsprijzen = {"a":0.0,"b":0.50,"c":0.30,"dh":0.60,"db":0.90}
toppingsdict = {"a":"Geen","b":"Slagroom","c":"Sprinkels","d":"Caramelsaus"}
smaakdict={"a":"Aardbei","c":"Chocolade","v":"Vanille"}
## Functies
## Welkomstscherm
def showintro():
    print("Welkom bij Papi Gelato")
## Error messages
def error():
    print("Sorry dat is geen optie die we aanbieden...")

def errorbakje():
    print("Sorry, een bakje kan maximaal 8 bolletjes bevatten.")
## Afscheidsboodschap
def totziens():
    print("Bedankt voor het bestellen bij Papi Gelato, tot ziens!")
## Bestellen van aantal bolletjes minimaal 1 maximaal 8
def aantalbolletjes(zakelijkofparticulier:bool) -> int:
    herhalen =  True
    while herhalen == True:
        try:
            if zakelijkofparticulier == True:
                liters = int(input('Hoeveel liter ijs wilt u?'))
                if liters >=1:
                    herhalen = False
                    return liters
                else:
                    error()
                    herhalen = True
            else:
                bolletjes = int(input('Hoeveel bolletjes wilt u? '))
                if bolletjes >= 1 and bolletjes < 4:
                    aantalbolletjes = bolletjes
                    herhalen = False
                    return aantalbolletjes
                elif bolletjes >= 4 and bolletjes < 9:
                    aantalbolletjes = bolletjes
                    herhalen = False 
                    return aantalbolletjes
                elif bolletjes > 8:
                    errorbakje()
                    herhalen = True
                elif bolletjes <=0:
                    error()
                    herhalen = True
        except:
            error()
            herhalen = True
## Kiezen van verpakking bakje of hoorntje
def verpakking(aantalbolletjes) -> str:
    herhalen = True
    while herhalen == True:
        try:
            if aantalbolletjes <=4:
                bakje = input('Wilt u deze '+ str(aantalbolletjes) +' bolletje(s) in een hoorntje of een bakje? ').lower()
                if bakje == 'bakje':
                    verpakking = 'bakje'
                    herhalen = False
                    return verpakking
                elif bakje == 'hoorntje':
                    verpakking = 'hoorntje'
                    herhalen = False
                    return verpakking
            else:
                print("U krijgt een bakje met "+str(aantalbolletjes)+" bolletje(s).")
                verpakking = 'bakje'
                herhalen = False
                return verpakking
        except:
            error()
            herhalen = True

## Keuze van meerbestellen ja of nee
def meerbestellen() -> bool:
    try:
        meerbestellen=input("Wilt u meer bestellen?").lower()
        if meerbestellen == 'ja':
            nognkeer = True
        elif meerbestellen == 'nee':
            nognkeer = False
    except:
        error()
    return nognkeer
## Printen van bonnetje met prijzen en totaalprijs
## Bonnetje kijkt zelf of het zakelijk of particulier is en past zich hier naar aan
## Bonnetje kijkt ook naar de verpakkingen en past zich hier naar aan
def bonnetje(aantalbolletjes:int,verpakkingen:str,smaken:list,toppings:list,zakelijkofparticulier:bool):
    if zakelijkofparticulier == True:
        literofbolletjes = "L"
        prijsliterofbolletjes = prijsLiter
    else:
        literofbolletjes = "B"
        prijsliterofbolletjes = prijsBolletje
    totaalbolletjes=0
    totaalhoorntjes=0
    totalbakjes=0
    totaalbolletjes+=aantalbolletjes
    for verpakking in verpakkingen:
        if verpakking == 'hoorntje':
            totaalhoorntjes+=1
        elif verpakking == 'bakje':
            totalbakjes+=1
        else:
            error()
    print("Hier is uw bonnetje!")
    print("-=-=-=-=-=-=-=-=-=-=-Papi Gelato-=-=-=-=-=-=-=-=-=-=-=-")
    aantalsmaken={}
    for smaak in smaken:
        if smaak in aantalsmaken:
            aantalsmaken[smaak]+=1
        else:
            aantalsmaken[smaak]=1
    for smaak in aantalsmaken:
        prijs = format(aantalsmaken[smaak]*prijsliterofbolletjes)
        print(str(literofbolletjes)+"."+str(smaak)+" "+str(aantalsmaken[smaak])+"x "+str(prijsliterofbolletjes)+" = "+str(prijs))
    if totaalhoorntjes >0:
        prijs = format(totaalhoorntjes*1.25)
        print("hoorntjes: "+str(totaalhoorntjes)+"x "+str(prijsHoorntje)+" = "+str(prijs))
    if totalbakjes >0:
        prijs = format(totalbakjes*0.75)
        print("bakjes: "+str(totalbakjes)+"x "+str(prijsbakje)+" = "+str(prijs))
    if toppings > 0:
        prijs = format(toppings)
        print("toppings            "                              " ="    +str(prijs))
    totaal=totaalbolletjes*float(prijsliterofbolletjes)+totaalhoorntjes*1.25+totalbakjes*0.75+toppings
    btw=totaal/100*6
    print("totaal: "+str(round(totaal,2)))
    if zakelijkofparticulier == True:
        btw = format(btw)
        print("Btw (6%)         "" ="+str((btw)))
    print("-=-=-=-=-=-=-=-=-=-=-Papi Gelato-=-=-=-=-=-=-=-=-=-=-=-")
## Kiezen van smaken
def smaken(aantalbolletjes:int,zakelijkofparticulier:bool)  -> str:
    repeat = True
    smakentext = ''
    if zakelijkofparticulier == True:
        literofbolletje = "liter "
    else:
        literofbolletje = 'bolletje '
    for keys , value in smaakdict.items():
        smakentext += keys +") " + value + " "
    try:
        while repeat == True:
                smaak = input("Welke smaak wilt u voor "+str(literofbolletje)+str(aantalbolletjes+1)+" "+str(smakentext)).lower()
                if smaak in smaakdict.keys():
                    return smaakdict[smaak]
    except:
        error()
            
## Kiezen van toppings
def toppingkiezen(bakjeofhoorntje:str) -> float:
    repeat = True
    toppingtext = ''
    for keys , value in toppingsdict.items():
        toppingtext += keys +") " + value + " "
    while repeat == True:
        try:
            topping = input("Wilt u een topping op uw ijs? "+toppingtext).lower()
            if topping in toppingsdict.keys():
                if bakjeofhoorntje == 'bakje' and topping == "d":
                    return toppingsprijzen["db"]
                elif bakjeofhoorntje == 'hoorntje' and topping == "d":
                    return toppingsprijzen["dh"]
                else:
                    return toppingsprijzen[topping]
        except:
            error()
            repeat=True
## Kijken of de klant een zakelijke klant is of een particuliere klant
def zakelijkeklant() -> bool:
    repeat = True
    while repeat == True:
        try:
            zakelijk = input("Bent u 1) een particuliere klant of 2) een zakelijke klant?").lower()
            if zakelijk == '2':
                repeat=False
                return True   
            elif zakelijk == '1':
                repeat=False
                return False
            else:
                error()
        except:
            error()
            repeat = True
## Formateren van prijzenS
def format(prijs:float) -> str:
    return f'{prijs: .2f}'








