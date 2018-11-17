import serial
import time
import glob, os
import curses

testing = False

# Open grbl serial port ==> CHANGE THIS BELOW TO MATCH YOUR USB LOCATION
try:
    s = serial.Serial('/dev/ttyUSB0',115200) # cu.wchusbserial1450 GRBL operates at 115200 baud. Leave that part alone.
except Exception as e:
    testing = True

# import gcode files   
shapes = []
numclearing = len(glob.glob("clearing paths/*.gcode"))
numshapes = len(glob.glob("shape paths/*.gcode"))
for f in glob.glob("clearing paths/*.gcode"):
    shapes.append(f[15:-6])
for f in glob.glob("shape paths/*.gcode"):
    shapes.append(f[12:-6])

while True:
    # print menu
    print "0. Manual"
    print "== Clearing Paths =="
    for i in range(0,numclearing):
        print str(i)+".",shapes[i]       
    print "== Shape Paths =="
    for i in range(numclearing,numclearing+numshapes):
        print str(i)+".",shapes[i]
    print ""
    choice = raw_input("Your choice: ")

    try:
        if "," not in choice: # single path
            choices = [int(choice) - 1]
        else: # multiple paths
            choicestemp = choice.split(",")
            choices = [int(c.strip()) for c in choicestemp]
        
        direction = ''
        if -1 in choices: #ignore everything else
            while direction != "q":
                direction = raw_input("Direction:")

                if not testing:
                    # Wake up grbl
                    s.write("\r\n\r\n")
                    time.sleep(2)   # Wait for grbl to initialize
                    s.flushInput()  # Flush startup text in serial input
                    s.write("G21 (mm mode)\n")
                    s.write("G91 (relative mode)\n")
                    s.write("F2000\n")
                
                if direction == "a":
                    output = "G1 X-1"
                elif direction == "d":
                    output = "G1 X1"
                elif direction == "w":
                    output = "G1 Y1"
                elif direction == "s":
                    output = "G1 Y-1"
                elif direction == "q":
                    break
                print output

                if not testing:
                    s.write(output + '\n') # Send g-code block to grbl
                    grbl_out = s.readline() # Wait for grbl response with carriage return
                    print ' : ' + grbl_out.strip()

                    
        else: # not manual mode
            for choice in choices: # loop through selected patterns
                filename = shapes[choice]
                if choice < numclearing:
                    filename = "clearing paths/" + filename
                else:
                    filename = "shape paths/" + filename                    

            
                # Open g-code file
                f = open(filename+'.gcode','r');

                # Wake up grbl
                s.write("\r\n\r\n")
                time.sleep(2)   # Wait for grbl to initialize
                s.flushInput()  # Flush startup text in serial input

                # Stream g-code to grbl
                for line in f:
                    l = line.strip() # Strip all EOL characters for consistency
                    print 'Sending: ' + l,
                    s.write(l + '\n') # Send g-code block to grbl
                    grbl_out = s.readline() # Wait for grbl response with carriage return
                    print ': ' + grbl_out.strip()

                # Wait here until grbl is finished to close serial port and file.
                raw_input("  Press <Enter> to exit and disable grbl.")

                # Close file and serial port
                f.close()
                s.close()

    except Exception as e:
        print "Invalid input:", e
