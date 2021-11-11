import turtle

class map:

  def __init__(self):
    self.screen = turtle.Screen()
    self.screen.setup(width = 1.0, height = 1.0)
    self.screen.tracer(False)
    self.drawGrid()
    self.drawInfinityStone(imageName="infinityStoneYellow.gif", xpos=0, ypos=100)
    self.drawInfinityStone(imageName="infinityStoneRed.gif", xpos=-200, ypos=100)
    self.drawInfinityStone(imageName="infinityStoneBlue.gif", xpos=-200, ypos=-100)
    self.drawInfinityStone(imageName="infinityStoneGreen.gif", xpos=200, ypos=-100)
    self.screen.tracer(True)

  def drawGrid(self):
    grid = turtle.Turtle()
    grid.color("lightgrey")
    self.drawSquare(grid, 100, -200, 100)
    self.drawSquare(grid, 100, -200, 0) 
    self.drawSquare(grid, 100, -100, 100)
    self.drawSquare(grid, 100, -100, 0) 
    self.drawSquare(grid, 100, 0, 0)
    self.drawSquare(grid, 100, 0, 100)
    self.drawSquare(grid, 100, 100, 100)
    self.drawSquare(grid, 100, 100, 0) 
    grid.penup()
    grid.color("black")
    grid.setpos(-15,150)
    grid.write("Norden")
    grid.setpos(-270,-5)
    grid.write("Westen")
    grid.setpos(230,-5)
    grid.write("Osten")
    grid.hideturtle()
    grid.setpos(-15,-150)
    grid.write("Süden")
    grid.hideturtle()

  def drawSquare(self, turtleObject, length, xpos, ypos):
    turtleObject.penup()
    turtleObject.setpos(xpos,ypos)
    turtleObject.pendown()
    turtleObject.forward(length)
    turtleObject.right(90)
    turtleObject.forward(length)
    turtleObject.right(90)
    turtleObject.forward(length)
    turtleObject.right(90)
    turtleObject.forward(length)
    turtleObject.right(90)

  def drawInfinityStone(self, imageName, xpos, ypos):
    self.screen.addshape(imageName)
    infinityStone = turtle.Turtle()
    infinityStone.penup()
    infinityStone.setpos(xpos,ypos)
    infinityStone.shape(imageName)
    return infinityStone
    
    
class thanos:

  def __init__(self, screen):
    self.distanceFactor = 10
    self.screen = screen
    self.screen.addshape("thanos_mini.gif")
    self.thanos = turtle.Turtle()
    self.thanos.color("purple")
    self.thanos.setpos(0,0)
    self.thanos.width(2)
    self.thanos.shape("thanos_mini.gif")

  def goNorth(self,distance):
    self.thanos.setheading(90)
    self.thanos.forward(distance*self.distanceFactor)

  def goWest(self,distance):
    self.thanos.setheading(180)
    self.thanos.forward(distance*self.distanceFactor)

  def goSouth(self,distance):
    self.thanos.setheading(270)
    self.thanos.forward(distance*self.distanceFactor)

  def goEast(self,distance):
    self.thanos.setheading(0)
    self.thanos.forward(distance*self.distanceFactor)