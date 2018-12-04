import csv

def get_encoding():
    codes, signals = {}, {}
    with open('signals.txt', newline='') as sigs:
        reader = csv.reader(sigs, delimiter=',', quotechar='\"')
        for row in reader:
            signals[row[0]] = row[1]
    with open('codes.txt', newline='') as cds:
        reader = csv.reader(cds, delimiter=',', quotechar='\"')
        for row in reader:
            codes[row[0]] = row[1]
    for key in codes.keys():
        temp = ''
        for i in range(len(codes[key])):
            temp += signals[codes[key][i]]
        codes[key] = temp
    return codes
