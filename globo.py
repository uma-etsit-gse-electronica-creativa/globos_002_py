class Globo(object):
    
    #Constructor
    def __init__(self, diametro, col, x, y, vx, vy):
        self.d = diametro
        self.col = col
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
       
    #Actualizar el estado del globo
    def update(self):
        self.vy -= random(0.02, 0.05)
        self.vx += random(-0.1, 0.1)
        self.x = self.x + self.vx
        self.y = self.y + self.vy
        
    #Dibujar el globo
    def draw(self):
        push()
        fill(self.col)
        translate(self.x, self.y)
        ellipse(0, 0, self.d, self.d)
        translate(0, self.d/2.0+5)
        triangle(0,-5,-5,0,5,0)
        pop()
