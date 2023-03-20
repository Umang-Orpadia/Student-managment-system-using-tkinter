try:
    f = open("demofile.txt", "r")
    print(f)
except:
    print("error 1")
try:
    f = open("demofile.txt", "a")
    print(f)
except:
    print("error 2")
try:
    f = open("demofile.txt", "w")
    print(f)
except:
    print("error")
try:
    f = open("demofile.txt", "x")
    print(f)
except:
    print("file already exist")
