import os
import time
money = 50

def save():
    list = [
        str(money)
    ]
    f = open("load1.txt", "w")
    for item in list:
        f.write(item + "\n")
    f.close

while True:
    ask = input("do you want to save your money or load your money or do  you want to add 20 to your money?:  ")
    if ask == "load":
        try:
            f = open("load1.txt", "r")
            list_loaded =f.readlines()
            money = list_loaded[0][:-1]
            print(money)
        except OSError:
            print("no file found! :(")
    elif ask == "save":
        try:
            save()
            print("money has ben saved")
        except OSError:
            print("no file found! :(")
    elif ask == "add":
        money = int(money) + 20
        print(money)
    time.sleep(2)
    os.system("cls")