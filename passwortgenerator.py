import random
import string
import time

letters = string.ascii_letters + string.punctuation + string.digits
counter = 0
topic = input("What is the password for?: ")
user = input("What is the user name?: ")
x = int(input("How long is the password?: "))
f = open("generatedpasswords.txt", "a")
print("Vorgang wird bearbeitet")
time.sleep(.25)
hello = str()
message = "\nThe password {} with the username {} is: {}"

if x <= 8:
    print("\nIf you want to have a safe password, it is recommended to have one with a length over 8\n\n")
    e_passwortlänge = input("möchtest du ein neues Passwortlänge eingeben?(y/n/e)")
    if e_passwortlänge == "y":
        x = int(input("How long would you like your password?\n"))
        if x <= 8:
            print("trolling me?")
            time.sleep(.5)
            print("Exiting")
        else:
            print("generating password...")
            time.sleep(.25)
            while counter < x:
                hello += str(random.choice(letters))
                counter + 1
            print(("password: {}").join(hello))
            message = message.format(topic, user,  hello)
            f.write(message)
    elif e_passwortlänge == "n":
        print("generating password...")
        time.sleep(.25)
        while counter < x:
            hello += str(random.choice(letters))
            counter + 1
        print("password: "+hello)
        message = message.format(topic, user, hello)
        f.write(message)
    elif e_passwortlänge == "e":
        print("Exit!")
    else: print("bitte 'y' oder 'n' ein!")
else:
    print("generating password...")
    time.sleep(.25)
    while counter < x:
        hello += str(random.choice(letters))
        counter + 1
    print("password: "+hello)
    message = message.format(topic, user, hello)
    f.write(message)
f.close()
