import math
class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def muovi(self, dx, dy):
        self.x += dx
        self.y += dy

    def distanza_da_origine(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)
    

p = Punto(3, 4)

print("Distanza dall'origine:", p.distanza_da_origine()) 

p.muovi(-1, 2)
print("Nuove coordinate:", p.x, p.y)

print("Nuova distanza dall'origine:", p.distanza_da_origine())