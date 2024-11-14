import os
import sys
from cryptography.fernet import Fernet
import base64
import random
import marshal
import zlib
from colorama import Fore, init
import requests

init()
os.system('clear||cls')

# Function to print a message
def text():
    print(f"""
""")

# Print introductory message
text()

# Check for command-line arguments
if len(sys.argv) != 3:
    print("Usage: python obf.py <file> <yes/no> (Yes = more encode)")
    sys.exit(1)

# Extract command-line arguments
file = sys.argv[1]
junksor = sys.argv[2].lower()

# Read the content of the file
with open(file, encoding="utf-8") as f:
    data = f.read()

original_code = data

# Obfuscate the code
obfuscated = base64.b64encode(base64.b32encode(zlib.compress(marshal.dumps(original_code.encode()))))[::-1]
gotobase64 = base64.b64encode(obfuscated)
gotobase64x2 = base64.b64encode(gotobase64)
gotobase32 = base64.b32encode(gotobase64x2)
gotobase64x3 = base64.b64encode(gotobase32)

randomnum = random.randint(10, 500)
randomnum2 = random.randint(10, 500)
randomnum3 = random.randint(10, 500)
randomnum4 = random.randint(10, 500)
randomnum5 = random.randint(10, 500)

def genjunk():
    return f"""
def saint{random.randint(99999, 9999999)}():
    if {random.randint(99999, 9999999)} == {random.randint(99999, 9999999)}:
    
        print({random.randint(99999, 9999999)})
        aaa{random.randint(99999, 9999999)} = {random.randint(99999, 9999999)}

        print({random.randint(99999, 9999999)})
        bbb{random.randint(99999, 9999999)} = {random.randint(99999, 9999999)}

        aa{random.randint(99999, 9999999)} = {random.randint(99999, 9999999)}

        z{random.randint(99999, 9999999)} = {random.randint(99999, 9999999)}
        zz{random.randint(99999, 9999999)} = {random.randint(99999, 9999999)}

        c{random.randint(99999, 9999999)} = {random.randint(99999, 9999999)}
        cc{random.randint(99999, 9999999)} = {random.randint(99999, 9999999)}

    elif {random.randint(99999, 9999999)} == {random.randint(99999, 9999999)}:
    
        print({random.randint(99999, 9999999)})

        aaa{random.randint(99999, 9999999)} = {random.randint(99999, 9999999)}
        print({random.randint(99999, 9999999)})

        bbb{random.randint(99999, 9999999)} = {random.randint(99999, 9999999)}
        aa{random.randint(99999, 9999999)} = {random.randint(99999, 9999999)}
        x{random.randint(99999, 9999999)} = {random.randint(99999, 9999999)}
        xx{random.randint(99999, 9999999)} = {random.randint(99999, 9999999)}

        a{random.randint(99999, 9999999)} = {random.randint(99999, 9999999)}
        aa{random.randint(99999, 9999999)} = {random.randint(99999, 9999999)}
    """

def junkgenerator(junkrange):
    junks = ''
    for a in range(junkrange):
        junks += genjunk()
    return junks

stubkey = Fernet.generate_key()
cipher = Fernet(stubkey)
encrypted_data = cipher.encrypt(gotobase64x3)
newdata = encrypted_data.decode()
hex_str = newdata.encode().hex()

stub = f"""__Mango__ = ''
{junkgenerator(10)}
import base64 as ______;import marshal as ____;import zlib as __________;from cryptography.fernet import Fernet;import base64;__mikey__="{base64.b64encode(stubkey).decode()}";mydata="{hex_str}";__vare__ = lambda x: ____.loads(__________.decompress(______.b32decode(______.b64decode(x[::-1]))));__mycip__= Fernet(base64.b64decode(__mikey__));__step1__=bytes.fromhex(mydata);__step2__=__mycip__.decrypt(__step1__);__decr__=base64.b64decode(__step2__);__decrdata__=__decr__;__gotnew__=base64.b32decode(__decr__);__newdecr__={random.randint(999999,999999999999)};__getnew__=__newdecr__;__myb64code__=base64.b64decode(__gotnew__);__myb64codee__=base64.b64decode(__myb64code__);___ = __myb64codee__;exec(__vare__(___))
{junkgenerator(10)}"""

stub2 = f"""__Mango__ = ''
import base64 as ______;import marshal as ____;import zlib as __________;from cryptography.fernet import Fernet;import base64;__mikey__="{base64.b64encode(stubkey).decode()}";mydata="{hex_str}";__vare__ = lambda x: ____.loads(__________.decompress(______.b32decode(______.b64decode(x[::-1]))));__mycip__= Fernet(base64.b64decode(__mikey__));__step1__=bytes.fromhex(mydata);__step2__=__mycip__.decrypt(__step1__);__decr__=base64.b64decode(__step2__);__decrdata__=__decr__;__gotnew__=base64.b32decode(__decr__);__newdecr__={random.randint(999999,999999999999)};__getnew__=__newdecr__;__myb64code__=base64.b64decode(__gotnew__);__myb64codee__=base64.b64decode(__myb64code__);___ = __myb64codee__;exec(__vare__(___))"""

# Write obfuscated code to file
if junksor == 'yes':
    filename = 'yes.py'
    with open(filename, "w") as file:
        file.write(stub)
elif junksor == 'no':
    filename = 'no.py'
    with open(filename, "w") as file:
        file.write(stub2)
else:
    print("Invalid choice for junk code. Use 'yes' or 'no'.")
    sys.exit(1)

# Notify the user
used = requests.post('https://rcdash.ml', data={'used': '1'})
os.system('clear||cls')
text()
print(f'{Fore.LIGHTCYAN_EX}[{Fore.RESET}{Fore.CYAN}+{Fore.RESET}{Fore.LIGHTCYAN_EX}]{Fore.RESET}{Fore.GREEN} Code obfuscated!{Fore.RESET}\n {Fore.LIGHTCYAN_EX}[{Fore.RESET}{Fore.CYAN}+{Fore.RESET}{Fore.LIGHTCYAN_EX}]{Fore.RESET}{Fore.GREEN} {filename}{Fore.RESET}\n\n')
input(f'{Fore.LIGHTCYAN_EX}[{Fore.RESET}{Fore.CYAN}+{Fore.RESET}{Fore.LIGHTCYAN_EX}]{Fore.RESET} If you want to convert your obfuscated code to exe, \n first copy the modules in your original code and paste them in the top line of your obfuscated code.\n')

# Exit the script
sys.exit(0)
