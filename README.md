# SecurityDoorAlarm
Door alarm using microbit and python.

Using the microbit’s magnetometer to sound an alarm when the front door is open. 
The microbit sender will send a signal to receiver microbit in another part of the room to sound an 
alarm when the door is open. Signals are send using microbit’s Bluetooth. 


Project Components Used: 
•	3 microbits
•	2 battery packs
•	Blu tak
•	Breadboard
•	Buzzer
•	Neodymium magnet
•	Jumper wires
•	Microbit expansion board
•	Old Cell Phone Case
•	Keyestudio Micro bit Sensor V2 Shield
•	Red LED module


Supplemental Activities: 
Magnetic Reading for magnet:


Magnetic Reading
Distance	Magnetic Force Strength
no magnet	59.98 microtesla
0 mm	2301.96 microtesla
1 mm	1830.34 microtesla
2 mm	1769.75 microtesla
magnetic force strength is the average of 3 readings taken

ALGORITHM FOR CODING: 
	Sender:
		Connect to channel 7
	Read magnetic force
	If door is open (magStrength is less than 1750 microteslas)
		Send number 1 to Receiver
		Show check mark symbol
	Else (door is close) 
send number 2 to receiver
		show symbol ‘x’

Receiver: 
	Connect to channel 7
	Check for signal
		If receivedNumber is 1 
			Then show angry face
			Play loud sound
				If button A is pressed 
					Stop all sound
		If receivedNumber is 2
			Then show check mark symbol
			Stop loud sound
	Keep checking packet signal strength
		If strength is less than 0 
			Play loud sound
			If button press B is pressed 
			Stop sound
LED Receiver 2: 
		Connect to channel 7
		Check for signal
			If receivedNumber is 3
			Turn on Red LED for 1 ms
			Turn off Red LED for 1 ms
