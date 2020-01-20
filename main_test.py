from imports import jarvis, funcs
import serial
import time
import pyttsx3

functions = funcs.functions

commands = funcs.commands

in_commands = False

jarvis = jarvis.main()
while True:
    for command_data, args in [[jarvis.read_mail, []], [jarvis.speach_get, [15]]]
        data = command_data(*args).lower()
        print(jarvis.search_algorithm(commands, functions, data, "jarvis"))