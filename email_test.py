from imports import jarvis, funcs
import datetime
import time as td

time = "6:30:00".split(":")

time = (int(time[0])*(60*60))+(int(time[1])*60)+int(time[2])
functions = funcs.functions

commands = funcs.commands
print("alarm gone off? y/n")
if input("\-->") == "y":
    ticker = 1
else:
    ticker = 0

while 1:
    currentDT = str(datetime.datetime.now()).split()[1].split(":")
    currentDT=(int(currentDT[0])*(60*60))+(int(currentDT[1])*60)+int(float(currentDT[2]))
    print(currentDT)
    print(time)
    if currentDT >  time and ticker == 0:
        print("its coming")
        funcs.say_str("max wake up max wake up max wake up max wake up max wake up max wake up max wake up max wake up max wake up max wake up max wake up max wake up max wake up max wake up max wake up max wake up max wake up max wake up max wake up max wake up max wake up max wake up max wake up max wake up max wake up max wake up max wake up max wake up max wake up max wake up max wake up max wake up max wake up max wake up max wake up max wake up max wake up max wake up max wake up max wake up max wake up max wake up max wake up max wake up max wake up max wake up max wake up max wake up max wake up max wake up max wake up max wake up max wake up max wake up max wake up max wake up max wake up max wake up max wake up max wake up max wake up max wake up max wake up max wake up max wake up max wake up max wake up max wake up max wake up max wake up max wake up max wake up max wake up max wake up max wake up max wake up max wake up max wake up max wake up max wake up max wake up max wake up max wake up max wake up max wake up max wake up max wake up max wake up max wake up max wake up max wake up max wake up max wake up max wake up max wake up max wake up max wake up max wake up max wake up max wake up max wake up max wake up max wake up max wake up max wake up max wake up max wake up max wake up max wake up max wake up max wake up", "test")
        print("yes")
        ticker = 1
    else:
        if currentDT < time+(5*60):
            print("armed")
            ticker = 0
    try:
        
        
        jarvis.main.read_mail(commands, functions)
    except:
        print("owww nooooo")
