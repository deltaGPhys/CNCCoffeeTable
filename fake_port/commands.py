from enum import Enum

class ModalGroup(Enum):
    MOTION_MODE = 0
    COORDINATE_SYSTEM_SELECT = 1
    PLANE_SELECT = 2
    DISTANCE_MODE = 3
    ARC_IJK_DISTANCE_MODE = 4
    FEED_RATE_MODE = 5
    UNITS_MODE = 6
    CUTTER_RADIUS_COMPENSATION = 7
    TOOL_LENGTH_OFFSET = 8
    PROGRAM_MODE = 9
    SPINDLE_STATE = 10
    COOLANT_STATE = 11

class GRBLCommand(Enum):
    G1 = ("G1", "Linear Interpolation", ModalGroup.MOTION_MODE, "Switch to linear motion at the current feed rate. "
                                                                "Used to cut a straight line --- the interpreter will "
                                                                "determine the acceleration needed along each axis to "
                                                                "ensure direct movement from the original to the destination "
                                                                "point at no more than the current Feed rate ")
    G21 = ("G21", "Unit mode: mm", ModalGroup.UNITS_MODE, "Best practice: do this at the start of a program and nowhere else. "
                                                          "The usual minimum increment in G21 (one thousandth of a millimeter, "
                                                          ".001 mm, that is, one micrometre)")
    G20 = ("G20", "Unit mode: in", ModalGroup.UNITS_MODE, "Best practice: do this at the start of a program and nowhere else. "
                                                          "The usual minimum increment in G20 is one ten-thousandth of an inch "
                                                          "(0.0001")
    G90 = ("G90", "Switch to absolute distance mode", ModalGroup.DISTANCE_MODE, "Coordinates are now relative to the origin of the "
                                                                                "currently active coordinate system, as opposed to "
                                                                                "the current position. G0 X-10 Y5 will move to the "
                                                                                "position 10 units to the left and 5 above the origin "
                                                                                "X0,Y0")
    G91 = ("G91", "Switch to incremental distance mode", ModalGroup.DISTANCE_MODE, "Coordinates are now relative to the current position, "
                                                                                   "with no consideration for machine origin. G0 X-10 Y5 "
                                                                                   "will move to the position 10 units to the left and 5 "
                                                                                   "above the current position")
    F = ("F", "Define feed rate", ModalGroup.FEED_RATE_MODE, "Unit used is that set by G20 or G21. The Feed setting in the G-Code determines "
                                                             "the maximum rate at which the motor can rotate when moving a given distance so "
                                                             "as to get up to (but not exceed) the Feed rate and the maximum acceleration limit "
                                                             "which is set in Grbl. Valid until next F command")

    def __init__(self, command, description, modalGroup, longDescription):
        self.command = command
        self.description = description
        self.longDescription = longDescription
        self.modalGroup = modalGroup

class GRBLResponse(Enum):
    OK = ("ok", "Command accepted")
    ERROR = ("error", "Error state")
    ALARM = ("ALARM", "ALARM - processes suspended")
    FEEDBACK = ("[]", "Parameters or Gcode state response")
    STATUS = ("<>", "Status report")

    def __init__(self, prefix, description):
        self.prefix = prefix
        self.description = description

class UnitMode(Enum):
    MM = 0
    IN = 0

class DistanceMode(Enum):
    ABSOLUTE = 0
    RELATIVE = 1


