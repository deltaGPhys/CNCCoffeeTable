from graphics import *

class SimGraphics:

    def __init__(self, maxX, maxY):
        print maxX, maxY
        self._maxX = maxX
        self._maxY = maxY
        self._statusWidth = 200
        self._statsHeight = 200
        self._scalingFactor = 2
        self._win = GraphWin('CNC Sim', maxX * self._scalingFactor + self._statusWidth, maxY * self._scalingFactor)
        self.setup()

    def setup(self):
        self._win.setBackground('black')

        statsBox = Rectangle(Point(0, 0), Point(self._statusWidth, self._maxY * self._scalingFactor - 1))
        statsBox.setOutline('white')
        statsBox.setFill('black')
        statsBox.draw(self._win)

        cncBox = Rectangle(Point(self._statusWidth, self._maxY * self._scalingFactor - 1), Point(self._maxX * self._scalingFactor + self._statusWidth - 1, 0))
        cncBox.setOutline('white')
        cncBox.setFill('black')
        cncBox.draw(self._win)

        head = Circle(Point(40, 100), 25)  # set center and radius
        head.setFill("yellow")
        head.draw(self._win)

        eye1 = Circle(Point(30, 105), 5)
        eye1.setFill('blue')
        eye1.draw(self._win)

    def draw(self, x1, y1, x2, y2):
        line = Line(Point(x1 + self._statusWidth, y1), Point(x2 + self._statusWidth, y2))
        line.setOutline('cyan')
        line.draw(self._win)
