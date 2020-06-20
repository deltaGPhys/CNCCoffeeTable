from commands import CommandException, GRBLResponse


class CNCSim:

    def __init__(self, maxX, maxY):
        self._maxX = maxX # max X coordinate, in mm
        self._maxY = maxY # max Y coordinate, in mm
        self._X = 0
        self._Y = 0
        self._feedRate = 0
        self._running = True
        self._unitMode = None
        self._distanceMode = None


    @property
    def maxX(self):
        return self._maxX

    @maxX.setter
    def maxX(self, maxX):
        self._maxX = maxX

    @property
    def maxY(self):
        return self._maxY

    @maxY.setter
    def maxY(self, maxY):
        self._maxY = maxY

    @property
    def X(self):
        return self._X

    @property
    def Y(self):
        return self._Y

    @property
    def feedRate(self):
        return self._feedRate

    @property
    def running(self):
        return self._running

    @property
    def unitMode(self):
        return self._unitMode

    @property
    def distanceMode(self):
        return self._distanceMode


    def setFeedRate(self, command):
        rate = command[1:]
        if not rate.isnumeric():
            self._running = False
            raise CommandException("Rate specified is not numeric")
        self._feedRate = rate
        return GRBLResponse.OK

    def setUnitMode(self, unitMode):
        self._unitMode = unitMode
        return GRBLResponse.OK

    def setDistanceMode(self, distanceMode):
        self._distanceMode = distanceMode
        return GRBLResponse.OK

    def move(self, command):
        return GRBLResponse.







