import os, pty
from commands import GRBLResponseType, GRBLCommand, ModalGroup
from commands import CommandException
from cnc_sim import CNCSim


def parseCommand(command, sim):
    if command[:1] == "F":
        return sim.setFeedRate(command)
    prefix = command.split(" ")[0]
    for comm in GRBLCommand.items():
        if prefix == comm.code:
            if comm.modalGroup == ModalGroup.UNITS_MODE:
                sim.setUnitMode = comm
                return sim.feedback
            elif comm.modalGroup == ModalGroup.DISTANCE_MODE:
                sim.distanceMode = comm
                return sim.feedback
            elif comm.modalGroup == ModalGroup.MOTION_MODE:
                args = command.split(" ")[1]
                sim.move(comm, args)
                return sim.feedback
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
            resp = parseCommand(cmd, sim)
        except CommandException as e:
            resp = e.message
        except:
            resp = "Unexpected error state"
        os.write(resp)

def create_serial():
    """Start the testing"""
    master, slave = pty.openpty()  # open the pseudoterminal
    s_name = os.ttyname(slave)  # translate the slave fd to a filename
    print s_name

    sim = CNCSim()

    listener(master, sim)


if __name__ == '__main__':
    create_serial()
