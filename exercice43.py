import turtle as t

class Rectangle:
    def __init__(self, longueur, largeur):
        self.longueur = longueur
        self.largeur = largeur

    def draw(self):
        t.fillcolor("black")
        t.begin_fill()
        for _ in range(2):
            t.forward(self.longueur)
            t.left(90)
            t.forward(self.largeur)
            t.left(90)
        t.end_fill()

class Square(Rectangle):
    def __init__(self, cote, inclinaison=30):
        super().__init__(cote, cote)
        self.inclinaison = inclinaison

    def draw(self):
        t.fillcolor("black")
        t.begin_fill()
        t.left(self.inclinaison)
        t.forward(self.longueur)
        t.right(90)
        t.forward(self.longueur)
        t.right(90)
        t.forward(self.longueur)
        t.right(90)
        t.forward(self.longueur)
        t.right(90)
        t.end_fill()
        t.forward(self.longueur)
        t.color("red")
        
# Test
t.speed(2)

# Rectangle
t.penup()
t.goto(-100, 100)
t.pendown()
r = Rectangle(200, 100)
r.draw()

# Square
t.penup()
t.goto(100, 100)
t.pendown()
s = Square(100)
s.draw()

t.done()