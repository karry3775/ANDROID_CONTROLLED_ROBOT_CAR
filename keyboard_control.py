import serial #serial imported for Serial Communication
import time #required to use delay functions

ArduinoSerial = serial.Serial('/dev/ttyACM0',9600) #change /dev/ttyACM0 with the serial port on your computer
#sleeping for 2 seconds for communication to be established
time.sleep(2)

#Now we are ready to read anything coming from ArduinoSerial
print(ArduinoSerial.readline())

#can also assign the value to a variable and use it for computations
while True:
    # print("Enter the number")
    var = raw_input() #get input from user
    print "you entered", var #print the input for confirmation
    k = int (var)

    #logic for forward back and stopping
    if(20<k<=90):
        p = '1'
    if(270<k<=340):
        p = '2'
    if((0<k<=20)or(340<k<=360)):
        p = '0'

    ArduinoSerial.write(p)
    time.sleep(1)
