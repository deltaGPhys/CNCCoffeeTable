from graphics import *

class SimGraphics:

    def __init__(self, maxX, maxY):
        self._maxX = maxX
        self._maxY = maxY
        self._statusWidth = 200
        self._statsHeight = 200
        self._scalingFactor = 2
        self._margin = 20
        self._win = GraphWin('CNC Sim', maxX * self._scalingFactor + self._statusWidth + 4 * self._margin, maxY * self._scalingFactor + 2 * self._margin)
        self.setup()

    def setup(self):
        self._win.setBackground('black')

        statsBox = Rectangle(
            Point(0, 0),
            Point(self._statusWidth + 2 * self._margin, self._maxY * self._scalingFactor - 1 + 2 * self._margin)
        )
        statsBox.setOutline('white')
        statsBox.setFill('black')
        statsBox.draw(self._win)

        cncBox = Rectangle(
            Point(self._statusWidth + 2 * self._margin, self._maxY * self._scalingFactor - 1 + 2 * self._margin),
            Point(self._maxX * self._scalingFactor + self._statusWidth - 1 + 4 * self._margin, 0)
        )
        cncBox.setOutline('white')
        cncBox.setFill('black')
        cncBox.draw(self._win)

        cncBox = Rectangle(
            Point(self._statusWidth + 3 * self._margin, self._maxY * self._scalingFactor - 1 + 1 * self._margin),
            Point(self._maxX * self._scalingFactor + self._statusWidth - 1 + 3 * self._margin, self._margin)
        )
        cncBox.setOutline('gray')
        cncBox.setFill('black')
        cncBox.draw(self._win)

        head = Circle(Point(40, 100), 25)  # set center and radius
        head.setFill("yellow")
        head.draw(self._win)

        eye1 = Circle(Point(30, 105), 5)
        eye1.setFill('blue')
        eye1.draw(self._win)

    def clear(self):
        cncBox = Rectangle(
            Point(self._statusWidth + 3 * self._margin, self._maxY * self._scalingFactor - 1 + 1 * self._margin),
            Point(self._maxX * self._scalingFactor + self._statusWidth - 1 + 3 * self._margin, self._margin)
        )
        cncBox.setOutline('gray')
        cncBox.setFill('black')
        cncBox.draw(self._win)

    def drawLine(self, x1, y1, x2, y2):
        line = Line(Point(self._scalingFactor * x1 + self._statusWidth + self._margin * 3, self._scalingFactor * y1 + self._margin), Point(self._scalingFactor * x2 + self._statusWidth + self._margin * 3, self._scalingFactor * y2 + self._margin))
        line.setOutline('cyan')
        line.draw(self._win)

    def drawArc(self):
        pass