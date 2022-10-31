from math import sqrt
from tkinter import HORIZONTAL
from turtle import exitonclick, forward, right, left, setpos, speed, penup, pendown, circle
from unicodedata import digit
from random import randint

def input_pole_x(): # velikost hraciho pole - volitelna velikost
    stranaX = input("Zadejte sirku hraciho pole (=mnozstvi sloupcu): ")
    if not stranaX.isdigit():
        print ("Nespravny input, sirka hraciho pole musi byt ve formatu celych cisel")
    stranaX = int(stranaX)
    return(stranaX)
    
def input_pole_y():
    stranaY = input("Zadejte sirku hraciho pole (=mnozstvi sloupcu): ")
    if not stranaY.isdigit():
        print ("Nespravny input, sirka hraciho pole musi byt ve formatu celych cisel")
    stranaY = int(stranaY)
    return(stranaY)
          
def vykresli_pole(stranaX, stranaY): #vykresleni hraciho pole - ctverec, funkce
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

def souradnice_hrac_x():
    while True: #hráč 1, zadá souřadnici "x", ověří se, že je OK, poté "y" a stejné ověření, pokud OK, nakreslí na vybraném místě křížek
        hraX = input("Hraci, zadejte x-ovou souradnici: ")        
        if not hraX.isdigit() or int(hraX) > stranaX: 
            hraX = print("Nespravny input, x-ova souradnice by mela byt ve formatu celeho cisla a melo by byt v intervalu od 1 do",stranaX,".")
        else:
            break
    hraX = int(hraX) #převod na integer, aby fungovalo vykreslování správně
    return(hraX)

def souradnice_hrac_y():
    while True:
        hraY = input("Hraci, zadejte y-ovou souradnici: ")
        if not hraY.isdigit() or int(hraY) > stranaY:
            hraY = print("Nespravny input, y-ova souradnice by mela byt ve formatu celeho cisla a melo by byt v intervalu od 1 do",stranaY,".")
        else:
            break
    hraY = int(hraY)
    return(hraY)
    
def namaluj_krizek(hraX, hraY):
    penup()
    setpos(((50*hraX)-50),((50*hraY)-50))
    pendown()
    left(45)
    forward((sqrt(5000)))
    right(135)
    forward(50)
    right(135)
    forward((sqrt(5000)))

def bot_souradnice_x(stranaX):
    return (randint(1, stranaX))
    
def bot_souradnice_y(stranaY):        
    return (randint(1, stranaY))
    
def vykresli_kolecko(hraX, hraY):
    penup()
    setpos(((50*hraX)-50),((50*hraY)-50))
    right(135)
    forward(25)
    pendown()
    circle(25)
    print("Bot si vybral souradnice x =",hraX,"a y =",hraY)
    
speed(0)

stranaX = input_pole_x()
stranaY = input_pole_y()

vykresli_pole(stranaX, stranaY)

hraX = 0
hraY = 0

tahy = stranaX * stranaY #pocet tahu v dane hre
aktualni = 0 #zjistuje jaky tah byl zahran

while True: #samotna hra, stridani mezi hracem 1 (zde) a 2; na tomto řádku omezení počtu kol, závisí na velikosti hracího pole - jedná se o maximální možný počet tahů
    sour_x = souradnice_hrac_x()
    sour_y = souradnice_hrac_y()
    namaluj_krizek(sour_x, sour_y)
    aktualni = aktualni + 1
    if aktualni >= tahy: #zjistuje, jestli aktualni tah uz neni tolikaty, kolik tahu ma dana hra mit; v pripade, ze uz je cil naplnen, tak se cyklus prerusi a hra ukonci (respektive nedovoli dalsi vstup)
        break

    #bot nahodna funkce, pro x a y priradi pro cislo 1 az stranaX (resp. stranaY), poté vykreslí na daném místě kolečko
    bot_x = bot_souradnice_x(stranaX)
    bot_y = bot_souradnice_y(stranaY)
    vykresli_kolecko(bot_x, bot_y)
    aktualni = aktualni + 1
    if aktualni >= tahy: #zjistuje, jestli aktualni tah uz neni tolikaty, kolik tahu ma dana hra mit; v pripade, ze uz je cil naplnen, tak se cyklus prerusi a hra ukonci (respektive nedovoli dalsi vstup)
        break

print("Konec hry! Program ukoncite kliknutim.")
exitonclick()