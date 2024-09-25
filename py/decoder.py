MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..', '1': '.----', '2': '..---', '3': '...--',
    '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..',
    '9': '----.', '0': '-----', ' ': ' '
}
def bin2text(message):
    input = message
    character = "".join(chr(int(c ,2)) for c in input.split(" "))
    print(character)

def morsh2text(message):
    msg = message
    reverse_dict = {v:k for k, v in MORSE_CODE_DICT.items()}
    reverse_msg = "".join(reverse_dict[c] for c in msg.split())
    print(reverse_msg)
while True:    
        msg = input("Enter Code to decode : ")
        if "0" in msg and "1" in msg:
            bin2text(msg)
        if "." in msg and "-" in msg:
            morsh2text(msg)
