from math import sqrt
from turtle import exitonclick, forward, right, left, setpos, speed, penup, pendown, circle
from unicodedata import digit
from random import randint

def input_pole():
    while True:
        stranaX = input("Zadejte sirku hraciho pole (=mnozstvi sloupcu): ")
        if not stranaX.isdigit() or int(stranaX) == 0:
            print ("Nespravny input, sirka hraciho pole musi byt ve formatu celych cisel a nemuze byt nulova.")
        stranaX = int(stranaX)

        stranaY = input("Zadejte vysku hraciho pole (=mnozstvi radku): ")
        if not stranaY.isdigit() or int(stranaY) == 0:
            print ("Nespravny input, vyska hraciho pole musi byt ve formatu celych cisel a nemuze byt nulova.")
        stranaY = int(stranaY)
        return stranaX, stranaY   
                
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
        
def souradnice_hrac(): #input od hráče, ověření podmínek, pak return do hraX, hraY
    while True:
        hraX = input("Hraci, zadejte x-ovou souradnici: ")        
        if not hraX.isdigit() or int(hraX) > stranaX or int(hraX) == 0: 
            hraX = print("Nespravny input, x-ova souradnice by mela byt ve formatu celeho cisla a melo by byt v intervalu od 1 do",stranaX,".")

        hraY = input("Hraci, zadejte y-ovou souradnici: ")
        if not hraY.isdigit() or int(hraY) > stranaY or int(hraY) == 0:
            hraY = print("Nespravny input, y-ova souradnice by mela byt ve formatu celeho cisla a melo by byt v intervalu od 1 do",stranaY,".")
        return int(hraX), int(hraY)

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

def bot_souradnice(): #náhodné souřadnice pro bota
    bot_x = randint(1, stranaX)
    bot_y = randint(1, stranaY)
    return int(bot_x), int(bot_y)

def vykresli_kolecko(bot_x, bot_y):
    penup()
    setpos(((50*bot_x)-50),((50*bot_y)-50))
    right(135)
    forward(25)
    pendown()
    circle(25)
    print("Bot si vybral souradnice x =",bot_x,"a y =",bot_y)
    
speed(0)

stranaX, stranaY = input_pole()

vykresli_pole(stranaX, stranaY) 

tahy = stranaX * stranaY #pocet tahu v dane hre
aktualni = 0 #zjistuje jaky tah byl zahran

while True: #samotna hra, stridani mezi hracem 1 (zde) a 2; na tomto radku omezeni poctu kol, zavisi na velikosti hraciho pole - jedna se o maximalni mozny pocet tahu
    hraX, hraY = souradnice_hrac()
    namaluj_krizek(hraX, hraY)
    aktualni = aktualni + 1
    if aktualni >= tahy: #zjistuje, jestli aktualni tah uz neni tolikaty, kolik tahu ma dana hra mit; v pripade, ze uz je cil naplnen, tak se cyklus prerusi a hra ukonci (respektive nedovoli dalsi vstup)
        break

    #bot nahodna funkce, pro x a y priradi pro cislo 1 az stranaX (resp. stranaY), poté vykreslí na daném místě kolečko
    bot_x, bot_y = bot_souradnice()    
    vykresli_kolecko(bot_x, bot_y)
    aktualni = aktualni + 1
    if aktualni >= tahy: #zjistuje, jestli aktualni tah uz neni tolikaty, kolik tahu ma dana hra mit; v pripade, ze uz je cil naplnen, tak se cyklus prerusi a hra ukonci (respektive nedovoli dalsi vstup)
        break

print("Konec hry! Program ukoncite kliknutim.")
exitonclick()