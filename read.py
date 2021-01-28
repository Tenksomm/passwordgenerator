import time
file_ = str()


f = open("generatedpasswords.txt", "r")
file_ = str(f.read())
output = str()

print("Datei wird gelesen")
for x in file_:
    if x == "das":
        print("c")    
f.close()