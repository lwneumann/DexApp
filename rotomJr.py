import os, re, shutil
from alive_progress import alive_bar
from DexBuilder.dex import pokedex
from Other.Moves.moves import move_list
from Other.Moves.TMHM import TMHM_list
from Other.Abilities.abilities import ability_list


FEM_IMGS_PATH = "./DexApp/static/img/sprites/female"


# -- Fix Missing Images

def add_same_backs(num):
    BASE = './DexApp/static/img/sprites/back/'
    source = BASE + f'{num}.png'
    destination = BASE + "female/" + f'{num}.png'
    shutil.copy(source, destination)

    BASE += "shiny/"
    source = BASE + f'{num}.png'
    destination = BASE + "female/" + f'{num}.png'
    shutil.copy(source, destination)
    return


# -- Page Populating

class Mon:
    def __init__(self):
        self.items = False
        self.egg_moves = False
        self.tutor_moves = False
        self.female_img = False
        self.pokewalker = False
        self.pokewalker_items = False
        return

    def __str__(self):
        return str([self.items, self.egg_moves, self.tutor_moves, self.female_img,
                    self.pokewalker, self.pokewalker_items])


def female_list():
    return [m[:-4] for m in os.listdir(FEM_IMGS_PATH)]


def dex_search():
    pokes = {}
    f_list = female_list()

    for p in range(1, 494):
        pokes[p] = Mon()
        mon = pokedex[p]

        # Female
        if str(p) in f_list:
            pokes[p].female_img = True

        # Key Search
        if mon['held_item'] is not None:
            pokes[p].items = True
        if "egg_moves" in mon:
            pokes[p].egg_moves = True
        if "tutor_moves" in mon:
            pokes[p].tutor_moves = True
        if "pokewalker" in mon:
            pokes[p].pokewalker = True
            if "item" in mon["pokewalker"]:
                pokes[p].pokewalker_items = True
    return pokes


def complete_learned_move_list(moves):
    new_moves = []

    # Level Learned, Move, Type, Category, Power, Accuracy, PP, Description
    for lvl in moves:
        for m in moves[lvl]:
            if m != '':
                if m == "The foe is hit with a destructive shock wave that always inflicts":
                    m = "SonicBoom"
                elif m == "The user looses its grudge on the move last used by the foe by cutting":
                    m = "Spite"
                elif m == 'The user endures any attack with at least':
                    m = "Endure"

                if m not in [i[1] for i in new_moves]:
                    move = [lvl,
                            m,
                            move_list[m]["type"].lower(),
                            move_list[m]["category"],
                            move_list[m]["power"],
                            move_list[m]["accuracy"],
                            move_list[m]["PP"],
                            move_list[m]["Effect"].replace('Ã©', 'é')
                            ]
                    new_moves.append(move)
    return new_moves


def complete_TMHM_move_list(moves):
    new_moves = []
    for tm in moves:
        if tm.strip() not in ("HGSS", "DPt"):
            if "%" in tm:
                return []
            elif tm[:2] in ("TM", "HM"):
                move_info = move_list[TMHM_list[tm]['name']]

                move = [tm,
                        TMHM_list[tm]['name'],
                        move_info["type"].lower(),
                        move_info["category"],
                        move_info["power"],
                        move_info["accuracy"],
                        move_info["PP"],
                        move_info["Effect"].replace('Ã©', 'é')
                        ]
                new_moves.append(move)

    return new_moves


def complete_move_list(moves):
    new_moves = []
    for tut in moves:
        if "Base/Max" in tut:
            return new_moves
        move = [tut,
                move_list[tut]["type"].lower(),
                move_list[tut]["category"],
                move_list[tut]["power"],
                move_list[tut]["accuracy"],
                move_list[tut]["PP"],
                move_list[tut]["Effect"].replace('Ã©', 'é')
                ]
        new_moves.append(move)
    return new_moves


def get_template():
    with open("./PageMaker/template.txt", "r", encoding="utf-8") as file:
        text = file.read()
    return text


def get_stat_ranges(mon):
    # 50, 100
    s_ranges = [[], []]

    for s in range(6):
        l = mon["possible_stats"]["50"][s][0].split(' - ')[0]
        h = mon["possible_stats"]["50"][s][2].split(' - ')[1]
        s_ranges[0].append(f"{l} - {h}")

        l = mon["possible_stats"]["100"][s][0].split(' - ')[0]
        h = mon["possible_stats"]["100"][s][2].split(' - ')[1]
        s_ranges[1].append(f"{l} - {h}")
    return s_ranges


def get_abilities(mon):
    new_abs = []
    for a in mon["ability"]:
        if "Forme" in a:
            a = a.split('(')[0].strip()
        new_abs.append( [a, ability_list[a][0]] )
    return new_abs


def make_page(num, moncases):
    # Get info
    pokemon = pokedex[num]
    jp_name = re.sub(r'[^\u3040-\u30ff\u4e00-\u9faf]', '', pokemon['jp_name'])
    has_fem = moncases.female_img
    classification = pokemon["classification"].split(' ')[0]
    if pokemon["egg_groups"] is None:
        egg_group = f"{pokemon["name"]} cannot breed"
    else:
        egg_group = ", ".join(pokemon["egg_groups"])
    exp_growth = f"{pokemon["experience_growth"][0]} - {pokemon["experience_growth"][1]}"
    gender_ratio = f"♂: {pokemon['gender_ratio'][0]}% &emsp; ♀: {pokemon['gender_ratio'][1]}%"
    has_held_item = pokemon['held_item'] is not None
    has_pokewalker = moncases.pokewalker
    has_pokewalker_items = moncases.pokewalker_items
    pokewalker_info = None
    if has_pokewalker:
        pokewalker_info = [pokemon["pokewalker"]["area"]]
        if has_pokewalker_items:
            pokewalker_info.append(pokemon["pokewalker"]["item"])
    stats = pokemon["stats"]
    stat_ranges = get_stat_ranges(pokemon)
    stat_widths = [ str(round((int(s)/255) * 100)) for s in stats ]
    stat_sum = sum([ int(s) for s in pokemon["stats"] ])
    stat_sum_w = str(round((stat_sum/720) * 100))
    effort_values = [ str(e) for e in pokemon["effort_values_earned"]]
    mon_abilities = get_abilities(pokemon)
    l_moves = complete_learned_move_list(pokemon["learnset"])
    # Dense Pokemon |
    #               V
    has_tmhm = num not in (129, 132, 201, 202, 235, 360, 374, 401)
    tm_moves = None
    if has_tmhm:
        tm_moves = complete_TMHM_move_list(pokemon["TMHM"])
    tut_moves = None
    if moncases.tutor_moves:
        tut_moves = complete_move_list(pokemon["tutor_moves"])
    e_moves = None
    if moncases.egg_moves:
        e_moves = complete_move_list(pokemon["egg_moves"])

    # Populate
    page = get_template()
    page = page.replace("PRIOR", str(num-1))
    page = page.replace("NEXT", str(num+1))
    page = page.replace("NUMBER", str(num))
    page = page.replace("ENNAME", pokemon["name"])
    page = page.replace("JPNAME", jp_name)
    page = page.replace("HASFEM", str(has_fem))
    page = page.replace("FLAVOR1", pokemon["flavor_text"][0])
    page = page.replace("FLAVOR2", pokemon["flavor_text"][-1])
    page = page.replace("CLASSIFICATION", classification)
    page = page.replace("HEIGHT", pokemon["height"])
    page = page.replace("WEIGHT", pokemon["weight"][:-3])
    page = page.replace("CAPRATE", pokemon["capture_rate"])
    page = page.replace("EGGSTEP", pokemon["base_egg_steps"])
    page = page.replace("EGGGROUP", egg_group)
    page = page.replace("EXPGROWTH", exp_growth)
    page = page.replace("SAFZONE", pokemon["safari_zone_flee_rate"])
    page = page.replace("COLOR", pokemon["color"])
    page = page.replace("BASEHAPP", pokemon["base_happiness"])
    page = page.replace("GENDRATIO", gender_ratio)
    page = page.replace("HASHELDITEM", str(has_held_item))
    page = page.replace("THEHELDITEMS", str(pokemon["held_item"]))
    page = page.replace("DAMAGE", str(pokemon["damage"]))
    page = page.replace("LOCATIONS", str(pokemon["location"]))
    page = page.replace("HASPOKEWALKER", str(has_pokewalker))
    page = page.replace("POKEITEMS", str(has_pokewalker_items))
    page = page.replace("POKEWALKERINF", str(pokewalker_info))
    
    for i, s in enumerate(["HP", "AATT", "DEEF", "SPATT", "SPDEF", "SPED"]):
        stat = "ST" + s
        width = "STw" + s
        stat_r_50 = s + "RANGE50"
        stat_r_100 = s + "RANGE100"

        page = page.replace(stat, stats[i])
        page = page.replace(width, stat_widths[i])
        page = page.replace(stat_r_50, stat_ranges[0][i])
        page = page.replace(stat_r_100, stat_ranges[1][i])
    page = page.replace("STATSUM", str(stat_sum))
    page = page.replace("STATwSUM", str(stat_sum_w))

    page = page.replace("EVSPREAD", str(effort_values))
    page = page.replace("ABILITIES", str(mon_abilities))
    page = page.replace("LEARNEDMOVES", str(l_moves))
    page = page.replace("HASTMHMMOVES", str(has_tmhm))
    page = page.replace("TMHMLIST", str(tm_moves))
    page = page.replace("HASTUTORMOVES", str(moncases.tutor_moves))
    page = page.replace("THETUTORMOVES", str(tut_moves))
    page = page.replace("HASEGGMOVES", str(moncases.egg_moves))
    page = page.replace("THEEGGMOVES", str(e_moves))

    # Save
    with open(f"./DexApp/templates/dex/{num}.html", "w+", encoding='utf-8') as file:
        file.write(page)
    return


def make_all_pages():
    edge_mon = dex_search()

    print()
    print('Making HTML pages')
    with alive_bar(493) as bar:
        for p in range(1, 494):
            make_page(p, edge_mon[p])
            bar()
    return


if __name__ == "__main__":
    make_all_pages()
