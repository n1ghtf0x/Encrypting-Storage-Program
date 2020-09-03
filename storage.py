import os
import pickle
import time
import random
from cryptography.fernet import Fernet

def write_key():
    key = Fernet.generate_key()
    with open((os.path.dirname(os.path.abspath(__file__)) + "/valut/key.key"), "wb") as key_file:
        key_file.write(key)

def load_key():
    return open((os.path.dirname(os.path.abspath(__file__)) + "/valut/key.key"), "rb").read()

def encrypt(filename, key):
    f = Fernet(key)


    with open((os.path.dirname(os.path.abspath(__file__)) + "/valut/" + filename), "rb") as file:
        file_data = file.read()

    encrypted_data = f.encrypt(file_data)


    with open((os.path.dirname(os.path.abspath(__file__)) + "/valut/" + filename), "wb") as file:
        file.write(encrypted_data)


def decrypt(filename, key):
    f = Fernet(key)
    with open((os.path.dirname(os.path.abspath(__file__)) + "/valut/" + filename), "rb") as file:
        encrypted_data = file.read()
    decrypted_data = f.decrypt(encrypted_data)
    with open((os.path.dirname(os.path.abspath(__file__)) + "/valut/" + filename), "wb") as file:
        file.write(decrypted_data)

def passedpass():
        x = input("[*] Enter command: ")
        if str(x.lower()) == "-o":
            openstorage()
        elif str(x.lower()) == "-m":
            movestorage()
        elif str(x.lower()) == "-e":
            quit()
        elif str(x.lower()) == "-h":
            writehelp()
        elif str(x.lower()) == "-d":
            delete()
        elif str(x.lower()) == "-u":
            unpack()
        else:
            print("[*] Error. Type there is no command called", x, ".")
            passedpass()

def unpack():
        co = input("[*] Enter name of file you want to get back from storage: ")
        spr = input("[*] Enter your current password to unpack this file: ")
        with open("password.txt", "rb") as plik6:
            sprawdzenie = pickle.load(plik6)

        p = bytearray.fromhex(sprawdzenie).decode()
        if spr == p:
            x = random.randint(1, 99999999999999)
            path = os.path.join(os.path.expandvars("%userprofile%"), "Desktop", "storage", str(x))
            os.mkdir(path)
            g = str(os.path.dirname(os.path.abspath(__file__))) + "/valut/" + str(co)
            y = str(os.path.dirname(os.path.abspath(__file__))) + "/" + str(x) + "/" + co
            decrypt(co, load_key())
            os.rename(g, y)
            print("[*] File moved successfully.")
            passedpass()
        else:
            print("[*] Wrong password.")
            passedpass()


def writehelp():
    print("--------------------------------------")
    print("[*] Type -o to see storage content.")
    print("[*] Type -m to move file to storage.")
    print("[*] Type -e to exit storage.")
    print("[*] Type -d to see delete your password and create new password.")
    print("[*] Type -u to unpack file from storage.")
    print("--------------------------------------")
    print(" ")
    passedpass()

def new():
    haslo = input("[*] Type new password: ")
    maslo = input("[*] Type new password again: ")
    if str(haslo) == str(maslo):
        h = ""
        for i in haslo:
            x = hex(ord(i))
            y = x.replace("0x", "")
            h = str(h) + str(y)
            
        with open("password.txt", "wb") as plik1:
            pickle.dump(h, plik1)

        with open("password.txt", "rb") as plik2:
            odczyt = pickle.load(plik2)

        u = bytearray.fromhex(odczyt).decode()

        print("[*] Your new password is", u)
        print("--------------------------------------")
        print("[*] Welcome to storage.")
        print("[*] Type -o to see storage content.")
        print("[*] Type -m to move file to storage.")
        print("[*] Type -e to exit storage.")
        print("[*] Type -h to see instructions.")
        print("[*] Type -d to see delete your password and create new password.")
        print("[*] Type -u to unpack file from storage.")
        print("--------------------------------------")
        print(" ")
        passedpass()
    else:
        print("[*] Error. You need to type your new password twice.")
        new()

def delete():
    try:
        os.remove("password.txt")
        print("[*] Password deleted")
        with open("password.txt", "w") as plik5:
            pass
        new()
    except:
        print("[*] Error. Password can't be deleted.")
        passedpass()

def openstorage():
    t = os.path.dirname(os.path.abspath(__file__))
    print(os.listdir(str(t) + "/valut"))
    passedpass()

def movestorage():
    print("[*] Warning! Please replace \ char with / char.")
    a = input("[*] Enter location of your file: ")
    b = input("[*] Enter full name of your file: ")
    c = a + "/" + b
    o = str(os.path.dirname(os.path.abspath(__file__))) + "/valut/" + b
    try:
        os.rename(c, o)
        encrypt(b, load_key())
        print("[*] File moved successfully.")
    except:
        print("[*] Error. File wasn't moved.")
    passedpass()

key = "uhetruydtiw3y8723842yc@!VV$%B#^$%b65f7498328924386xc3dsugf73fewydf3c$xeWr3Crxwedsrfc$rxweCwecxrcert%BY65nb6Ui8(mNYGvc3w4xz265BB%Ve4$NBe6#es4vcwasbn4#shH$%3cwe4543454534g543#b453"
file = open("password.txt", "r")
if os.stat("password.txt").st_size == 0:
    print("[*] Error file password.txt is empty!")
    time.sleep(5)
    file.close()
elif(file.read() == key):
    file.close()
    write_key()
    new()
else:
    file.close()
    check = input("[*] Type your password: ")
    with open("password.txt", "rb") as plik4:
        hmmm = pickle.load(plik4)
    j = bytearray.fromhex(hmmm).decode()
    if check == j:
        print("--------------------------------------")
        print("[*] Welcome to storage.")
        print("[*] Type -o to see storage content.")
        print("[*] Type -m to move file to storage.")
        print("[*] Type -e to exit storage.")
        print("[*] Type -h to see instructions.")
        print("[*] Type -d to see delete your password and create new password.")
        print("[*] Type -u to unpack file from storage.")
        print("--------------------------------------")
        print(" ")
        passedpass()
    else:
        print("[*] Wrong password.")
        time.sleep(5)
