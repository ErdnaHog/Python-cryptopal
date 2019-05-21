# hex to base64
# 1st step: decode hex string to get value of the string
# 2nd step: encode value into base 64 and return it

import base64

def hex_to_b64(x):
    #converting a string to unicode byte
    plain_text = bytes.fromhex(x)
    #printing plain text
    print("Plain text is: %s" %plain_text.decode())
    #using of base64 library, .decode('utf-8') helps convert the byte to a string
    new_encode_text = base64.b64encode(plain_text).decode()
    return new_encode_text

y = input("Hex string: ")
print(hex_to_b64(y))
