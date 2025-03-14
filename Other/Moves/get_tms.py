from moves import move_list


def get_tmhms():
    with open('tm_list.txt', "r", encoding="utf-8") as file:
        text = file.read()

    lines = text.split("\n")
    tmhm = {}
    for line in lines[1::2]:
        line = [ t.strip() for t in line.split('\t')]
        move_list[line[1]]
        tmhm[line[0]] = {
            'name': line[1],
            'location': line[4],
            'price': line[-1]
        }

    with open("TMHM.py", "w+", encoding='utf-8') as file:
        file.write('TMHM_list=' + str(tmhm))
    return

if __name__ == "__main__":
    get_tmhms()
