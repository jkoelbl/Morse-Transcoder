from auxil import get_decoding
import sys

def is_valid_message(raw, codes):
    return True

def get_message(raw, codes):
    return raw

def decode():
    raw = ''
    if len(sys.argv) > 1:   raw = sys.argv[1].lower()
    else:                   raw = input('Enter Message: ')
    codes = get_decoding()
    if is_valid_message(raw, codes):    msg = get_message(raw, codes)
    else:                               msg = 'not a valid message'
    return msg

if __name__ == '__main__':
    print(decode())
