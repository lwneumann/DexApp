import moves, abilities


def search(search):
    names = {'bulbasaur': 1, 'ivysaur': 2, 'venusaur': 3, 'charmander': 4, 'charmeleon': 5, 'charizard': 6, 'squirtle': 7, 'wartortle': 8, 'blastoise': 9, 'caterpie': 10, 'metapod': 11, 'butterfree': 12, 'weedle': 13, 'kakuna': 14, 'beedrill': 15, 'pidgey': 16, 'pidgeotto': 17, 'pidgeot': 18, 'rattata': 19, 'raticate': 20, 'spearow': 21, 'fearow': 22, 'ekans': 23, 'arbok': 24, 'pikachu': 25, 'raichu': 26, 'sandshrew': 27, 'sandslash': 28, 'nidoran♀': 29, 'nidorina': 30, 'nidoqueen': 31, 'nidoran♂': 32, 'nidorino': 33, 'nidoking': 34, 'clefairy': 35, 'clefable': 36, 'vulpix': 37, 'ninetales': 38, 'jigglypuff': 39, 'wigglytuff': 40, 'zubat': 41, 'golbat': 42, 'oddish': 43, 'gloom': 44, 'vileplume': 45, 'paras': 46, 'parasect': 47, 'venonat': 48, 'venomoth': 49, 'diglett': 50, 'dugtrio': 51, 'meowth': 52, 'persian': 53, 'psyduck': 54, 'golduck': 55, 'mankey': 56, 'primeape': 57, 'growlithe': 58, 'arcanine': 59, 'poliwag': 60, 'poliwhirl': 61, 'poliwrath': 62, 'abra': 63, 'kadabra': 64, 'alakazam': 65, 'machop': 66, 'machoke': 67, 'machamp': 68, 'bellsprout': 69, 'weepinbell': 70, 'victreebel': 71, 'tentacool': 72, 'tentacruel': 73, 'geodude': 74, 'graveler': 75, 'golem': 76, 'ponyta': 77, 'rapidash': 78, 'slowpoke': 79, 'slowbro': 80, 'magnemite': 81, 'magneton': 82, "farfetch'd": 83, 'doduo': 84, 'dodrio': 85, 'seel': 86, 'dewgong': 87, 'grimer': 88, 'muk': 89, 'shellder': 90, 'cloyster': 91, 'gastly': 92, 'haunter': 93, 'gengar': 94, 'onix': 95, 'drowzee': 96, 'hypno': 97, 'krabby': 98, 'kingler': 99, 'voltorb': 100, 'electrode': 101, 'exeggcute': 102, 'exeggutor': 103, 'cubone': 104, 'marowak': 105, 'hitmonlee': 106, 'hitmonchan': 107, 'lickitung': 108, 'koffing': 109, 'weezing': 110, 'rhyhorn': 111, 'rhydon': 112, 'chansey': 113, 'tangela': 114, 'kangaskhan': 115, 'horsea': 116, 'seadra': 117, 'goldeen': 118, 'seaking': 119, 'staryu': 120, 'starmie': 121, 'mr. mime': 122, 'scyther': 123, 'jynx': 124, 'electabuzz': 125, 'magmar': 126, 'pinsir': 127, 'tauros': 128, 'magikarp': 129, 'gyarados': 130, 'lapras': 131, 'ditto': 132, 'eevee': 133, 'vaporeon': 134, 'jolteon': 135, 'flareon': 136, 'porygon': 137, 'omanyte': 138, 'omastar': 139, 'kabuto': 140, 'kabutops': 141, 'aerodactyl': 142, 'snorlax': 143, 'articuno': 144, 'zapdos': 145, 'moltres': 146, 'dratini': 147, 'dragonair': 148, 'dragonite': 149, 'mewtwo': 150, 'mew': 151, 'chikorita': 152, 'bayleef': 153, 'meganium': 154, 'cyndaquil': 155, 'quilava': 156, 'typhlosion': 157, 'totodile': 158, 'croconaw': 159, 'feraligatr': 160, 'sentret': 161, 'furret': 162, 'hoothoot': 163, 'noctowl': 164, 'ledyba': 165, 'ledian': 166, 'spinarak': 167, 'ariados': 168, 'crobat': 169, 'chinchou': 170, 'lanturn': 171, 'pichu': 172, 'cleffa': 173, 'igglybuff': 174, 'togepi': 175, 'togetic': 176, 'natu': 177, 'xatu': 178, 'mareep': 179, 'flaaffy': 180, 'ampharos': 181, 'bellossom': 182, 'marill': 183, 'azumarill': 184, 'sudowoodo': 185, 'politoed': 186, 'hoppip': 187, 'skiploom': 188, 'jumpluff': 189, 'aipom': 190, 'sunkern': 191, 'sunflora': 192, 'yanma': 193, 'wooper': 194, 'quagsire': 195, 'espeon': 196, 'umbreon': 197, 'murkrow': 198, 'slowking': 199, 'misdreavus': 200, 'unown': 201, 'wobbuffet': 202, 'girafarig': 203, 'pineco': 204, 'forretress': 205, 'dunsparce': 206, 'gligar': 207, 'steelix': 208, 'snubbull': 209, 'granbull': 210, 'qwilfish': 211, 'scizor': 212, 'shuckle': 213, 'heracross': 214, 'sneasel': 215, 'teddiursa': 216, 'ursaring': 217, 'slugma': 218, 'magcargo': 219, 'swinub': 220, 'piloswine': 221, 'corsola': 222, 'remoraid': 223, 'octillery': 224, 'delibird': 225, 'mantine': 226, 'skarmory': 227, 'houndour': 228, 'houndoom': 229, 'kingdra': 230, 'phanpy': 231, 'donphan': 232, 'porygon2': 233, 'stantler': 234, 'smeargle': 235, 'tyrogue': 236, 'hitmontop': 237, 'smoochum': 238, 'elekid': 239, 'magby': 240, 'miltank': 241, 'blissey': 242, 'raikou': 243, 'entei': 244, 'suicune': 245, 'larvitar': 246, 'pupitar': 247, 'tyranitar': 248, 'lugia': 249, 'ho-oh': 250, 'celebi': 251, 'treecko': 252, 'grovyle': 253, 'sceptile': 254, 'torchic': 255, 'combusken': 256, 'blaziken': 257, 'mudkip': 258, 'marshtomp': 259, 'swampert': 260, 'poochyena': 261, 'mightyena': 262, 'zigzagoon': 263, 'linoone': 264, 'wurmple': 265, 'silcoon': 266, 'beautifly': 267, 'cascoon': 268, 'dustox': 269, 'lotad': 270, 'lombre': 271, 'ludicolo': 272, 'seedot': 273, 'nuzleaf': 274, 'shiftry': 275, 'taillow': 276, 'swellow': 277, 'wingull': 278, 'pelipper': 279, 'ralts': 280, 'kirlia': 281, 'gardevoir': 282, 'surskit': 283, 'masquerain': 284, 'shroomish': 285, 'breloom': 286, 'slakoth': 287, 'vigoroth': 288, 'slaking': 289, 'nincada': 290, 'ninjask': 291, 'shedinja': 292, 'whismur': 293, 'loudred': 294, 'exploud': 295, 'makuhita': 296, 'hariyama': 297, 'azurill': 298, 'nosepass': 299, 'skitty': 300, 'delcatty': 301, 'sableye': 302, 'mawile': 303, 'aron': 304, 'lairon': 305, 'aggron': 306, 'meditite': 307, 'medicham': 308, 'electrike': 309, 'manectric': 310, 'plusle': 311, 'minun': 312, 'volbeat': 313, 'illumise': 314, 'roselia': 315, 'gulpin': 316, 'swalot': 317, 'carvanha': 318, 'sharpedo': 319, 'wailmer': 320, 'wailord': 321, 'numel': 322, 'camerupt': 323, 'torkoal': 324, 'spoink': 325, 'grumpig': 326, 'spinda': 327, 'trapinch': 328, 'vibrava': 329, 'flygon': 330, 'cacnea': 331, 'cacturne': 332, 'swablu': 333, 'altaria': 334, 'zangoose': 335, 'seviper': 336, 'lunatone': 337, 'solrock': 338, 'barboach': 339, 'whiscash': 340, 'corphish': 341, 'crawdaunt': 342, 'baltoy': 343, 'claydol': 344, 'lileep': 345, 'cradily': 346, 'anorith': 347, 'armaldo': 348, 'feebas': 349, 'milotic': 350, 'castform': 351, 'kecleon': 352, 'shuppet': 353, 'banette': 354, 'duskull': 355, 'dusclops': 356, 'tropius': 357, 'chimecho': 358, 'absol': 359, 'wynaut': 360, 'snorunt': 361, 'glalie': 362, 'spheal': 363, 'sealeo': 364, 'walrein': 365, 'clamperl': 366, 'huntail': 367, 'gorebyss': 368, 'relicanth': 369, 'luvdisc': 370, 'bagon': 371, 'shelgon': 372, 'salamence': 373, 'beldum': 374, 'metang': 375, 'metagross': 376, 'regirock': 377, 'regice': 378, 'registeel': 379, 'latias': 380, 'latios': 381, 'kyogre': 382, 'groudon': 383, 'rayquaza': 384, 'jirachi': 385, 'deoxys': 386, 'turtwig': 387, 'grotle': 388, 'torterra': 389, 'chimchar': 390, 'monferno': 391, 'infernape': 392, 'piplup': 393, 'prinplup': 394, 'empoleon': 395, 'starly': 396, 'staravia': 397, 'staraptor': 398, 'bidoof': 399, 'bibarel': 400, 'kricketot': 401, 'kricketune': 402, 'shinx': 403, 'luxio': 404, 'luxray': 405, 'budew': 406, 'roserade': 407, 'cranidos': 408, 'rampardos': 409, 'shieldon': 410, 'bastiodon': 411, 'burmy': 412, 'wormadam': 413, 'mothim': 414, 'combee': 415, 'vespiquen': 416, 'pachirisu': 417, 'buizel': 418, 'floatzel': 419, 'cherubi': 420, 'cherrim': 421, 'shellos': 422, 'gastrodon': 423, 'ambipom': 424, 'drifloon': 425, 'drifblim': 426, 'buneary': 427, 'lopunny': 428, 'mismagius': 429, 'honchkrow': 430, 'glameow': 431, 'purugly': 432, 'chingling': 433, 'stunky': 434, 'skuntank': 435, 'bronzor': 436, 'bronzong': 437, 'bonsly': 438, 'mime jr.': 439, 'happiny': 440, 'chatot': 441, 'spiritomb': 442, 'gible': 443, 'gabite': 444, 'garchomp': 445, 'munchlax': 446, 'riolu': 447, 'lucario': 448, 'hippopotas': 449, 'hippowdon': 450, 'skorupi': 451, 'drapion': 452, 'croagunk': 453, 'toxicroak': 454, 'carnivine': 455, 'finneon': 456, 'lumineon': 457, 'mantyke': 458, 'snover': 459, 'abomasnow': 460, 'weavile': 461, 'magnezone': 462, 'lickilicky': 463, 'rhyperior': 464, 'tangrowth': 465, 'electivire': 466, 'magmortar': 467, 'togekiss': 468, 'yanmega': 469, 'leafeon': 470, 'glaceon': 471, 'gliscor': 472, 'mamoswine': 473, 'porygon-z': 474, 'gallade': 475, 'probopass': 476, 'dusknoir': 477, 'froslass': 478, 'rotom': 479, 'uxie': 480, 'mesprit': 481, 'azelf': 482, 'dialga': 483, 'palkia': 484, 'heatran': 485, 'regigigas': 486, 'giratina': 487, 'cresselia': 488, 'phione': 489, 'manaphy': 490, 'darkrai': 491, 'shaymin': 492, 'arceus': 493}
    result = {}

    # Get Mon
    dex_search = [[names[mon], mon] for mon in 
                    names if search.lower() in mon.lower()]
    if len(dex_search) > 0:
        result["dex"] = dex_search
        if search.lower() in dex_search:
            return {"dex": [names[search.lower(), search.title()]]}, True

    # Get Moves
    move_search = [move for move in 
                    moves.move_list if search.lower() in move.lower()]
    if len(move_search) > 0:
        result['moves'] = move_search
        if search.lower() in [ m.lower() for m in move_search ]:
            themove = [m for m in move_search if search.lower() == m.lower()]
            return {"moves": themove}, True

    # Get Abilities
    ability_search = [ability for ability in 
                    abilities.ability_list if search.lower() in ability.lower()]
    if len(ability_search) > 0:
        result["ability"] = ability_search
        if search.lower() in [ a.lower() for a in ability_search ]:
            theability = [a for a in ability_search if search.lower() == a.lower()]
            return {"ability": theability}, True

    # Partial Single Result
    # (Perfect Searches covered above)
    single = False
    if len(result) == 1 and len(result[list(result.keys())[0]]) == 1:
        single = True

    return result, single


def pretty_search(result):
    new_result = []
    for r in result:
        header = {'dex': 'Pokémon', 'moves': 'Moves', 'ability': "Abilities"}[r]
        url = {'dex': 'mon_page', 'moves': 'move_page', 'ability': "ability_page"}[r]

        if r == 'dex':
            new_result.append([[header, url]])
            for p in result[r]:
                new_result[-1].append([ p[0], p[1].title() ])
        else:
            new_result.append([[header, url]] + result[r])

    good_search = True
    if result == {}:
        good_search = False

    return new_result, good_search
