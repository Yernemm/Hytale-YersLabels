from PIL import Image, ImageDraw, ImageFont

fontDir = ""

letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!?@#$€£%^&*().,':"


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

for letter in letters:
    labelTexture = Image.open("LabelSignEmpty.png")

    labelDrawable = ImageDraw.Draw(labelTexture)

    font = ImageFont.truetype(fontDir, 28)

    txt = Image.new("RGBA", labelTexture.size, (255, 255, 255, 0))

    txtDraw = ImageDraw.Draw(txt)

    txtDraw.text((13, 25), letter, font=font, fill=(32, 17, 8, 236), anchor="ms")

    labelTexture = Image.alpha_composite(labelTexture, txt)

    labelTexture.save(f"output/LabelSignText{getName(letter)}.png")