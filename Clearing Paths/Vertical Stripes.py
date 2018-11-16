from __future__ import division
xmax = 635
ymax = 220

x = 8
y = 0

diff = 20
R = ymax

print "G21 (mm mode)"
print "G90 (absolute mode)"
print "F2000"
# clear the area


print "G1 X0"
print "G1 Y0"
print "G1 X630"
x = 630
while x > 0:
    y = ymax
    # up
    print "G1 Y"+str(y)
    x = x - 5
    print "G1 X"+str(x)
    y = 0
    #down
    print "G1 Y"+str(y)
    x = x - 5
    print "G1 X"+str(x)

    



