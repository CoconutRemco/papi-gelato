from functions import error,showintro,errorbakje
nognkeer = True
showintro()
while nognkeer == True:
    try:
        bolletjes = int(input('Hoeveel bolletjes wilt u? '))
        if bolletjes >= 1 and bolletjes <= 3:
            mnognkeer = False
            aantalbolletjes = bolletjes
            bakje = input('Wilt u deze '+ str(bolletjes) +' bolletje(s) in een hoorntje of een bakje? ').lower()
            if bakje == 'bakje':
                meerbestellen = input('Hier is uw bakje met '+ str(bolletjes) +' bolletje(s). Wilt u nog meer bestellen?').lower()
                if meerbestellen == 'ja':
                    nognkeer = True
                elif meerbestellen  == 'nee':
                    print('Bedankt en tot ziens!')
                    nognkeer = False
                else:
                    error()
            elif bakje == 'hoorntje':
                meerbestellen = input('Hier is uw hoorntje met '+ str(bolletjes) +' bolletje(s). Wilt u nog meer bestellen?').lower()
                if meerbestellen == 'ja':
                    nognkeer = True
                elif meerbestellen == 'nee':
                    nognkeer = False
                    print('Bedankt en tot ziens!')
                else:
                    error()
            else:
                error()

        elif bolletjes >= 4 and bolletjes <= 8:
            aantalbolletjes = bolletjes
            print('Dan krijgt u van mij een bakje met '+ str(bolletjes) +' bolletjes.')
            nognkeer = False
            meerbestellen = input('Wilt u nog meer bestellen?').lower()
            if meerbestellen == 'ja':
                nognkeer = True
            elif meerbestellen == 'nee':
                nognkeer = False
                print('Bedankt en tot ziens!')
            else:
                error()

        elif bolletjes > 8:
            errorbakje()
            nognkeer= True
        elif bolletjes == 0 or bolletjes <0:
            error()
            nognkeer = True
    except:
        error()