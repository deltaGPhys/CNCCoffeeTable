from serial import Serial


# open a pySerial connection to the slave
s_name = "/dev/ttys008"
ser = Serial(s_name, 2400, timeout=1)

filename = '../shape paths/Maze.gcode'
commands = lines = [line.rstrip('\n') for line in open(filename)]

for command in commands:

    ser.write(command+'\r\n')  # write the first command
    res = b""
    while not res.endswith(b'\r\n'):
        # read the response
        res += ser.read()
    print(res)