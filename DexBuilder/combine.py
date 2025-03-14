import json, importlib
from config import *
import pokewalker


def get_text(name):
    with open(name, "r") as file:
        text = file.read()
    return text


def store_data(p_data, text_file=True, py_file=True):
    # Readable txt
    if text_file:
        with open(f"{DEX_NAME}.txt", 'w+', encoding="utf-8") as file:
            file.write(json.dumps(p_data, indent=4))
    if py_file:
        with open(f"{DEX_NAME}.py", 'w+', encoding="utf-8") as file:
            file.write("pokedex="+str(p_data))
    return


def get_dex():
    module = importlib.import_module(FIRST_DEX)
    dex = getattr(module, "full_dex")
    return dex


def add_csv():
    csv_text = get_text(f"{CSV_NAME}")
    csv_text = csv_text.split('\n')[1:]

    fulldex = get_dex()
    #,Name,Type 1,Type 2,Total,HP,Attack,Defense,Sp. Atk,Sp. Def,Speed,Generation,Legendary
    for p in csv_text:
        number, name, t1, t2, total, HP , attack, defense, spatk, spdef, speed, gen , legendary = p.split(',')
        number = int(number)
        gen = int(gen)
        if gen <= 4:
            break
        elif "Mega" not in name or name == "Meganium":
            if t2 == "":
                fulldex[number]["types"] = [t1]
            else:
                fulldex[number]["types"] = [t1, t2]
            fulldex[number]["legendary"] = legendary
            fulldex[number]["generation"] = gen
            if "stats" not in fulldex[number].keys():
                fulldex[number]["stats"] = [HP]

    return fulldex


def add_pokewalker(dex):
    walker = pokewalker.get_walker_info()
    for num in walker.keys():
        dex[num]["pokewalker"] = walker[num]
    return dex


def fix_moves(dex):
    # For all mon
    for mon in dex:
        # For all move pools
        move_pool = ["learnset"]
        if "egg_moves" in dex[mon]:
            move_pool.append("egg_moves")
        if "tutor_moves" in dex[mon]:
            move_pool.append("tutor_moves")

        for m in move_pool:
            for i, move_l in enumerate(dex[mon][m]):
                if m == "learnset":
                    for i, move in enumerate(dex[mon][m][move_l]):
                        name = dex[mon][m][move_l][i]
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
                        dex[mon][m][move_l][i] = name
                else:
                    name = dex[mon][m][i]
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
                    dex[mon][m][i] = name
    return dex


def add_all():
    csvdex = add_csv()
    fulldex = add_pokewalker(csvdex)

    print()
    print('Fixing Move Names')
    fulldex = fix_moves(fulldex)

    store_data(fulldex)
    print()
    print('Attached information from', {CSV_NAME}, {WALKER_NAME})
    print()
    return

if __name__ == "__main__":
    add_all()
