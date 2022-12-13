def showintro():
    print('Welkom bij Papi Gelato je mag alle smaken kiezen zolang het maar vanile ijs is.')

def error():
    print("Sorry, dat snap ik niet.")
def stap1(aantalbolletjes:int):
    if aantalbolletjes >3:
        return("Dan krijgt u van mij een bakje met ",aantalbolletjes,' bolletjes.')
    elif aantalbolletjes >0 and aantalbolletjes <4:
        pass
    elif aantalbolletjes >8:
        return('Sorry, zulke grote bakken hebben we niet.')
    else:
        return error()

        
def stap2(bakjeofhoorntje:str):
    if bakjeofhoorntje == 'bakje':
        return 'stap3'

    elif bakjeofhoorntje == 'hoorntje':
        return 'stap3'
    else:
        return error()
        


def stap3(meerbestellen:str,aantalbolletjes:int,bakjeofhoorntje:str):
    if meerbestellen == 'ja':
        return 'stap1'
    elif meerbestellen == 'nee':
        return print("Bedankt en tot ziens!")
    else:
        return error()













