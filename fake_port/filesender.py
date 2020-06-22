from serial import Serial


# open a pySerial connection to the slave
s_name = "/dev/ttys008"
ser = Serial(s_name, 2400, timeout=1)

filename = '../shape paths/square checkerboard.gcode'
commands = [line.rstrip('\n') for line in open(filename)]

ser.write('X\r\n')

for command in commands:

    ser.write(command+'\r\n')
    res = b""
    while not res.endswith(b'\r\n'):
        # read the response
        res += ser.read()
    print(res)