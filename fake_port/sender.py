from serial import Serial


# open a pySerial connection to the slave
s_name = "/dev/ttys008"
ser = Serial(s_name, 2400, timeout=1)

commands = ["G21 (mm mode)",
            "F2000",
            "G90 (absolute mode)",
            "G1 X20Y40",
            "G91 (relative mode)",
            "G1 X0Y40",
            "G1 X-20Y-40",
            "G1 X60Y0"
            ]
for command in commands:

    ser.write(command+'\r\n')  # write the first command
    res = b""
    while not res.endswith(b'\r\n'):
        # read the response
        res += ser.read()
    print(res)