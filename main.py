import curses
import json
from handlers import internet_radio, spotify, casting, podcasts, load_ascii_art, type_out, back
import navigation

# Load the JSON menu
with open('menu.json', 'r') as file:
    menu_data = json.load(file)
    main_menu_items = menu_data["main_menu"]

# The dispatch table mapping action names to functions
action_dispatch = {
    "internet_radio": internet_radio,
    "spotify": spotify,
    "casting": casting,
    "podcasts": podcasts,
    "exit_program": exit,
    "back": back
}

header_art = load_ascii_art("header.txt")

def main(stdscr):
    navigation.setup_screen(5, 10, 5, header_art, 0, 0, main_menu_items, action_dispatch)

curses.wrapper(main)
