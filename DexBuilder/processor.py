import json
import re
from config import *


# Nasty Text Handling ---------
def get_evs(ev_yield):
    # Initialize EV list [HP, Attack, Defense, Sp. Attack, Sp. Defense, Speed]
    evs = [0, 0, 0, 0, 0, 0]
    
    # EV type to index mapping
    ev_mapping = {
        'HP': 0,
        'Attack': 1,
        'Defense': 2,
        'Sp. Attack': 3,
        'Special Attack': 3,  # For consistency
        'Sp. Defense': 4,
        'Special Defense': 4,  # For consistency
        'Speed': 5
    }
    
    # Split the string into parts to parse
    parts = ev_yield.split("Point(s)")
    
    for part in parts:
        if part.strip() == "":
            continue  # Skip any empty part
        
        # Extract number and type of EV
        for ev_type in ev_mapping:
            if ev_type in part:
                number = int(part.split()[0])  # Get the number from the part
                evs[ev_mapping[ev_type]] += number  # Update the EV list
                break
    return evs


def fix_location(text):
    separated_text = re.sub(r'(\d)([A-Z])', r'\1, \2', text)
    separated_text = re.sub(r'(?<=[a-z\)])(?=[A-Z])', ', ', separated_text)
    return separated_text


def extract_hgss_moves(text):
    # Find the HeartGold/SoulSilver section in the list
    hgss_start = re.search(r"HeartGold/SoulSilver Level Up", text)
    if not hgss_start:
        return "HeartGold/SoulSilver section not found."
    
    # Extract everything after "HeartGold/SoulSilver Level Up"
    text = text[hgss_start.end():].strip()

    # Regex pattern to match levels and move names
    pattern = r"(\d{1,3}|—)\s*([A-Za-z\s\-]+?)(?=\s*\d{1,3}|—|$)"
    
    # Find all matches for level and move name
    moves = re.findall(pattern, text)

    # Create a dictionary with level as the key and list of move names as the value
    moves_dict = {}
    for level, move in moves:
        # Clean the move name
        move_name = move.strip().replace("--", "").strip()
        
        # Replace '—' (dash) with 0 in levels
        if level == '—':
            level = '0'

        # Ensure level is an integer
        level = int(level)

        # Append move to the list of moves for that level
        if level not in moves_dict:
            moves_dict[level] = []
        moves_dict[level].append(move_name)
    return moves_dict


def extract_egg_moves(text):
    # Regex pattern to match move names and ignore '--', 'HGSS Only', and ' - '
    pattern = r"([A-Za-z\s\-]+?)(\d{1,3}|\?\?|--)\s*(\d{1,3}|--)\s*(\d{1,2})\s*(\d{1,3}|--)\s*Details"

    # Find all move names using regex
    moves = re.findall(pattern, text)

    # Extract only the move names (first capturing group) and clean them
    move_names = [re.sub(r'\s*--| - |HGSS Only', '', move[0].strip()) for move in moves]

    return move_names

# --------------------------------------


def parse_pokemon_data(number):
    # Read file
    with open(f"./{RAW_FOLDER}/{number:0>3}.txt", "r", encoding="utf-8") as file:
        text = file.read()
    split_text = text.split('\n')
    pokemon_data = {}

    damage_log = False
    location_search = False
    move_search = False
    tutor_search = False

    for i, line in enumerate(split_text):
        # Stop weird double text
        if line.strip() in ("<---", "--->"):
            break

        # Get Name and number
        if line == "Name":
            pokemon_data['name'] = split_text[i+7]
            pokemon_data['jp_name'] = split_text[i+8]
            pokemon_data['number'] = split_text[i+9]
        # Get Gender Ratio
        if line == "Gender Ratio":
            if "Genderless" in split_text[i+7]:
                pokemon_data['gender_ratio'] = "Genderless"
            else:
                ratio = split_text[i+7].split('%')
                ratio = ratio[0].split(':')[1], ratio[1].split(':')[1]
                pokemon_data['gender_ratio'] = ratio
        # Get Ability(s)
        if "Ability: " in line:
            abilities = line.split("Ability: ")[1]
            pokemon_data['ability'] = []
            for a in abilities.split('&'):
                pokemon_data['ability'].append(a.strip())
        # Classification, Height, Weight, Capture Rate, Base Egg Steps
        if "Classification" in line:
            pokemon_data["classification"] = split_text[i+7]
            pokemon_data["height"] = split_text[i+8]
            pokemon_data["weight"] = split_text[i+9]
            pokemon_data["capture_rate"] = split_text[i+10]
            pokemon_data["base_egg_steps"] = split_text[i+11]
        # Experience Growth, Base Happiness, Effort Values Earned, Colour, Safari Zone Flee Rate
        if "Experience Growth" in line:
            exp_growth = split_text[i+7].split('Points')
            exp_growth = exp_growth[0].strip(), exp_growth[1]
            pokemon_data["experience_growth"] = exp_growth
            pokemon_data["base_happiness"] = split_text[i+8]
            pokemon_data["effort_values_earned"] = get_evs(split_text[i+9])
            pokemon_data["color"] = split_text[i+10]
            pokemon_data["safari_zone_flee_rate"] = split_text[i+11]
        # Damage
        if "Damage Taken" in line and not damage_log:
            damage_log = True
            damage = [d[1:] for d in split_text[i+55:i+72]]
            pokemon_data["damage"] = damage
        # Item
        if "Wild Hold Item" in line:
            held_item = split_text[i+4]
            #print(held_item)
            if r"D/P/PtHG/SS" in held_item:
                held_item = held_item.split('%')[1:]
                if len(held_item) == 2:
                    held_item = held_item[0] + "%"
                else:
                    held_item = held_item[0]

            if held_item == "No Hold Item":
                pokemon_data["held_item"] = None
            else:
                if held_item.count("%") > 1:
                    held_item = held_item.split('%')
                    held_item = held_item[0].strip()+'%', held_item[1]+'%'
                else:
                    held_item = [held_item]
                pokemon_data["held_item"] = []
                for i in held_item:
                    i = i.split('- ')
                    i = i[0].strip(), i[1][:-1]
                    pokemon_data["held_item"].append(i)
        # Egg groups
        if "Egg Groups" in line:
            if "cannot breed" in split_text[i+4]:
                pokemon_data["egg_groups"] = None
            else:
                pokemon_data["egg_groups"] = []
                egg_groups = []
                egg_groups.append(split_text[i+5])
                if len(split_text[i+7]) > 2:
                    egg_groups.append(split_text[i+7])
                for e in egg_groups:
                    eg = e.split("Ditto")[-1].strip()
                    pokemon_data["egg_groups"].append(eg)
        # Flavor Text
        if "HeartGold" == line.strip() and "SoulSilver" == split_text[i+5]:
            pokemon_data["flavor_text"] = [split_text[i+1].strip()]
            ss_text = split_text[i+7].strip()
            if ss_text != "":
                pokemon_data["flavor_text"].append(ss_text)
        # Start looking for location
        if not location_search and ("Location (In-Depth Details)" in line or 
                                    ("Location" in line and "Game" in split_text[i+5].strip())):
            location_search = True
            pokemon_data["location"] = []
        elif location_search and "HeartGold" in line:
            pokemon_data["location"].append(fix_location(split_text[i+3].strip()))
        elif location_search and "SoulSilver" in line:
            location_search = False
            pokemon_data["location"].append(fix_location(split_text[i+3].strip()))
        # Get Move Text
        if "HeartGold/SoulSilver Level Up" in line:
            pokemon_data["learnset"] = extract_hgss_moves(line)

            pokemon_data["TMHM"] = [line[-4:]]
            move_search = True
            move_search_count = 0
        elif move_search:
            if "HeartGold/SoulSilver Move Tutor Attacks" in line:
                move_search = False
                tutor_search = True
                move_search_count = 0
                pokemon_data["tutor_moves"] = []
            else:
                move_search_count += 1
                if "athlon Stats" not in line and move_search_count%8 == 0:
                    pokemon_data["TMHM"].append(line[-4:])
        # Tutor and Egg Moves
        elif tutor_search:
            if "Egg Moves" in line:
                tutor_search = False
                pokemon_data["egg_moves"] = extract_egg_moves(line)
            else:
                if "Base/Max Pok\u00e9" in line:
                    tutor_search = False
                else:
                    if move_search_count % 9 == 0:
                        pokemon_data["tutor_moves"].append(line.strip())
                    move_search_count += 1
        if "Stats" == line.strip():
            base_stats = (
                split_text[i+9],
                split_text[i+10],
                split_text[i+11],
                split_text[i+12],
                split_text[i+13],
                split_text[i+14]
            )
            pokemon_data["stats"] = base_stats
        if "Max StatsHindering Nature" in line:
            # 50: [min, neutral, max], 100: -//-
            pokemon_data["possible_stats"] = {50: [[] for n in range(6)], 100: [[] for m in range(6)]}
            for mnm in range(3):
                starter_i = i+15*mnm
                for lvl_i, lvl in enumerate((50, 100)):
                    for s in range(6):
                        pokemon_data["possible_stats"][lvl][s].append(split_text[starter_i + lvl_i*7 + 2 + s])
    return pokemon_data


def store_data(p_data, number, name=None):
    if name is None:
        name = f"./{STORAGE_FOLDER}/{number:0>3}.txt"

    with open(name, 'w+', encoding="utf-8") as file:
        file.write(json.dumps(p_data, indent=4))
    return


def process_pokemon(number):
    store_data(parse_pokemon_data(number), number)
    return


if __name__ == "__main__":
    pass