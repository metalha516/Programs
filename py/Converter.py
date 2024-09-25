import datetime
time = datetime.datetime.now()
time = str(time)
MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..', '1': '.----', '2': '..---', '3': '...--',
    '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..',
    '9': '----.', '0': '-----', ' ': ' '
}
def create():
   
    site = input("Entry_0 :")
    morse_site = "".join(MORSE_CODE_DICT[c] for c in site.upper())
    Email = input("Entry_1 : ")
    password = input("Entry_2 : ")
    inten, exten = "_%^$", "/*-+"
    created_pass = inten+""+password+""+exten
    password_bin = " ".join(format(ord(i), "b") for i in created_pass)
    email_bin = " ".join(format(ord(j), "b") for j in Email)
    file = open("C:\\Users\\talha\OneDrive\\Desktop\\Essential\\Coding Projects\\txt\\DB.txt", "a")
    file.write(time +"\n"+morse_site+"\n"+email_bin + "\n" + password_bin)
    file.close()
    file = open("C:\\Users\\talha\\OneDrive\\Desktop\\Essential\\Coding Projects\\txt\\main_db.txt", "w")
    file.write(site+"\n"+email_bin + "\n" + password_bin+"\n")
    file.close()


def extract():
    file = open("C:\\Users\\talha\\OneDrive\\Desktop\\Essential\\Coding Projects\\txt\\main_db.txt", "r")
    site,mail_bin, pass_bin = file.read().splitlines()
    mail = "".join(chr(int(i, 2))for i in mail_bin.split(" "))
    password = "".join(chr(int(j, 2))for j in pass_bin.split(" "))
    print(site)
    print(mail)
   
    extracted = password.replace("_%^$", "")
    extracted = extracted.replace("/*-+", "")
    print(extracted)

while True:
    x = input("Action :")
    if 'cre' in x:
        create()
       
    if 'ext' in x:
        extract()
       
    if 'bre' in x:
        break

    