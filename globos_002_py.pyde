# Luis Molina-Tanco - 2021. 
# 
# Ejemplo uso puerto serie. 
#
# Este programa está pensado para funcionar con un arduino
# que esté ejecutando el ejemplo InputPullupSerial, que se puede
# ver aquí:
#
# https:#www.arduino.cc/en/Tutorial/BuiltInExamples/InputPullupSerial  
    
add_library('serial')    
from globo import Globo
globos = []

dato = "1"
datoAnt = "1"

def setup():
    size(1000,800)
    printArray(Serial.list())
    portIndex = 4
    LF = 10
    print " Connecting to ", Serial.list()[portIndex]
    myPort = Serial(this, Serial.list()[portIndex], 9600)  # El this no significa nada en python
                                                           # pero Processing.py lo admite. 
    myPort.bufferUntil(LF)
        
def draw(): 
    background(155, 226, 244)
    for g in globos:
        g.update()
        g.draw()
        
def mousePressed():
    creaGlobo(mouseX,mouseY)
    
def serialEvent(evt):
    global dato
    global datoAnt
    dato = evt.readString()
    dato = dato.strip();     # para quitarle los retornos de carro. 
    if datoAnt == "1":       # TODO: pasarlo a int (no consigo que funcione) 
        if dato == "0":
            creaGlobo(int(random(0,width)),height-100)
    datoAnt = dato

def creaGlobo(x,y):
    c = color(random(255),random(255),random(255))
    globos.append(Globo(random(100,150),
                        c,
                        x,
                        y,
                        0.0,
                        0.0))
    println(len(globos))
