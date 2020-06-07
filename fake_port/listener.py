import os, pty
from serial import Serial
import threading

def listener(port):
    #continuously listen to commands on the master device
    while 1:
        res = b""
        while not res.endswith(b"\r\n"):
            #keep reading one byte at a time until we have a full line
            res += os.read(port, 1)
        print("command: %s" % res)

        #write back the response
        if res == b'QPGS\r\n':
            os.write(port, b"correct result\r\n")
        else:
            os.write(port, b"I dont understand\r\n")

def create_serial():
    """Start the testing"""
    master,slave = pty.openpty() #open the pseudoterminal
    s_name = os.ttyname(slave) #translate the slave fd to a filename
    print s_name

    listener(master)

if __name__=='__main__':
    create_serial()