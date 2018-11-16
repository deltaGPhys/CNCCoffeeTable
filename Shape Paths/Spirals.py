from __future__ import division
xmax = 635
ymax = 220

R = ymax
unit = 90
diff = unit/5
N = 6

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
### debugging: bounding box"
print "G1 X"+str(xmax)
print "G1 Y"+str(ymax)
print "G1 X0"
print "G1 Y0"
##
##x = 0
##y = 0
### horizontal back n' forth
##dx = 1
##dy = 2
##while y <= ymax-dy:
##    x = x + dx*xmax #swaps dirs
##    xmax = xmax * -1
##    print "G1 X"+str(x)
##    y = y + dy
##    print "G1 Y"+str(y) 

#x = x + unit/2
#y = y - unit/2 - diff/2
print "G1 Y"+str(ymax)
x = xmax-(xmax-(N+.75)*unit)/2
print "G1 X"+str(x-unit/2)

#x = xmax-(xmax-(N+.75)*unit)/2
y = ymax*.75
print "G2 X"+str(x)+" Y"+str(y)+" R"+str(unit/2+ diff/2)

#print "G1 X"+str(x) #start positions
#print "G1 Y"+str(y)

for j in range(0,N):
    x,y = smallSpiralRight(unit,x,y,diff)
    
#arc to next row
x = x + unit/2
y = y - unit/2 - diff/2
print "G3 X"+str(x)+" Y"+str(y)+" R"+str(unit/2+ diff/2)


#y = ymax*.5
print "G1 Y"+str(y)
for j in range(0,N-1):
    x,y = smallSpiralLeft(unit,x,y,diff)

#arc to next row
x = x + unit/2
y = y - unit/2 - diff/2
print "G2 X"+str(x)+" Y"+str(y)+" R"+str(unit/2+ diff/2)


print "G1 Y"+str(y)
for j in range(0,N):
    x,y = smallSpiralRight(unit,x,y,diff)

#arc to next row
x = x + unit/2
y = y - unit/2 - diff/2
print "G3 X"+str(x)+" Y"+str(0)+" R"+str(unit/2+ diff/2)

print "G1 X0 Y0"

    
##
##    #clockwise
##    print "G3 X"+str(x)+"Y0 R"+str(R/2)
##    #nudge forward
##    x = x + diff
##    print "G1 X"+str(x)



