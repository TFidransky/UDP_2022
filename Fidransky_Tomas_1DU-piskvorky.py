from math import sqrt
from turtle import exitonclick, forward, right, left, setpos, speed, penup, pendown, circle
from unicodedata import digit

speed(0)

#velikost hraciho pole - volitelna velikost
stranaX = input("Zadejte šířku hracího pole (=množství sloupců): ")
if not stranaX.isdigit():
    stranaX = print ("Nesprávný input, šířka hracího pole musí být ve formátu celých čísel")

stranaY = input("Zadejte šířku hracího pole (=množství sloupců): ")
if not stranaY.isdigit():
    stranaY = print ("Nesprávný input, šířka hracího pole musí být ve formátu celých čísel")
  
stranaX = int(stranaX)
stranaY = int(stranaY)

#vykresleni hraciho pole - ctverec
for y in range(stranaY):
    for x in range (stranaX):
        for i in range (4):
            forward (50)
            left(90)
        forward(50)
    right(180)
    forward(stranaX*50)
    right(90)
    forward(50)
    right(90)
tahy = stranaX * stranaY
aktualni = 0

while True: #samotna hra, stridani mezi hracem 1 (zde) a 2; na tomto řádku omezení počtu kol, závisí na velikosti hracího pole - jedná se o maximální možný počet tahů
    while True: #hráč 1, zadá souřadnici "x", ověří se, že je OK, poté "y" a stejné ověření, pokud OK, nakreslí na vybraném místě křížek
        hraX = input("Hráč 1, zadejte x-ovou souřadnici: ")        
        if not hraX.isdigit() or int(hraX) > stranaX: 
            hraX = print("Nesprávný input, x-ová souřadnice by měla být ve formátu celého čísla a mělo by být v intervalu od 1 do",stranaX,".")
        else:
            break
        
    while True:
        hraY = input("Hráč 1, zadejte y-ovou souřadnici: ")
        if not hraY.isdigit() or int(hraY) > stranaY:
            hraY = print("Nesprávný input, y-ová souřadnice by měla být ve formátu celého čísla a mělo by být v intervalu od 1 do",stranaY,".")
        else:
            break

    hraX = int(hraX)
    hraY = int(hraY)

    #kreslení křížku
    penup()
    setpos(((50*hraX)-50),((50*hraY)-50))
    pendown()
    left(45)
    forward((sqrt(5000)))
    right(135)
    forward(50)
    right(135)
    forward((sqrt(5000)))
    aktualni = aktualni + 1
    if aktualni >= tahy:
        break

    #HRAC 2 - opět zadá "x" a "y" souřadnice, if zjišťuje podmínky, pokud jsou  OK, tak na vybraném políčku vykreslí kolečko, poté volí místo hráč 1 a to se opakuje do nekonečna
    while True:    
        hraX = input("Hráč 2, zadejte x-ovou souřadnici: ")
        
        if not hraX.isdigit() or int(hraX) > stranaX:
            hraX = print("Nesprávný input, x-ová souřadnice by měla být ve formátu celého čísla a mělo by být v intervalu od 1 do",stranaX,".")
        else:
            break

    while True:
        hraY = input("Hráč 2, zadejte y-ovou souřadnici: ")
        if not hraY.isdigit() or int(hraY) > stranaY:
            hraY = print("Nesprávný input, y-ová souřadnice by měla být ve formátu celého čísla a mělo by být v intervalu od 1 do",stranaY,".")
        else:
            break

    hraX = int(hraX)
    hraY = int(hraY)

    #kreslení kolečka
    penup()
    setpos(((50*hraX)-50),((50*hraY)-50))
    right(135)
    forward(25)
    pendown()
    circle(25)
    aktualni = aktualni + 1
    if aktualni >= tahy:
        break
exitonclick()

