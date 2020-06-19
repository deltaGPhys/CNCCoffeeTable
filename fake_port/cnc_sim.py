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

    @feedRate.setter
    def feedRate(self, feedRate):
        self._feedRate = feedRate

    @property
    def running(self):
        return self._running

    @running.setter
    def running(self, running):
        self._running = running

    @property
    def unitMode(self):
        return self._unitMode

    @unitMode.setter
    def unitMode(self, unitMode):
        self._unitMode = unitMode

    @property
    def distanceMode(self):
        return self._unitMode

    @distanceMode.setter
    def distanceMode(self, distanceMode):
        self._distanceMode = distanceMode





