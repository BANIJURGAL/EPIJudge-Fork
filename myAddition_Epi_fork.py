from unicodedata import name


def splicer(string):
    if len(string)%2 == 0:
        return "Even"
    else:
        return string[0]

name = ["Amandine", "Aurore", "Eirlef", "Bertrand"]

newPrint = list(map(splicer,name)) 
print(newPrint)