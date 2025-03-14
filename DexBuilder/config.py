"""
abilities - !EXTRA!
    Stores all abilities
combine -
    -> add_all
    Combines csv info,
    pokewalker locations
dex -
    -> pokedex is dict
    py - dict dex to use in code
    txt - readable version
get_moves - !EXTRA!
    gets moves with tm names
pokewalker -  (called by combine)
    gets pokewalker data
    txt - raw text
processor -
    reads all raw scraped pages
scraper - 
    gets data from seribii
search -
    ensuring processor quailty
seribii_main -
    -> compile_raw
    compiles seribii text

make_dex -
    -> main
    DexBuilder main.
    Run main to do everything.
"""

TOTAL_MON = 493

RAW_FOLDER = "Raw"
STORAGE_FOLDER = "PC"

LOG_PATH = "log.txt"
TEMP_PATH = "temp.txt"


# -------------
FIRST_DEX = "rough_dex"
DEX_NAME = "dex"

CSV_NAME = "pokemon.csv"
WALKER_NAME = "pokewalker.txt"
MOVE_NAME = "move_list.txt"
TM_NAME = "tm_list.txt"