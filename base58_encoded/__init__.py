# Tools for encoding and decoding numbers with base58

alphabet = '123456789abcdefghijkmnopqrstuvwxyzABCDEFGHJKLMNPQRSTUVWXYZ'
base_count = len(alphabet)

####################################################

def encode(num):
    
    encoded = ''

    while num >= base_count:
        div = num / base_count
        mod = (num - (base_count * int(div)))
        encoded = alphabet[mod] + encoded
        num = int(div)

    if num:
        encoded = alphabet[num] + encoded

    return encoded

####################################################

def decode(s):
    
    decoded = 0
    multi = 1
    s = s[::-1]

    for char in s:
        decoded += multi * alphabet.index(char)
        multi = multi * base_count
    
    return decoded

