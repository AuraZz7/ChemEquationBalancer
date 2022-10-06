# equation = "NaCl2 + HO2 -> H2Cl + NaO2"
equation = "C3H8 + O2 -> H2O + CO2"
# balance " C3H8 +5O2 -> 4H2O + 3CO2"
# remove all whitespace
equation = equation.replace(" ", "")
# split into an array of length 2, with reactants and products
equation = equation.split("->")

# split equation into a list of individual molecules
compounds = []
for product in equation:
    compounds.append(product.rsplit("+"))


def compound_parser(compound: str):
    """
    :param compound
    :return dict of elements
    """
    # check for the position of every capital letter (or start of a new element)
    idxs = [i for i, char in enumerate(compound) if char.isupper()]
    # use the previous list to create a list of element strings and their respective numbers (if existing)
    elements = [compound[item:idxs[i+1]] if i < len(idxs) - 1 else compound[item:] for i, item in enumerate(idxs)]

    # create a dictionary where key = element and value = number of that element
    new_elements = {}
    for element in elements:
        for i, char in enumerate(element):
            if char.isdigit():
                new_elements[element[:i]] = int(element[i:])
                break
        else:
            new_elements[element] = 1

    return new_elements


reactants, products = compounds[0], compounds[1]

for i in range(2):
    temp_arr = []
    for compound in (reactants if i == 0 else products):
        parsed_compound = compound_parser(compound)
        for key, val in parsed_compound.items():
            temp_arr.append((key, val))
    if i == 0:
        elements_r = temp_arr
    else:
        elements_p = temp_arr

print(elements_p)

