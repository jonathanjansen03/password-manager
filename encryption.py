import base64
import random
import string

CHARS = string.ascii_letters + string.digits
LENGTH = len(CHARS)

def shift(strs):
    key = random.randint(1, 99)
    shifted_string = ""

    for i in strs:
        idx = CHARS.find(i)
        shifted_string += CHARS[(idx + key) % LENGTH]

    if key < 10:
        shifted_string = str(key) + shifted_string + "0"
    else:
        shifted_string = str(key)[1] + shifted_string + str(key)[0]
    
    return shifted_string

def shift_back(strs):
    strs = str(strs)
    key = int(strs[-1] + strs[0])
    shifted_string = ""
    strs = strs[1:-1]

    for i in strs:
        idx = CHARS.find(i)
        shifted_string += CHARS[(idx - key) % LENGTH]

    return shifted_string

def encode_b64(strs):
    bytes = base64.b64encode(strs.encode("ascii"))

    return bytes.decode("ascii")

def decode_b64(strs):
    bytes = base64.b64decode(strs.encode("ascii"))

    return bytes.decode("ascii")

def convert_to_binary(strs):
    binary = ""

    for i in strs:
        binary += format(ord(i), "08b") + " "
    
    return binary[0:-1]

def convert_from_binary(strs):
    lst = strs.split()
    converted_string = ""

    for i in lst:
        char = chr(int(i, 2))
        converted_string += char
    
    return converted_string

def encrypt(strs):
    strs = shift(strs)
    strs = encode_b64(strs)
    strs = convert_to_binary(strs)

    return strs

def decrypt(strs):
    strs = convert_from_binary(strs)
    strs = decode_b64(strs)
    strs = shift_back(strs)

    return strs