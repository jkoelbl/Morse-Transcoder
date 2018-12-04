from auxil import get_encoding
import sys

def is_valid_message(raw, codes):
    for i in range(len(raw)):
        if raw[i] not in codes:
            return False
    return True

def get_message(raw, codes):
    msg = ''
    for i in range(len(raw)):
        msg += codes[raw[i]]
    return msg

if __name__ == '__main__':
    raw = ''
    if len(sys.argv) > 1:
        raw = sys.argv[1].lower()
    else:
        raw = input('Enter Message: ')
    codes = get_encoding()
    if is_valid_message(raw, codes):
        msg = get_message(raw, codes)
        print(msg)
    else:
        print('not a valid message')
