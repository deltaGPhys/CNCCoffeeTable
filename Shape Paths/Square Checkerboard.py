from __future__ import division
xmax = 635
ymax = 220

diff = 5
offsetx = 8
offsety = 5
Nx = 5
width = 620/Nx
Ny = 3
height = 210/Ny

x = offsetx
y = offsety

print "G21 (mm mode)"
print "G90 (absolute mode)"
print "F2000"
print "G1 X"+str(offsetx)+" Y0"

#bounding box
print "G1 Y"+str(ymax-offsety)
print "G1 X"+str(xmax-offsetx)
print "G1 Y0"
print "G1 X0"

print "G1 X"+str(x)
print "G1 Y"+str(y)

# horizontal box: lower right to upper left
def boxh(x,y,rows):
    for i in range (0,rows):
        x = x + (-1)**i * width
        print "G1 X" + str(x)
        if i < rows - 1:
            y = y + diff
            print "G1 Y" + str(y)

    return [x,y]
    

# vertical box: upper right to lower left
def boxv(x,y,cols):
    for i in range (1,cols+1):
        y = y + (-1)**i * height
        print "G1 Y" + str(y)
        if i < cols:
            x = x + diff
            print "G1 X" + str(x)

  #  y = y + diff
  #  print "G1 Y" + str(y)
    return [x,y]

# vertical box2: lower right to upper left
def boxv2(x,y,cols):
    for i in range (1,cols+1):
        y = y - (-1)**i * height
        print "G1 Y" + str(y)
        if i < cols:
            x = x - diff
            print "G1 X" + str(x)

  #  y = y + diff
  #  print "G1 Y" + str(y)
    return [x,y]

# horizontal box2: upper right to lower left
def boxh2(x,y,rows):
    for i in range (0,rows):
        x = x - (-1)**i * width
        print "G1 X" + str(x)
        if i < rows - 1:
            y = y - diff
            print "G1 Y" + str(y)

    return [x,y]

r = 0
c = 0
while c < Ny:

    while r < Nx:    
        [x,y] = boxh(x,y,int(height/diff) + 1)
        r = r + 1
        if r < Nx:
            [x,y] = boxv(x,y,int(width/diff) + 1)
            r = r + 1
    c = c + 1
    if c < Ny:
        while r > 0:
            [x,y] = boxv2(x,y,int(width/diff)+1)   
            r = r - 1
            if r > 0:
                [x,y] = boxh2(x,y,int(height/diff)+1)   
                r = r - 1
        c = c + 1
    
print "G1 Y0"
print "G1 X0"
    

