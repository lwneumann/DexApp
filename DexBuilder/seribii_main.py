from alive_progress import alive_bar
import scraper
from processor import process_pokemon
from config import *


def get_raw():
    print()
    print(f"Getting Raw Sites storing into ./{RAW_FOLDER}/")
    with alive_bar(TOTAL_MON) as bar:
        for p in range(1, TOTAL_MON+1):
            scraper.store_site(p, RAW_FOLDER)
            bar()
    return


def process_raw():
    print()
    print(f"Processing Sites storing into ./{STORAGE_FOLDER}/")
    with alive_bar(TOTAL_MON) as bar:
        for p in range(1, TOTAL_MON+1):
            process_pokemon(p)
            bar()
    return


def get_dict(number):
    with open(f"./{STORAGE_FOLDER}/{number:0>3}.txt", 'r') as file:
        data = file.read()
    data = data.replace("null", "None")
    data = eval(data)
    return data


def compile():
    dex = {}
    print()
    print("Compiling processed data")
    with alive_bar(TOTAL_MON) as bar:
        for p in range(1, TOTAL_MON+1):
            entry = get_dict(p)
            dex[p] = entry
            bar()

    with open(f"{FIRST_DEX}.py", 'w+', encoding="utf-8") as file:
        file.write("full_dex="+str(dex))
        # file.write(json.dumps(dex, indent=5))
    print()
    print(f"Saved Dex as {FIRST_DEX}.py")
    return


def compile_raw():
    process_raw()
    compile()
    return

if __name__ == "__main__":
    process_raw()
