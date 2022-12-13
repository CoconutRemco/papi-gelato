from functions import stap1,stap2,stap3,error,showintro
opnieuw =True
bestelling=[]
while opnieuw == True:
    aantalbolletjes =int(input('Hoeveel bolletjes wilt u?'))
    if aantalbolletjes >3:
        bakjeofhoorntje='bakje'
        print(stap1(aantalbolletjes))
    elif aantalbolletjes <4 and aantalbolletjes <9:
        bakjeofhoorntje= str(input("Wilt u deze "+str(aantalbolletjes)+" bolletje(s) in een hoorntje of een bakje?")).lower()
    else:
        error()
    if stap2(bakjeofhoorntje) == 'stap3':
        print("Hier is uw ",bakjeofhoorntje," met ",aantalbolletjes," bolletje(s).")
        meerbestellen= str(input("Wilt u nog meer bestellen?")).lower()
        
        if stap3(meerbestellen,aantalbolletjes,bakjeofhoorntje) == 'stap1':
            opnieuw=True
            bestelling.append("Hier is uw "+str(bakjeofhoorntje)+" met "+str(aantalbolletjes)+" bolletje(s).")

        else:
            opnieuw=False
            print(stap3(meerbestellen,aantalbolletjes,bakjeofhoorntje))
            bestelling.append("Hier is uw "+str(bakjeofhoorntje)+" met "+str(aantalbolletjes)+" bolletje(s).")
            print(bestelling)

