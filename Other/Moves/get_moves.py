def get_text(name):
    with open(name, "r") as file:
        text = file.read()
    return text


def make_move_list():
    moves = {}

    # Get Moves
    text = get_text("moves.txt")
    lines = text.split("\n")

    # #, Name, Type, Category, Contest, Power, Accuracy, Generation, Battle Description, 
    # Appeal, Jam, Contest Description
    for line in lines[1:]:
        desc = line.split("\t")
        num = desc[0].strip()
        name = desc[1].strip()
        type = desc[2].strip()
        cat = desc[3].strip()
        cont = desc[4].strip()
        pow = desc[5].strip()
        acc = desc[6].strip()
        gen = desc[7].strip()
        
        moves[name] = {
            "number": num,
            "type": type,
            "category": cat,
            "power": pow,
            "accuracy": acc,
            "generation": gen
        }
        
    # Add Serebii
    text = get_text("serebii_moves.txt")
    lines = text.split("\n")

    # Name, Type, Cat., PP, Att., Acc., Effect
    for line in lines[1:]:
        move = line.split("\t")
        move = [ i.strip() for i in move ]

        name = move[0]
        if name == "Double-edge":
            name = "Double-Edge"
        elif name == "Doubleslap":
            name = "Double Slap"
        elif name == "Thunderpunch":
            name = "Thunder Punch"
        elif name == "Twineedle":
            name = "Twin Needle"
        elif name == "Vicegrip":
            name = "Vice Grip"
        elif name == "Mud-slap":
            name = "Mud-Slap"
        elif name == "Roar Of Time":
            name = "Roar of Time"
        elif name == "Sonicboom":
            name = "SonicBoom"
        elif name == "Conversion 2":
            name = "Conversion2"
        elif name == "Lock-on":
            name = "Lock-On"
        elif name == "Poisonpowder":
            name = "Poison Powder"
        elif name == "Sand-attack":
            name = "Sand-Attack"
        elif name == "Will-o-wisp":
            name = "Will-O-Wisp"

        moves[name]["PP"] = move[3]
        moves[name]["Effect"] = move[6].replace("Ã©", "é")

    # Save
    with open("just_moves.py", "w+", encoding="utf-8") as file:
        file.write("move_list = " + str(moves))
    return


if __name__ == "__main__":
    make_move_list()
