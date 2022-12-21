
def showintro():
    print("Welkom bij Papi Gelato")

def error():
    print("Sorry dat is geen optie die we aanbieden...")

def errorbakje():
    print("Sorry, een bakje kan maximaal 8 bolletjes bevatten.")

def totziens():
    print("Bedankt voor het bestellen bij Papi Gelato, tot ziens!")

def aantalbolletjes(zakelijkofparticulier:bool):
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
                if bolletjes >= 1 and bolletjes <= 4:
                    aantalbolletjes = bolletjes
                    herhalen = False
                    return aantalbolletjes
                elif bolletjes > 4 and bolletjes < 9:
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

def verpakking(aantalbolletjes):
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


def meerbestellen():
    try:
        meerbestellen=input("Wilt u meer bestellen?").lower()
        if meerbestellen == 'ja':
            nognkeer = True
        elif meerbestellen == 'nee':
            nognkeer = False
    except:
        error()
    return nognkeer

def bonnetje(aantalbolletjes:int,verpakkingen:str,smaken:list,toppings:list,zakelijkofparticulier:bool):
    if zakelijkofparticulier == True:
        literofbolletjes = "L"
        prijsliterofbolletjes = 9.80
    else:
        literofbolletjes = "B"
        prijsliterofbolletjes = 0.95
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
    if "Aardbei" in smaken:
        print(str(literofbolletjes)+".Aardbei: "+str(aantalsmaken['Aardbei'])+"x 1.10 = "+str(aantalsmaken['Aardbei']*float(prijsliterofbolletjes)))
    if "Chocolade" in smaken:
        print(str(literofbolletjes)+".Chocolade: "+str(aantalsmaken['Chocolade'])+"x 1.10 = "+str(aantalsmaken['Chocolade']*float(prijsliterofbolletjes)))
    if "Vanille" in smaken:
        print(str(literofbolletjes)+".Vanille: "+str(aantalsmaken['Vanille'])+"x 1.10 = "+str(aantalsmaken['Vanille']*float(prijsliterofbolletjes)))
    if "Munt" in smaken:
        print(str(literofbolletjes)+".Munt: "+str(aantalsmaken['Munt'])+"x 1.10 = "+str(aantalsmaken['Munt']*float(prijsliterofbolletjes)))
    if totaalhoorntjes >0:
        print("hoorntjes: "+str(totaalhoorntjes)+"x 1.25 = "+str(totaalhoorntjes*1.25))
    if totalbakjes >0:
        print("bakjes: "+str(totalbakjes)+"x 0.75 = "+str(totalbakjes*0.75))
    if toppings > 0:
        print("toppings            "                              " ="    +str(toppings))
    totaal=totaalbolletjes*float(prijsliterofbolletjes)+totaalhoorntjes*1.25+totalbakjes*0.75+toppings
    btw=totaal/100*9
    print("totaal: "+str(round(totaal,2)))
    if zakelijkofparticulier == True:
        print("Btw (9%)         "" ="+str((btw)))
    print("-=-=-=-=-=-=-=-=-=-Papi Gelato-=-=-=-=-=-=-=-=-=-=-=-=-")

def smaken(aantalbolletjes:int,zakelijkofparticulier:bool):
    repeat = True
    smaakdict={"a":"Aardbei","c":"Chocolade","m":"Munt","v":"Vanille",}
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
            

def toppingkiezen(bakjeofhoorntje:str):
    toppingsprijzen = {"a":0.0,"b":0.50,"c":0.30,"dh":0.60,"db":0.90}
    toppingsdict = {"a":"Geen","b":"Slagroom","c":"Sprinkels","d":"Caramelsaus"}
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

def zakelijkeklant():
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





