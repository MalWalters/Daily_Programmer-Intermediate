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
        if not symbol in symbols:
            valid_symbol = True
        else:
            if sec_sym_pos == len(element):
                first_sym_pos += 1
                if first_sym_pos < len(element) - 1:
                    sec_sym_pos = first_sym_pos + 1
                else:
                    if not element in no_match:
                        no_match.append(element)
            else:
                sec_sym_pos += 1          
    if len(symbol) == 2:
        symbols.append(symbol)

symbols = []
no_match = []

elements = open(element_list_file).read().split()
for element in elements:
    find_symbol(element)

print("The first one with no working elemental symbol is: " + no_match[0])
