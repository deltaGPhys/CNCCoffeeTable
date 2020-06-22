import os, pty
from commands import GRBLResponseType, GRBLCommand, ModalGroup
from commands import CommandException
from cnc_sim import CNCSim

def parseCommand(command, sim):
    if command[:1] == "F":
        return sim.setFeedRate(command)
    prefix = command.split(" ")[0]
    for comm in GRBLCommand:
        if prefix == comm.code:
            if comm.modalGroup == ModalGroup.UNITS_MODE:
                return sim.setUnitMode(comm)
            elif comm.modalGroup == ModalGroup.DISTANCE_MODE:
                return sim.setDistanceMode(comm)
            elif comm.modalGroup == ModalGroup.MOTION_MODE:
                args = command.split(" ")[1]
                return sim.move(comm, args)
            elif comm.modalGroup == ModalGroup.FAKE:
                return sim.clear()
            else:
                raise CommandException("Unimplemented command group")
    raise CommandException("Unrecognized command")

def listener(port, sim):
    # continuously listen to commands on the master device
    while sim.running:
        cmd = b""
        while not cmd.endswith(b"\r\n"):
            # keep reading one byte at a time until we have a full line
            cmd += os.read(port, 1)
        print("command received: %s" % cmd)

        # write back the response
        try:
            cmd = cmd.split("(")[0].strip()
            resp = parseCommand(cmd, sim).getText()
        except CommandException as e:
            resp = e.message
        except Exception as e:
            print e
            resp = "Unexpected error state: " + e.message
        os.write(port, resp + "\r\n")

def create_serial():
    """Start the testing"""
    master, slave = pty.openpty()  # open the pseudoterminal
    s_name = os.ttyname(slave)  # translate the slave fd to a filename
    print s_name

    sim = CNCSim(635, 225)

    listener(master, sim)


if __name__ == '__main__':
    create_serial()
