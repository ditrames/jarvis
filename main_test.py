from imports import jarvis, funcs
import serial
import time
import pyttsx3

print(dir(funcs.functions))

functions = funcs.functions

commands = funcs.commands

in_commands = False

while True:
    for i in "COM0", "COM1", "COM2", "COM3", "COM4", "COM5", "COM6", "COM7", "COM8":
        try:
            ser = serial.Serial(i, 2000000)
            time.sleep(7)
            print("connected at", i)
            ser.write("276894".encode())
            data = ser.readline()
            break
        except Exception as e:
            print(e)

    data = ""
    data = jarvis.main.speach_get(15)
    try:
        
        print(jarvis.main.jarvis_strip(commands, functions, data, True, True))
    except:
        print("hello josh im gay")
