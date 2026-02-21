letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!?@#$€£%^&*().,':"

saveFileLocation = ""

def getName(letter):
        if letter == "?":
            return "_Qm"
        elif letter == "*":
            return "_As"
        elif letter == "!":
            return "_Ex"
        elif letter == "@":
            return "_At"
        elif letter == "#":
            return "_Ha"
        elif letter == "$":
            return "_Do"
        elif letter == "%":
            return "_Pe"
        elif letter == "^":
            return "_Ca"
        elif letter == "&":
            return "_An"
        elif letter == "(":
            return "_Op"
        elif letter == ")":
            return "_Cl"
        elif letter == ".":
            return "_Fs"
        elif letter == ",":
            return "_Co"
        elif letter == "€":
            return "_Eu"
        elif letter == "£":
            return "_Po"
        elif letter == "'":
            return "_Ap"
        elif letter == ":":
            return "_Cn"

        
        return letter


import json

#

#make new json
with open(saveFileLocation + "/mods/Yernemm.Labels/Server/Item/Groups/Labels/Yernemm_Labels_Text_Group.json", "w") as f:
    json.dump({
        "Blocks": [f"Yernemm_Labels_LabelText{getName(letter)}" for letter in letters]
    }, f, indent=2)