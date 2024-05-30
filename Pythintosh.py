import time
import sys
import colorama
from colorama import Fore 

colorama.init()
print("Pythintosh created by skull._.python")
time.sleep(0.5)
print(Fore.GREEN + "Enter any key to boot up")
a = input("")
time.sleep(0.25)
un = input("Enter username: ")
while un != "admin":
    print("Incorrect username, try again")
    un = input("Enter username: ")
p = input("Enter password: ")
while p != "123":
    print("Incorrect password, try again")
    p = input("Enter password: ")
time.sleep(0.75)
print("Pythintosh booting up")
time.sleep(0.5)
print("Pythintosh has booted up successfully with no errors")
time.sleep(0.25)
print("Welcome to Pythintosh, " + un)
time.sleep(0.25)
print("For a list of commands, enter: /list of commands. For help enter the command, /info user")
while True: 
    i = input("")
    if i == "/list of commands":
        print("Enter one of the following commands: /sys specs, /shut down sys, /run calculator, /info user")
    elif i == "/shut down sys":
        time.sleep(2)
        print("Turning off background processes")
        time.sleep(0.75)
        print("Shutting down")
        sys.exit()
    elif i == "/info user":
        print("What would you like help with?")
        h = input(" ")
        if h == "calculator":
            print("You can use commands like: add, sub, mul, div")
        else:
           print("invalid command")
    elif i == "/sys specs":
        time.sleep(0.25)
        print("Storage: 2098 bytes")
        time.sleep(0.5)
        print("OS: Pythintosh 4.0 ")
        time.sleep(0.25)
        print("Made with Visual Studio Code")
    elif i == "/run calculator":
        print("Enter which type of calculation you have to do")
        tc = str(input(" "))
        if tc == "add":
         print("Enter first number:")
         fn = float(input())
         print("Enter second number:")
         sn = float(input())
         print(fn + sn)
        elif tc == "sub":
         print("Enter minuend:")
         fn = float(input())
         print("Enter subtrahend:")
         sn = float(input())
         print(fn - sn)
        elif tc == "mul":
         print("Enter first number:")
         fn = float(input())
         print("Enter second number:")
         sn = float(input())
         print(fn * sn)
        elif tc == "div":
         print("Enter first number:")
         fn = float(input())
         print("Enter second number:")
         sn = float(input())
         print(fn/sn)
        else: 
         print("invalid")
    else:
     print("wrong command")
     i = input("")
