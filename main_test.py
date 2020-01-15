from imports import jarvis, funcs
import serial
import time
import pyttsx3

print(dir(funcs.functions))

functions = funcs.functions

commands = funcs.commands

in_commands = False

jarvis = jarvis.main()
while True:
    data = jarvis.speach_get(15)
    print(jarvis.search_algorithm(commands, functions, "jarvis say testtest", "jarvis"))
