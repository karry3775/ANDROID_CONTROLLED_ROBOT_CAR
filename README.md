# keyboard_control
This is a test file for a tilt_car_project which involves motor control using Sensor data from Android. In this case the values 
are obtained from command line but for my next project the values will be fed real-time from an android sensor!

# tilt_car_project
This is the main file that needs to be run in order to control the motion of the car using mobile tilt data. The basic functionality is that when the mobile is tilted forward the car moves forward and when the mobile is tilted backwards the car moves backward. This is possible by just tracking the pitch of the android device. Currently this works while connected to USB. Next step would be to control it using a bluetooth module so that wireless communication can be established
The ino file is same as the keyboard_control uses.

# full_functionality_tilt_car_project
This is an update on the previous version "tilt_car_project". This one provides the car functionality to move forward, backward, turn right and turn left.
To move the car in this setting, first open up the app in your android device, then enter the internal ip address xxx.xxx.x.xx:5000
Open up the python file for this while the ino code is already uploaded.

# Bluetooth connection link
https://www.jaredwolff.com/get-started-with-bluetooth-low-energy/#show1

# Setting up ESP8266MOD node-mcu
https://www.youtube.com/watch?v=NEo1WsT5T7s ;
iwgetid - command to discover the SSID name of the wifi network you are connected to ;
https://tttapa.github.io/ESP8266/Chap07%20-%20Wi-Fi%20Connections.html (FOLLOW THIS TUTORIAL);
PS: Use your phone's network beacause the general wifi might be too crowded

