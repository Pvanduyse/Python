import csv
import numpy

# Import values
ifile = open("../Modules/molecular_weights.csv","r")
csv_reader = csv.reader(ifile)
by_symbol = {}
by_name = {}
by_index = list()
for l in csv_reader:
    if(l[0] == "Symbol"):
        continue
    by_symbol[l[0]] = float(l[2])
    by_name[l[1]] = float(l[2])
    by_index.append(l[2])
by_atomic_number = numpy.array([0]+by_index)
del by_index
ifile.close()

def by_formula(FORMULA):
    RESULT = 0.0
    COUNT = 0
    ELEMENT = ""
    for CHAR in FORMULA:
        if(CHAR.isdigit()):
            COUNT = COUNT*10 + int(CHAR)
        elif(CHAR.isupper()):
            if(ELEMENT != ""):
                RESULT = RESULT + (COUNT if COUNT > 0 else 1) * by_symbol[ELEMENT]
            ELEMENT = CHAR
            COUNT = 0
        else:
            ELEMENT = ELEMENT + CHAR
    return RESULT + (COUNT if COUNT > 0 else 1) * by_symbol[ELEMENT]