from locations import locations


def fix_data(d):
    items = []
    d = d.split('\n')
    for l in d:
        line = l.split("-")
        if l == '':
            items.append("\\hline")
        else:
            line = line[0].strip(), line[1].strip()
            items.append(line)
    return items


def latexify(d_l):
    for e in d_l:
        if e == "\\hline":
            print(e)
        else:
            print(e[0], "&", e[1], "\\\\")
            print("\\hline")
    return


latexify(fix_data(locations))