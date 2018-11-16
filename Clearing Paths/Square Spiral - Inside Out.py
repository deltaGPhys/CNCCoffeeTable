from __future__ import division
xmax = 635
ymax = 220

xb = 0
yb = 0
xt = xmax
yt = ymax

diff = 5
diffy = ymax*diff/xmax
n = 0



xb = 320
xt = 315
yb = 110.866141732
yt = 109.133858268

while xb >= 0 and xt <= xmax and yb >= 0 and yt <= ymax:
    yb = yb - diffy
    
    print "G1 X" + str(int(xt))
    print "G1 Y" + str(int(yt))
    print "G1 X" + str(int(xb))
    print "G1 Y" + str(int(yb))

    xb = xb - diff
    xt = xt + diff
    yt = yt + diffy
    n = n + 1
print "G1 X0"
