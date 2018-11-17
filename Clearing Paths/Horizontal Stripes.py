from __future__ import division
xmax = 635
ymax = 220

diff = 20
R = ymax

print "G21 (mm mode)"
print "G90 (absolute mode)"
print "F2000"
# clear the area


print "G1 X0"
print "G1 Y0"
#print "G1 X635"
print "G1 Y220"

y = ymax + 5
x = 0
while y >= 0:
    if x == 0:
        x = xmax
    else:
        x = 0
    # down
    print "G1 Y"+str(y)
    y = y - 5
    print "G1 X"+str(x)

    



