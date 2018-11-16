from __future__ import division
from math import *
xmax = 635
ymax = 220

N = 10 # horizontal number (+.5)

d = xmax//(N+.5) # width of each unit (floor division)
offset = (xmax-(N+.5)*d)/2 # space on either side to center pattern
M = 10 # vertical number
h = ymax/M # height of each unit



def smallSpiralRight(unit,x,y,diff):
    D = unit
    
    #print "G91 (relative mode)"
    for i in range(1,6):
        #anticlockwise, then clockwise
        x = x + D*(-1)**i
        print "G2 X"+str(x)+" R"+str(D/2)+" ("+str(x)+","+str(y)+")"
        D = D - diff
    x = x + diff/2
    D = D + diff
    print "G1 X"+str(x)

    for i in range(1,6):
        x = x + D*(-1)**i
        print "G3 X"+str(x)+" R"+str(D/2)+" ("+str(x)+","+str(y)+")"
        D = D + diff

    return([x,y])

def smallSpiralLeft(unit,x,y,diff):
    D = unit
    
    #print "G91 (relative mode)"
    for i in range(1,6):
        #anticlockwise, then clockwise
        x = x - D*(-1)**i
        print "G2 X"+str(x)+" R"+str(D/2)+" ("+str(x)+","+str(y)+")"
        D = D - diff
    x = x - diff/2
    D = D + diff
    print "G1 X"+str(x)

    for i in range(1,6):
        x = x-+ D*(-1)**i
        print "G3 X"+str(x)+" R"+str(D/2)+" ("+str(x)+","+str(y)+")"
        D = D + diff

    return([x,y])


print "G21 (mm mode)"
print "G90 (absolute mode)"
print "F2000"
# clear the area

print "G1 X0"
print "G1 Y0"
# debugging: bounding box"
print "G1 X"+str(xmax)
print "G1 Y"+str(ymax)
print "G1 X0"
print "G1 Y0"


### horizontal back n' forth
##dx = 1
##dy = 2
##while y <= ymax-dy:
##    x = x + dx*xmax #swaps dirs
##    xmax = xmax * -1
##    print "G1 X"+str(x)
##    y = y + dy
##    print "G1 Y"+str(y) 

print "G1 X"+str(offset)
x = offset
y = 0

for j in range(0,M): # loop through the rows
    #half arc
    x = x + ((-1)**j)*d/2
    y = y + h
    g = int((5+(-1)**j)/2) #clockwise or CCW mode
    print "G"+str(g)+" X"+str(x)+" Y"+str(y)+" R"+str(2*h)
    #arcs
    for i in range(0,N): # loop through the arcs
        x = x + ((-1)**j)*d
        print "G"+str(g)+" X"+str(x)+" Y"+str(y)+" R"+str(sqrt(2)*h)

print "G1 X0 Y0"


