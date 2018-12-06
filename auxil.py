import csv

CODES = 'codes.csv'
SIGNALS = 'signals.csv'

def load_signals():
    signals = {}
    with open(SIGNALS, newline='') as sigs:
        reader = csv.reader(sigs, delimiter=',', quotechar='\"')
        for row in reader:
            signals[row[0]] = row[1]
    return signals

def get_full_signal(code, signals):
    temp = ''
    for i in range(len(code)):
        temp += signals[code[i]]
    return temp

def get_encoding():
    codes = {}
    signals = load_signals()
    with open(CODES, newline='') as cds:
        reader = csv.reader(cds, delimiter=',', quotechar='\"')
        for row in reader:
            codes[row[0]] = get_full_signal(row[1], signals)
    return codes

def get_decoding():
    codes = {}
    signals = load_signals()
    with open(CODES, newline='') as cds:
        reader = csv.reader(cds, delimiter=',', quotechar='\"')
        for row in reader:
            codes[get_full_signal(row[1], signals)] = row[0]
    return codes