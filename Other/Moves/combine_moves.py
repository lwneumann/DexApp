import just_moves, TMHM


def combine():
    new_moves = just_moves.move_list

    for tm in TMHM.TMHM_list:
        new_moves[TMHM.TMHM_list[tm]["name"]]["TMHM"] = tm

    for m in new_moves:
        if "TMHM" not in new_moves[m]:
            new_moves[m]["TMHM"] = '--'

    with open('moves.py', "w+", encoding='utf-8') as file:
        file.write("move_list=" + str(new_moves))
    return


if __name__ == "__main__":
    combine()