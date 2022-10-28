from math import sqrt
from turtle import forward, right, left, setpos, speed, penup, pendown, circle
from unicodedata import digit

speed(0)

#velikost hraciho pole - volitelna velikost
stranaX = int(float(input("Zadejte šířku hracího pole (=množství sloupců): ")))
stranaY = int(float(input("Zadejte výšku hracího pole (=množství řádků): ")))

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

while True: #samotna hra, stridani mezi hracem 1 (zde) a 2; nekonecny cyklus while, nevim jak omezit, kdyz nemam fixni pocet kol - výhra v ruznem poctu kol nebo kvuli upravitelne velikosti hraciho pole)
    while True: #hráč 1, zadá souřadnici x, ověří se, že je OK, poté Y a stejné ověření, pokud OK, nakreslí na vybraném místě křížek
        hraX = input("Hráč 1, zadejte x-ovou souřadnici: ")
        
        if not hraX.isdigit() or int(hraX) > stranaX: 
            hraX = print("Nesprávný input, formát by měl být v ")
        else:
            break
        
    while True:
        hraY = input("Hráč 1, zadejte y-ovou souřadnici: ")
        if not hraY.isdigit() or int(hraY) > stranaY:
            hraY = print("Nesprávný input")
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

    #HRAC 2 - opět zadá X a Y souřadnice, if zjišťuje podmínky, pokud jsou  OK, tak na vybraném políčku vykreslí kolečko, poté volí místo hráč 1 a to se opakuje do nekonečna
    while True:    
        hraX = input("Hráč 2, zadejte x-ovou souřadnici: ")
        
        if not hraX.isdigit() or int(hraX) > stranaX:
            hraX = print("Nesprávný input")
        else:
            break

    while True:
        hraY = input("Hráč 2, zadejte y-ovou souřadnici: ")
        if not hraY.isdigit() or int(hraY) > stranaY:
            hraY = print("Nesprávný input")
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