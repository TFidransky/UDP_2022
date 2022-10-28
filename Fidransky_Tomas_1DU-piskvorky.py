from math import sqrt
from turtle import forward, right, left, exitonclick, setpos, speed, penup, pendown, circle

speed(10)

#Poznámka shrnující - hra funguje při správném zadání hodnot (float dojde k zaokrouhlení na int případně), ale spadne při zadání str místo int

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

while True: #samotna hra, stridani mezi hracem 1 (zde) a 2 (nekonecny cyklus while, nevim jak omezit, kdyz nemam fixni pocet kol - výhra v ruznem poctu kol nebo kvuli upravitelne velikosti hraciho pole) 
    hraX = int(float(input("Hráč 1, zadejte x-ovou souřadnici: ")))   
    hraY = int(float(input("Hráč 1, nyní zadejte y-ovou souřadnici: ")))
    #while hraX != int or hraY != int: #neúspěšná snaha zajistit, aby program nespadl při zadání jiného znaku než čísla a vyzval hráče zadat celé číslo; došlo k zacyklení programu, neprošlo to k další podmínce
    #    hraX = int(input("Hráč 1, zadejte x-ovou souřadnici ve formátu celých čísel: "))
    #    hraY = int(input("Hráč 1, zadejte y-ovou souřadnici ve formátu celých čísel: "))   
    while hraX > stranaX or hraY > stranaY: 
        print("Zadejte prosím hodnoty souřadnic X a Y, které jsou maximálně tak velké, jako jste zvolil pro šířku či výšku hracího pole")
        hraX = int(float(input("Hráč 1, zadejte x-ovou souřadnici: ")))
        hraY = int(float(input("Hráč 1, nyní zadejte y-ovou souřadnici: ")))
    penup()
    setpos(((50*hraX)-50),((50*hraY)-50))
    pendown()
    left(45)
    forward((sqrt(5000)))
    right(135)
    forward(50)
    right(135)
    forward((sqrt(5000)))

#HRAC 2 - opět zadá X a Y souřadnice, pokud jsou hodnoty OK z hlediska podmínek, tak na daném políčku vykreslí kolečko, poté opět hráč 1 a dokola
    hraX = int(float(input("Hráč 2, nyní zadejte X-ovou souřadnici: ")))
    hraY = int(float(input("Hráč 2, nyní zadejte y-ovou souřadnici: ")))
    while hraX > stranaX or hraY > stranaY:
        print("Zadejte prosím hodnoty souřadnic X a Y, které jsou maximálně tak velké, jako jste zvolil pro šířku či výšku hracího pole")
        hraX = int(float(input("Hráč 2, zadejte x-ovou souřadnici: ")))
        hraY = int(float(input("Hráč 2, nyní zadejte y-ovou souřadnici: ")))
    penup()
    setpos(((50*hraX)-50),((50*hraY)-50))
    right(135)
    forward(25)
    pendown()
    circle(25)