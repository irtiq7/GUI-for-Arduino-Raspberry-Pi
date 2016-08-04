'''# GUI-for-Arduino-Raspberry-Pi
This is a Work in Progress Graphical User Interface (GUI) that will be able to communicate with an Arduino and raspberry Pi using serial interface.
This is a Work in Progress Interface and a lot will change in the upcoming months.All in all, feel free to use this code for self study!
'''
#!/usr/bin/python
from Tkinter import *

import sys
import time
import serial
import serial.tools.list_ports

root = Tk()
bottomframe = Frame(root).grid()
port_list = []
port = []
global save_port
global input_CTRL
global ser_CTRL
i = 0
def savebutton():
	global ser_CTRL
	input_CTRL = E1.get()
	#~ # configure the serial connection
	portname = 'COM'+str(input_CTRL)
	save_port = portname
	ser_CTRL = serial.serial_for_url(portname, baudrate = 9600, parity=serial.PARITY_NONE, bytesize=serial.EIGHTBITS, stopbits=serial.STOPBITS_ONE, timeout=2)
	if(not ser_CTRL.isOpen()):
		Label(root, text =str(ser_CTRL.name) + " cannot be opened. Exiting. \r\n").grid(row=13, sticky='S')
		ser_CTRL.close()
		time.sleep(5)
		sys.exit()
	Label(bottomframe, text="--------COM"+str(input_CTRL)+" CONNECTED-----------", bg='green',fg="black").grid(row=16, column=0, sticky='S')
	#~ print(ser_CTRL.port + " open.\r\n")
	#~ print(portname)
	time.sleep(1)

#~ for port in serial.tools.list_ports.comports():
    #~ Label(root,text= str('{0:4} : {1:10}\r'.format(int(port[0][3:]), port[1]))).grid(row=6+i, sticky='S')
    #~ i += 1
#~ for port in serial.tools.list_ports.comports():
    #~ port_list.insert(i, port[0][3:])
    #~ i += 1
#~ if(len(port_list)==0):
	#~ Label(root, text="Bluebox not connected!", bg='red',fg="yellow").grid(row=14, column=0, sticky="S")
	#~ Label(root, text="Connect and restart the software!", bg='red',fg="yellow").grid(row=15, column=0, sticky="S")
#~ print port_list

E1 = Entry(root, text = "Enter COM number")
E1.focus_set()
E1.grid(row=10, sticky='S')
Button(root, text="CONNECT", command = savebutton).grid(row=11,sticky='S')


def PWMButtonPress():
	PWMvalue = PWMscale.get()
	send = "A%d"%(PWMvalue)
	ser_CTRL.write(send)
	print send

def pinsselection():
	top = Toplevel(root)
	global var1, var2, var3, var4
	var1, var2, var3, var4 = IntVar(),IntVar(),IntVar(),IntVar()
	Checkbutton(top, text="PIN1", variable=var1).grid(row=0, column=0, sticky='W')
	Checkbutton(top, text="PIN3", variable=var3).grid(row=0, column=1, sticky='W')
	Checkbutton(top, text="PIN2", variable=var2).grid(row=1, column=0, sticky='E')
	Checkbutton(top, text="PIN4", variable=var4).grid(row=1, column=1, sticky='E')
	B1 = Button(top, text="SET", command=pins_states).grid(row=2, sticky='S')
def pins_states():
	#~ print(ser_CTRL)
	#~ print(save_port)

	try:

		#~ ser_CTRL = serial.serial_for_url(save_port, baudrate = 9600, parity=serial.PARITY_NONE, bytesize=serial.EIGHTBITS, stopbits=serial.STOPBITS_ONE, timeout=2)
		#~ time.sleep(2)
		PIN1 = var1.get()
		PIN2 = var2.get()
		PIN3 = var3.get()
		PIN4 = var4.get()
		send = "P%d%d%d%d"%(PIN1, PIN2, PIN3, PIN4)
		ser_CTRL.write(send)
		print(send)
		#~ response = ser_CTRL.readline()   # read a '\n' terminated line
		#~ print response+"hi"
		#~ print(ser_CTRL1)
		#~ print(ser_CTRL)
		#~ B1.config(state=Tkinter.ACTIVE)
	except:
		#~ ser_CTRL = serial.serial_for_url(save_port, baudrate = 9600, parity=serial.PARITY_NONE, bytesize=serial.EIGHTBITS, stopbits=serial.STOPBITS_ONE, timeout=2)
		#~ time.sleep(2)
		PIN1 = var1.get()
		PIN2 = var2.get()
		PIN3 = var3.get()
		PIN4 = var4.get()
		send = "P%d%d%d%d"%(PIN1, PIN2, PIN3, PIN4)
		ser_CTRL.write(send)
		print(send)
		response = ser_CTRL.readline()   # read a '\n' terminated line
		#~ print response+"except"
		#~ print(ser_CTRL1)
		#~ print(ser_CTRL)
		#~ B1.config(state=Tkinter.ACTIVE)



#Welcome screen

Label(root, text="::BlueBox by Usama::", bg='blue', fg='yellow').grid(row=0, column=0, sticky='N')
Label(root, text="------------------------------------", fg="black").grid(row=1, column=0, sticky='N')
#~ Label(root, text="-----------------------", fg="black").grid(row=3, column=0, sticky='W')
#~ Label(root, text="-----------------------", fg="black").grid(row=5, column=0, sticky='W')
#Connection pallette and button
Label(bottomframe, text="---------N0 CONNECTION------------", bg='red',fg="yellow").grid(row=16, column=0, sticky='S')
#~ Button(bottomframe, text='CONNECT', command=connectPort).grid(row=9, column=0, sticky='S')
#Checkbuttons for ucontroller pins
Label(root, text="PINS SELECTION", fg="black").grid(row=2, column=0, sticky='N')
Label(root, text="------------------------------------", fg="black").grid(row=3, column=0, sticky='S')
Button(root, text="PINS SELECTION", command=pinsselection).grid(row=3, column=0, sticky='W')

Label(root, text="------------------------------------", fg="black").grid(row=7, column=0, sticky='S')
#Scale for measuring PWM
Label(root, text="------------------------------------", fg="black").grid(row=1, column=1, sticky='N')
Label(root, text="PWM SELECTION", fg="black").grid(row=2, column=1, sticky='N')
Label(root, text="------------------------------------", fg="black").grid(row=3, column=1, sticky='S')
PWMscale = Scale(root, from_=0, to=100, orient=HORIZONTAL)
PWMscale.focus_set
PWMscale.grid(row=4, column=1, sticky='N')
PWMButton = Button(root, text='SET', command = PWMButtonPress).grid(row=5, column=1, sticky='S')

root.mainloop()

