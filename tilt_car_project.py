import sys
from flask import Flask
from flask_sockets import Sockets

#library  inlcusion for socket Communication
import serial #serial imported for Serial Communication
import time #required to use delay function

ArduinoSerial = serial.Serial('/dev/ttyACM0',9600)
time.sleep(2)
print(ArduinoSerial.readline())


app = Flask(__name__)
sockets = Sockets(app)
var = '0'


def ret_routine_code(k):
	return k
def routine_code(array):
	global var

	k = float(array[1])
	print(type(k))
	ret_routine_code(k)
	print("the value of k is {}".format(k))
	if (20<k<=90):
		var = '1' #for forward
		print("inside the forward if statement")
	if (270<k<=340):
		var = '2' #for backward
		print("inside the back if statement")
	if ((0<k<=20)or(340<k<=360)):
		var='0' #for stopping
		print("inside the stop if statement")

	ArduinoSerial.write(var)


@sockets.route('/orientation')

def echo_socket(ws):
	f=open("orientation.txt","a")
	while True:
		message = ws.receive()
                # print(message)
		array = message.split(',')
		print(array[1])
		routine_code(array)
                ws.send(message)
                print>>f,message


	f.close()

@app.route('/')
def hello():
	return 'Hello World!'

if __name__ == "__main__":
	from gevent import pywsgi
	from geventwebsocket.handler import WebSocketHandler
	server = pywsgi.WSGIServer(('0.0.0.0', 5000), app, handler_class=WebSocketHandler)
	server.serve_forever()
