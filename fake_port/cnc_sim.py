from commands import CommandException, GRBLResponseType, DistanceMode, GRBLResponse


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
        return GRBLResponse(GRBLResponseType.OK, "Feed rate set: " + rate + " " + self._unitMode.value + "/min")

    def setUnitMode(self, unitMode):
        self._unitMode = unitMode
        return GRBLResponse(GRBLResponseType.OK, "Unit mode set: " + unitMode.value)

    def setDistanceMode(self, distanceMode):
        self._distanceMode = distanceMode
        return GRBLResponse(GRBLResponseType.OK, "Distance mode set: " + distanceMode.value)

    def move(self, command, args):
        xArg = args.split("Y")[0][1:]
        yArg = args.split("Y")[1]
        if not (xArg.isnumeric() and yArg.isNumeric()):
            return GRBLResponse(GRBLResponseType.ERROR, "Coordinates were not numeric")
        if self.distanceMode == DistanceMode.ABSOLUTE:
            if xArg <= self._maxX and xArg >= 0 and yArg <= self._maxY and yArg >=0:
                finalX = xArg
                finalY = yArg
                # need to draw here
                self._X = finalX
                self._Y = finalY
                return GRBLResponse(GRBLResponseType.OK, "")

            else:
                error = GRBLResponse(GRBLResponseType.ALARM, "")
                if xArg < 0:
                    self._X = 0
                    error.message += "X low limit switch"
                elif xArg > self._maxX:
                    self._X = self._maxX
                    error.message += "X high limit switch"
                elif yArg < 0:
                    self._Y = 0
                    error.message += "Y low limit switch"
                elif yArg > self._maxY:
                    self._Y = self._maxY
                    error.message += "Y high limit switch"
                return error

        return GRBLResponse(GRBLResponseType.FEEDBACK, "placeholder")







