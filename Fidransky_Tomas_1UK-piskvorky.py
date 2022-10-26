from math import sqrt
from turtle import forward, right, left, exitonclick, setpos, speed, penup, pendown, circle

speed(10)

#velikost hracího pole
a = int(input("Zadejte šířku hracího pole (=množství sloupců): "))
b = int(input("Zadejte výšku hracího pole (=množství řádků): "))


#vykreslení hracího pole - čtverec
for y in range(b):
    for x in range (a):
        for i in range (4):
            forward (50)
            left(90)
        forward(50)
    right(180)
    forward(a*50)
    right(90)
    forward(50)
    right(90)
#vrácení na [0,0] pozici        
right(90)
forward(50*b)
left(90)

while True: #samotná hra, střídání mezi hráčem 1 a 2, počet kol není omezen, ani pozice, lze dát [4,4] při hraní na 3x3 poli
    c = int(input("Hráč 1, zadejte x-ovou souřadnici: "))
    d = int(input("Hráč 1, nyní zadejte y-ovou souřadnici: "))
    penup()
    setpos(((50*c)-50),((50*d)-50))
    pendown()
    left(45)
    forward((sqrt(5000)))
    right(135)
    forward(50)
    right(135)
    forward((sqrt(5000)))
    c = int(input("Hráč 2, nyní zadejte X-ovou souřadnici: "))
    d = int(input("Hráč 2, nyní zadejte y-ovou souřadnici: "))
    penup()
    setpos(((50*c)-50),((50*d)-50))
    right(135)
    forward(25)
    pendown()
    circle(25)
    

exitonclick()