
def showintro():
    print("Welkom bij Papi Gelato")

def error():
    print("Sorry, dat snap ik niet.")

def errorbakje():
    print("Sorry, een bakje kan maximaal 8 bolletjes bevatten.")

def totziens():
    print("Bedankt voor het bestellen bij Papi Gelato, tot ziens!")

def aantalbolletjes():
    herhalen =  True
    while herhalen == True:
        try:
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

def bonnetje(aantalbolletjes:int,verpakkingen:str,smaken:list,toppings:list):
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
    print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
    aantalsmaken={}
    for smaak in smaken:
        if smaak in aantalsmaken:
            aantalsmaken[smaak]+=1
        else:
            aantalsmaken[smaak]=1
    if "Aardbei" in smaken:
        print("B.Aardbei: "+str(aantalsmaken['Aardbei'])+"x 1.10 = "+str(aantalsmaken['Aardbei']*1.10))
    if "Chocolade" in smaken:
        print("B.Chocolade: "+str(aantalsmaken['Chocolade'])+"x 1.10 = "+str(aantalsmaken['Chocolade']*1.10))
    if "Vanille" in smaken:
        print("B.Vanille: "+str(aantalsmaken['Vanille'])+"x 1.10 = "+str(aantalsmaken['Vanille']*1.10))
    if "Munt" in smaken:
        print("B.Munt: "+str(aantalsmaken['Munt'])+"x 1.10 = "+str(aantalsmaken['Munt']*1.10))
    print("hoorntjes: "+str(totaalhoorntjes)+"x 1.25 = "+str(totaalhoorntjes*1.25))
    print("bakjes: "+str(totalbakjes)+"x 0.75 = "+str(totalbakjes*0.75))
    if toppings > 0:
        print("toppings "                              " ="    +str(toppings))
    print(("totaal: "+str(totaalbolletjes*1.10+totaalhoorntjes*1.25+totalbakjes*0.75+toppings)))
    print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
def smaken(aantalbolletjes:int):
    smakenlist=[]
    repeat = True
    while repeat == True:
        try:
            smaak = input("Welke smaak wilt u voor bolletje "+str(aantalbolletjes+1)+" A) Aardbei, C) Chocolade, M) Munt of V) Vanille?”").lower()
            if smaak == "a":
                smaak = "Aardbei"
                smakenlist.append(smaak)
                repeat = False
            elif smaak == "c":
                smaak = "Chocolade"
                smakenlist.append(smaak)
                repeat = False
            elif smaak == "m":
                smaak = "Munt"
                smakenlist.append(smaak)
                repeat = False
            elif smaak == "v":
                smaak = "Vanille"
                smakenlist.append(smaak)
                repeat = False
            else:
                error()
        except:
            error()
    return smakenlist

def toppingkiezen(bakjeofhoorntje:str):
    slagroom  = 0.50
    sprinkels = 0.30
    caramelsaushoorntje = 0.60
    caramelsausbakje = 0.90
    repeat = True
    while repeat == True:
        try:
            topping = input("Wilt u een topping op uw ijs A) Geen, B) Slagroom, C) Sprinkels of D) Caramel Saus?").lower()
            if topping == "a":
                repeat = False
            elif topping == "b":
                repeat = False
                return slagroom
            elif topping == "c":
                repeat = False
                return  sprinkels
            elif topping == "d":
                repeat = False
                if bakjeofhoorntje == "hoorntje":
                    return caramelsaushoorntje
                elif bakjeofhoorntje == "bakje":
                    return caramelsausbakje
            else:
                error()
        except:
            error()
            repeat=True







