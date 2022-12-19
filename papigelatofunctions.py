def showintro():
    print('Welkom bij Papi Gelato je mag alle smaken kiezen zolang het maar vanile ijs is.')

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
            bakje = input('Wilt u deze '+ str(aantalbolletjes) +' bolletje(s) in een hoorntje of een bakje? ').lower()
            if bakje == 'bakje':
                verpakking = 'bakje'
                herhalen = False
                return verpakking
            elif bakje == 'hoorntje':
                verpakking = 'hoorntje'
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

def bonnetje(aantalbolletjes:int,verpakking:str):
    totaalbolletjes=0
    totaalhoorntjes=0
    totalbakjes=0
    totaalbolletjes+=aantalbolletjes
    if verpakking == 'hoorntje':
        totaalhoorntjes+=1
    elif verpakking == 'bakje':
        totalbakjes+=1
    else:
        error()
    print("Hier is uw bonnetje!")
    print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
    print("bolletjes: "+str(totaalbolletjes)+"x 1.10 : "+str(totaalbolletjes*1.10))
    print("hoorntjes: "+str(totaalhoorntjes)+"x 1.25 : "+str(totaalhoorntjes*1.25))
    print("bakjes: "+str(totalbakjes)+"x 0.75 : "+str(totalbakjes*0.75))
    print("totaal: "+str(totaalbolletjes*1.10+totaalhoorntjes*1.25+totalbakjes*0.75))
    print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
    return bonnetje




