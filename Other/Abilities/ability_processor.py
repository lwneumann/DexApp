def get_text():
    with open("abilities.txt", "r") as file:
        text = file.read()
    return text.split("\n")


def get_abilities():
    numbers = {"Bulbasaur":1,"Ivysaur":2,"Venusaur":3,"Charmander":4,"Charmeleon":5,"Charizard":6,"Squirtle":7,"Wartortle":8,"Blastoise":9,"Caterpie":10,"Metapod":11,"Butterfree":12,"Weedle":13,"Kakuna":14,"Beedrill":15,"Pidgey":16,"Pidgeotto":17,"Pidgeot":18,"Rattata":19,"Raticate":20,"Spearow":21,"Fearow":22,"Ekans":23,"Arbok":24,"Pikachu":25,"Raichu":26,"Sandshrew":27,"Sandslash":28,"Nidoran♀":29,"Nidorina":30,"Nidoqueen":31,"Nidoran♂":32,"Nidorino":33,"Nidoking":34,"Clefairy":35,"Clefable":36,"Vulpix":37,"Ninetales":38,"Jigglypuff":39,"Wigglytuff":40,"Zubat":41,"Golbat":42,"Oddish":43,"Gloom":44,"Vileplume":45,"Paras":46,"Parasect":47,"Venonat":48,"Venomoth":49,"Diglett":50,"Dugtrio":51,"Meowth":52,"Persian":53,"Psyduck":54,"Golduck":55,"Mankey":56,"Primeape":57,"Growlithe":58,"Arcanine":59,"Poliwag":60,"Poliwhirl":61,"Poliwrath":62,"Abra":63,"Kadabra":64,"Alakazam":65,"Machop":66,"Machoke":67,"Machamp":68,"Bellsprout":69,"Weepinbell":70,"Victreebel":71,"Tentacool":72,"Tentacruel":73,"Geodude":74,"Graveler":75,"Golem":76,"Ponyta":77,"Rapidash":78,"Slowpoke":79,"Slowbro":80,"Magnemite":81,"Magneton":82,"Farfetch'd":83,"Doduo":84,"Dodrio":85,"Seel":86,"Dewgong":87,"Grimer":88,"Muk":89,"Shellder":90,"Cloyster":91,"Gastly":92,"Haunter":93,"Gengar":94,"Onix":95,"Drowzee":96,"Hypno":97,"Krabby":98,"Kingler":99,"Voltorb":100,"Electrode":101,"Exeggcute":102,"Exeggutor":103,"Cubone":104,"Marowak":105,"Hitmonlee":106,"Hitmonchan":107,"Lickitung":108,"Koffing":109,"Weezing":110,"Rhyhorn":111,"Rhydon":112,"Chansey":113,"Tangela":114,"Kangaskhan":115,"Horsea":116,"Seadra":117,"Goldeen":118,"Seaking":119,"Staryu":120,"Starmie":121,"Mr. Mime":122,"Scyther":123,"Jynx":124,"Electabuzz":125,"Magmar":126,"Pinsir":127,"Tauros":128,"Magikarp":129,"Gyarados":130,"Lapras":131,"Ditto":132,"Eevee":133,"Vaporeon":134,"Jolteon":135,"Flareon":136,"Porygon":137,"Omanyte":138,"Omastar":139,"Kabuto":140,"Kabutops":141,"Aerodactyl":142,"Snorlax":143,"Articuno":144,"Zapdos":145,"Moltres":146,"Dratini":147,"Dragonair":148,"Dragonite":149,"Mewtwo":150,"Mew":151,"Chikorita":152,"Bayleef":153,"Meganium":154,"Cyndaquil":155,"Quilava":156,"Typhlosion":157,"Totodile":158,"Croconaw":159,"Feraligatr":160,"Sentret":161,"Furret":162,"Hoothoot":163,"Noctowl":164,"Ledyba":165,"Ledian":166,"Spinarak":167,"Ariados":168,"Crobat":169,"Chinchou":170,"Lanturn":171,"Pichu":172,"Cleffa":173,"Igglybuff":174,"Togepi":175,"Togetic":176,"Natu":177,"Xatu":178,"Mareep":179,"Flaaffy":180,"Ampharos":181,"Bellossom":182,"Marill":183,"Azumarill":184,"Sudowoodo":185,"Politoed":186,"Hoppip":187,"Skiploom":188,"Jumpluff":189,"Aipom":190,"Sunkern":191,"Sunflora":192,"Yanma":193,"Wooper":194,"Quagsire":195,"Espeon":196,"Umbreon":197,"Murkrow":198,"Slowking":199,"Misdreavus":200,"Unown":201,"Wobbuffet":202,"Girafarig":203,"Pineco":204,"Forretress":205,"Dunsparce":206,"Gligar":207,"Steelix":208,"Snubbull":209,"Granbull":210,"Qwilfish":211,"Scizor":212,"Shuckle":213,"Heracross":214,"Sneasel":215,"Teddiursa":216,"Ursaring":217,"Slugma":218,"Magcargo":219,"Swinub":220,"Piloswine":221,"Corsola":222,"Remoraid":223,"Octillery":224,"Delibird":225,"Mantine":226,"Skarmory":227,"Houndour":228,"Houndoom":229,"Kingdra":230,"Phanpy":231,"Donphan":232,"Porygon2":233,"Stantler":234,"Smeargle":235,"Tyrogue":236,"Hitmontop":237,"Smoochum":238,"Elekid":239,"Magby":240,"Miltank":241,"Blissey":242,"Raikou":243,"Entei":244,"Suicune":245,"Larvitar":246,"Pupitar":247,"Tyranitar":248,"Lugia":249,"Ho-oh":250,"Celebi":251,"Treecko":252,"Grovyle":253,"Sceptile":254,"Torchic":255,"Combusken":256,"Blaziken":257,"Mudkip":258,"Marshtomp":259,"Swampert":260,"Poochyena":261,"Mightyena":262,"Zigzagoon":263,"Linoone":264,"Wurmple":265,"Silcoon":266,"Beautifly":267,"Cascoon":268,"Dustox":269,"Lotad":270,"Lombre":271,"Ludicolo":272,"Seedot":273,"Nuzleaf":274,"Shiftry":275,"Taillow":276,"Swellow":277,"Wingull":278,"Pelipper":279,"Ralts":280,"Kirlia":281,"Gardevoir":282,"Surskit":283,"Masquerain":284,"Shroomish":285,"Breloom":286,"Slakoth":287,"Vigoroth":288,"Slaking":289,"Nincada":290,"Ninjask":291,"Shedinja":292,"Whismur":293,"Loudred":294,"Exploud":295,"Makuhita":296,"Hariyama":297,"Azurill":298,"Nosepass":299,"Skitty":300,"Delcatty":301,"Sableye":302,"Mawile":303,"Aron":304,"Lairon":305,"Aggron":306,"Meditite":307,"Medicham":308,"Electrike":309,"Manectric":310,"Plusle":311,"Minun":312,"Volbeat":313,"Illumise":314,"Roselia":315,"Gulpin":316,"Swalot":317,"Carvanha":318,"Sharpedo":319,"Wailmer":320,"Wailord":321,"Numel":322,"Camerupt":323,"Torkoal":324,"Spoink":325,"Grumpig":326,"Spinda":327,"Trapinch":328,"Vibrava":329,"Flygon":330,"Cacnea":331,"Cacturne":332,"Swablu":333,"Altaria":334,"Zangoose":335,"Seviper":336,"Lunatone":337,"Solrock":338,"Barboach":339,"Whiscash":340,"Corphish":341,"Crawdaunt":342,"Baltoy":343,"Claydol":344,"Lileep":345,"Cradily":346,"Anorith":347,"Armaldo":348,"Feebas":349,"Milotic":350,"Castform":351,"Kecleon":352,"Shuppet":353,"Banette":354,"Duskull":355,"Dusclops":356,"Tropius":357,"Chimecho":358,"Absol":359,"Wynaut":360,"Snorunt":361,"Glalie":362,"Spheal":363,"Sealeo":364,"Walrein":365,"Clamperl":366,"Huntail":367,"Gorebyss":368,"Relicanth":369,"Luvdisc":370,"Bagon":371,"Shelgon":372,"Salamence":373,"Beldum":374,"Metang":375,"Metagross":376,"Regirock":377,"Regice":378,"Registeel":379,"Latias":380,"Latios":381,"Kyogre":382,"Groudon":383,"Rayquaza":384,"Jirachi":385,"Deoxys":386,"Turtwig":387,"Grotle":388,"Torterra":389,"Chimchar":390,"Monferno":391,"Infernape":392,"Piplup":393,"Prinplup":394,"Empoleon":395,"Starly":396,"Staravia":397,"Staraptor":398,"Bidoof":399,"Bibarel":400,"Kricketot":401,"Kricketune":402,"Shinx":403,"Luxio":404,"Luxray":405,"Budew":406,"Roserade":407,"Cranidos":408,"Rampardos":409,"Shieldon":410,"Bastiodon":411,"Burmy":412,"Wormadam":413,"Mothim":414,"Combee":415,"Vespiquen":416,"Pachirisu":417,"Buizel":418,"Floatzel":419,"Cherubi":420,"Cherrim":421,"Shellos":422,"Gastrodon":423,"Ambipom":424,"Drifloon":425,"Drifblim":426,"Buneary":427,"Lopunny":428,"Mismagius":429,"Honchkrow":430,"Glameow":431,"Purugly":432,"Chingling":433,"Stunky":434,"Skuntank":435,"Bronzor":436,"Bronzong":437,"Bonsly":438,"Mime Jr.":439,"Happiny":440,"Chatot":441,"Spiritomb":442,"Gible":443,"Gabite":444,"Garchomp":445,"Munchlax":446,"Riolu":447,"Lucario":448,"Hippopotas":449,"Hippowdon":450,"Skorupi":451,"Drapion":452,"Croagunk":453,"Toxicroak":454,"Carnivine":455,"Finneon":456,"Lumineon":457,"Mantyke":458,"Snover":459,"Abomasnow":460,"Weavile":461,"Magnezone":462,"Lickilicky":463,"Rhyperior":464,"Tangrowth":465,"Electivire":466,"Magmortar":467,"Togekiss":468,"Yanmega":469,"Leafeon":470,"Glaceon":471,"Gliscor":472,"Mamoswine":473,"Porygon-Z":474,"Gallade":475,"Probopass":476,"Dusknoir":477,"Froslass":478,"Rotom":479,"Uxie":480,"Mesprit":481,"Azelf":482,"Dialga":483,"Palkia":484,"Heatran":485,"Regigigas":486,"Giratina":487,"Cresselia":488,"Phione":489,"Manaphy":490,"Darkrai":491,"Shaymin":492,"Arceus":493}

    text = get_text()
    ability = {}
    last = ""
    for i, line in enumerate(text):
        ab = line.split("\t")

        if "NULL" not in line:
            if i != 0:
                if len(ab) < 3:
                    if "[Field Effect]" in line:
                        mon = line.split('\t')[1].split(',')
                        mon = [m.strip() for m in mon]
                        for p in range(len(mon)):
                            name = mon[p]
                            if "Deoxys" in name:
                                name = "Deoxys"
                            name = name.replace("â™€", "♀")
                            name = name.replace("â™‚", "♂")
                            ability[last][1].append([ name, numbers[name] ])
                        last = ""
                    else:
                        name, effect = line.split("\t")
                        ability[name] = [effect, []]
                        last = name
                else:
                    ability[ab[0].strip()] = [ab[1], ab[2].split(", ")]
                    mon = ability[ab[0].strip()][1]
                    for p in range(len(mon)):        
                        name = ability[ab[0].strip()][1][p]
                        name = name.replace("â™€", "♀")
                        name = name.replace("â™‚", "♂")
                        ability[ab[0].strip()][1][p] = [ name, numbers[name] ]
                

    with open(f"abilities.py", 'w+', encoding="utf-8") as file:
        file.write("ability_list=" + str(ability))
    return


if __name__ == "__main__":
    get_abilities()
