import sys
element_list_file = "Splurthian Element List.txt"

try:
    with open(element_list_file) as file:
        pass
except IOError:
    print("File does not exist or can't be opened")
    sys.exit()

def find_symbol(element):
    valid_symbol = False
    first_sym_pos = 1
    sec_sym_pos = 2
    while not valid_symbol:
        if first_sym_pos > 1:
            first_sym = element[first_sym_pos-1:first_sym_pos]
        else:
            first_sym = element[:first_sym_pos]
        sec_sym = element[sec_sym_pos-1:sec_sym_pos]
        symbol = first_sym.upper() + sec_sym
        #print(element + ": Trying: " + symbol)
        if not symbol in symbols:
            valid_symbol = True
        else:
            if first_sym_pos == len(element):
                print("No symbol for " + element)
                return
            if sec_sym_pos == len(element):
                first_sym_pos += 1
                sec_sym_pos = first_sym_pos + 1
                #print("** Out of combinations: " + element)
            else:
                sec_sym_pos += 1          
    #print(element)
    #print("*1st: " + first_sym.upper() + " | 2nd: " + sec_sym)
    #print("++ Adding " + symbol + " " + element + '\n')
    if element == "Bartium":
        print(element + " " + symbol)
    symbols.append(symbol)


symbols = []

elements = open(element_list_file).read().split()
for element in elements:
    find_symbol(element)
