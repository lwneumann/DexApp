import re
from dex import pokedex
from seribii_main import compile_raw
from config import *


def get_max_stats():
    for st in range(6):
        m = 0
        mp = []
        print()
        print(["HP", "Attack", "Defense", "Sp. Attack", "Sp. Defense", "Speed"][st])
        for p in range(1, 494):
            s = int(pokedex[p]["stats"][st])
            if s >= m:
                if s > m:
                    mp = []
                    m = s
                mp.append(pokedex[p]['name'])
        print(m, mp)
    return


def count_keys():
    kcount = {}
    mt = []
    for p in range(1, 494):
        tutmoves = False
        for k in pokedex[p].keys():
            if k not in kcount.keys():
                kcount[k] = 1
            else:
                kcount[k] += 1
            if k == "tutor_moves":
                tutmoves = True
        if not tutmoves:
            mt.append(pokedex[p]['name'])
    print()
    print(f"{'Key Counts':-<40}")
    for k in kcount.keys():
        print(("X", "-")[kcount[k] == 493], kcount[k], k)
    print('-'*40)
    print(mt)
    return 


def check_ps():
    for p in range(1, 494):
        print(p, pokedex[p]["name"], pokedex[p]["possible_stats"].keys())
    return


def missing():
    count = 0
    for p in range(1, 494):
        if "location" not in pokedex[p].keys():
            print(p, pokedex[p]['name'])
            count += 1
    print()
    print(count, "missing")
    return


def check_raw_counts():
    print()
    print('-'*20)
    print("Missing Information")
    print('-'*20)
    egg_c = 0
    tutor_c = 0
    missing_tmon = []
    for p in range(1, 494):
        with open(f"./{RAW_FOLDER}/{p:0>3}.txt", "r", encoding="utf-8") as file:
            text = file.read()
        if "Egg Moves" in text:
            egg_c += 1
        if "Tutor Attacks" in text:
            tutor_c += 1
        else:
            missing_tmon.append(p)
    print()
    print(tutor_c, "Tutor Moves")
    print(egg_c, "Egg Moves")
    print([pokedex[n]['name'] for n in missing_tmon])
    return


def only_headbutt():
    only_h = []

    for p in pokedex.keys():
        for l in pokedex[p]["location"]:
            if l[-10:] == "(Headbutt)":
                name = pokedex[p]["name"]
                if name not in only_h:
                    only_h.append(name)
    return only_h


def weight_lbs():
    w = []
    for p in range(1, 494):
        un = pokedex[p]["weight"][-3:]
        if un not in w:
            w.append(un)
    return w


def classifications():
    c = []
    for p in range(1, 494):
        cl = pokedex[p]["classification"].split(' ')[-1]
        if cl not in c:
            c.append(cl)
    return c


def locations():
    l = {}
    for p in range(1, 494):
        loc = len(pokedex[p]["location"])
        if loc not in l:
            l[loc] = 0
        l[loc] += 1
    for k in l:
        print(k, l[k])
    return


def stat_sums():
    max_s = 0
    name = ''
    for p in range(1, 494):
        stats = pokedex[p]["stats"]
        ss = sum([ int(s) for s in stats ])
        if ss > max_s:
            max_s = ss
            name = pokedex[p]["name"]
    print(name, max_s)
    return


def egg_moves():
    ec = {}
    for p in range(1, 494):
        print(p)
        eggs = pokedex[p]["egg_moves"]
        if len(eggs) not in ec:
            ec[len(eggs)] = 0
        ec[len(eggs)] += 1
    for k in ec:
        print(k, ec[k])
    return


def make_num_list():
    nums = "names = {"
    for p in range(1, 494):
        if p != 1:
            nums += ","
        nums += '"' + pokedex[p]['name'] + '"' + ":" + str(p)
    nums += "}"

    #with open("nameNums.py", "w+", encoding="utf-8") as file:
    #    file.write(nums)
    print(nums)
    return


def get_jp_names():
    c = 0
    for p in range(1, 494):
        c += 1
        jpo = re.sub(r'[^\u3040-\u30ff\u4e00-\u9faf]', '', pokedex[p]['jp_name'])
        print(c, jpo)
    return


if __name__ == "__main__":
    stat_sums()
