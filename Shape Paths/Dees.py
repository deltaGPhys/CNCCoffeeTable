from __future__ import division
xmax = 635
ymax = 220

x = 0
y = 0

diff = 5
R = ymax

print "G21 (mm mode)"
print "G90 (absolute mode)"
print "F2000"
print "G1 X"+str(x)
print "G1 Y"+str(y)
x = x + R/2
print "G1 X"+str(x)

while x < xmax/2:
    #anticlockwise
    print "G2 X"+str(x)+"Y"+str(R)+" R"+str(R/2)
    #nudge forward
    x = x + diff
    print "G1 X"+str(x)

    #clockwise
    print "G3 X"+str(x)+"Y0 R"+str(R/2)
    #nudge forward
    x = x + diff
    print "G1 X"+str(x)

while x < xmax-R/2:
    #clockwise
    print "G3 X"+str(x)+"Y"+str(R)+" R"+str(R/2)
    #nudge forward
    x = x + diff
    print "G1 X"+str(x)
    
    #anticlockwise
    print "G2 X"+str(x)+"Y0 R"+str(R/2)
    #nudge forward
    x = x + diff
    print "G1 X"+str(x)

print "G1 Y0"
print "G1 X0"


    

