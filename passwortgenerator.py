import random
import string
import time

letters = string.ascii_letters + string.punctuation + string.digits
counter = 0
x = int(input("Wie lang soll das Passwort sein?\n"))
f = open("generatedpasswords.txt", "a")
print("Vorgang wird bearbeitet")
time.sleep(2)
hello = str()
if x <= 5:
    print("\nWenn du ein sicheres Passwort möchtest, empfehle ich dir ein Passwort, welches Länger ist als 5\n\n")
    e_passwortlänge = input("möchtest du ein neues Passwortlänge eingeben?(y/n/e)")
    if e_passwortlänge == "y":
        x = int(input("Wie lang soll das Passwort sein?\n"))
        if x <= 5:
            print("Warum hast du noch mal eine Zahl unter 5 eingegeben??")
            time.sleep(.5)
            print("Der Script wird geschlossen")
        else:
            print("Zahl wird ertsellt")
            time.sleep(1)
            while counter < x:
                hello += str(random.choice(letters))
                counter = counter + 1
            print("Hier ist dein Passwort: " + hello)
            f.write("\n"+hello)
    elif e_passwortlänge == "n":
        print("Zahl wird erstellt")
        time.sleep(1)
        while counter < x:
            hello += str(random.choice(letters))
            counter = counter + 1
        print("Hier ist dein Passwort: "+hello)
        f.write("\n"+hello)
    elif e_passwortlänge == "e":
        print("Exit!")
    else: print("bitte 'y' oder 'n' ein!")
    
else:
    print("Zahl wird erstellt")
    time.sleep(1)
    while counter < x:
        hello += str(random.choice(letters))
        counter = counter + 1
    print("Hier ist dein Passwort: "+hello)
    f.write("\n"+hello)
f.close()






