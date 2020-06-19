from serial import Serial


# open a pySerial connection to the slave
s_name = "/dev/ttys011"
ser = Serial(s_name, 2400, timeout=1)
ser.write(b'test2\r\n')  # write the first command
res = b""
while not res.endswith(b'\r\n'):
    # read the response
    res += ser.read()
print("result: %s" % res)
ser.write(b'QPGS\r\n')  # write a second command
res = b""
while not res.endswith(b'\r\n'):
    # read the response
    res += ser.read()
print("result: %s" % res)