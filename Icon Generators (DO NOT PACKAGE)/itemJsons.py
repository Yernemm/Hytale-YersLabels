letters = "CDEFGHIJKLMNOPQRSTUVWXYZ0123456789!?@#$€£%^&*().,':"

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


with open(saveFileLocation + "/mods/Yernemm.Labels/Server/Item/Items/YerLabels/Regular/Text/Yernemm_Labels_LabelTextB.json", "r") as f:
    data = json.load(f)
    print(data["BlockType"]["CustomModelTexture"][0]["Texture"])

    for letter in letters:
        if letter == "A":
            continue
        if letter == "B":
            continue
        data["BlockType"]["CustomModelTexture"][0]["Texture"] = f"Items/YerLabels/Regular/LabelSignText{getName(letter)}.png"
        data["Icon"] = f"Icons/ItemsGenerated/Yernemm_Labels_LabelText{getName(letter)}.png"
        data["Recipe"]["BenchRequirement"][0]["Categories"] = ["Sign"]

        with open(saveFileLocation + f"/mods/Yernemm.Labels/Server/Item/Items/YerLabels/Regular/Text/Yernemm_Labels_LabelText{getName(letter)}.json", "w") as f:
            json.dump(data, f, indent=2)