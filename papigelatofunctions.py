def showintro():
    print('Welkom bij Papi Gelato je mag alle smaken kiezen zolang het maar vanile ijs is.')

def error():
    print("Sorry, dat snap ik niet.")

def errorbakje():
    print("Sorry, een bakje kan maximaal 8 bolletjes bevatten.")

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
            elif bolletjes == 0 or bolletjes <0:
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

def bestelling(aantalbolletjes:int,verpakking:str):
    bestelling = {}
    bestelling[verpakking]=aantalbolletjes
    return bestelling




