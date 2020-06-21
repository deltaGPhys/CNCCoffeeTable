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
        rate = command[1:].strip()
        if not rate.isdigit():
            self._running = False
            raise CommandException("Rate specified is not numeric")
        if self._unitMode == None:
            self._running = False
            return GRBLResponse(GRBLResponseType.ERROR, "Unit mode not set")
        self._feedRate = rate
        return GRBLResponse(GRBLResponseType.OK, "Feed rate set: " + rate + " " + self._unitMode.value + "/min")

    def setUnitMode(self, unitModeCommand):
        self._unitMode = unitModeCommand.getUnitMode()
        return GRBLResponse(GRBLResponseType.OK, "Unit mode set: " + self._unitMode.value)

    def setDistanceMode(self, distanceModeCommand):
        self._distanceMode = distanceModeCommand.getDistanceMode()
        return GRBLResponse(GRBLResponseType.OK, "Distance mode set: " + self._distanceMode.value)

    def move(self, command, args):
        xArg = args.split("Y")[0][1:]
        yArg = args.split("Y")[1].strip()
        try:
            xArg = int(xArg)
            yArg = int(yArg)
        except Exception as e:
            return GRBLResponse(GRBLResponseType.ERROR, "Coordinates were not numeric")

        if self.distanceMode == DistanceMode.ABSOLUTE:
            self._X = xArg
            self._Y = yArg
        elif self.distanceMode == DistanceMode.RELATIVE:
            self._X += xArg
            self._Y += yArg
        else:
            return GRBLResponse(GRBLResponseType.ERROR, "Distance mode not set")

        # check for error state (out of bounds)
        error = self.checkLimits()
        if error != None: return error

        # need to draw here

        return GRBLResponse(GRBLResponseType.OK, "Final position: X:" + str(self._X) + ", Y:" + str(self._Y))

    def checkLimits(self):
        error = GRBLResponse(GRBLResponseType.ALARM, "")
        if self._X > self._maxX:
            self._X = self._maxX
            error.message += "X high limit switch "
        if self._X < 0:
            self._X = 0
            error.message += "X low limit switch "
        if self._Y > self._maxY:
            self._Y = self._maxY
            error.message += "Y high limit switch "
        if self._Y < 0:
            self._Y = 0
            error.message += "Y low limit switch "
        if (error.message != ""):
            return error
        else:
            return None





