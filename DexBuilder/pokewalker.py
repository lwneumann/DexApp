from config import WALKER_NAME


def get_text():
    with open(WALKER_NAME, "r", encoding="utf-8") as file:
        text = file.read()
    return text


def get_walker_info():
    """
    Header:
    # 	  	Pokémon 	Gender 	Group 	Area Found 	Unlock Method 	Level 	Number of steps 	Rarity 	Item Held
    """
    text = get_text()
    text = text.split('\n')[1:]
    walkermon = {}
    for l in text:
        line = l.split('\t')
        num = int(line[0].strip())
        area = line[5].strip()
        item = line[10].strip()
        if "None" not in item:
            item = item[4:-11]
        else: item = None
        if num not in walkermon.keys():
            walkermon[num] = {"area": [area]}
            if item is not None:
                walkermon[num]["item"] = [item]
        else:
            walkermon[num]["area"].append(area)
            if item is not None:
                if "item" in walkermon[num].keys():
                    walkermon[num]["item"].append(item)
                else:
                    walkermon[num]["item"] = [item]
    return walkermon


if __name__ == "__main__":
    w = get_walker_info()
    for k in w.keys():
        print(k, w[k])
