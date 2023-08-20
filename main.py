import curses
import json
from handlers import internet_radio, spotify, casting, podcasts


# Load the JSON menu
with open('menu.json', 'r') as file:
    menu_data = json.load(file)
    main_menu_items = menu_data["main_menu"]

# Define some padding
pad_top = 5
pad_left = 10


# The dispatch table mapping action names to functions
action_dispatch = {
    "internet_radio": internet_radio,
    "spotify": spotify,
    "casting": casting,
    "podcasts": podcasts,
    "exit_program": exit
}

ascii_art = """
    _   _           _       
   | | | |         | |      
   | |_| | __ _ ___| |_ ___ 
   |  _  |/ _` / __| __/ _ \\
   | | | | (_| \__ \ ||  __/
   \_| |_/\__,_|___/\__\___|
"""

def main(stdscr):
    curses.start_color()
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.curs_set(0)

    current_row = 0

    while True:
        stdscr.clear()
        stdscr.bkgd(curses.color_pair(1))

        # Display ASCII art
        for line_idx, line in enumerate(ascii_art.split('\n')):
            stdscr.addstr(line_idx, pad_left, line, curses.color_pair(1))
        
        menu_start_position = len(ascii_art.split('\n'))

        # Display menu items below the ASCII art
        for idx, item in enumerate(main_menu_items):
            if idx == current_row:
                stdscr.addstr(pad_top + menu_start_position + idx, pad_left, item["name"], curses.A_REVERSE | curses.color_pair(1))
            else:
                stdscr.addstr(pad_top + menu_start_position + idx, pad_left, item["name"], curses.color_pair(1))

        key = stdscr.getch()
        


        if key == curses.KEY_UP and current_row > 0:
            current_row -= 1
        elif key == curses.KEY_DOWN and current_row < len(main_menu_items) - 1:
            current_row += 1
        elif key == curses.KEY_ENTER or key == 10:  # 10 represents the Enter key
            selected_action = main_menu_items[current_row]["action"]
            if selected_action in action_dispatch:
                action_dispatch[selected_action]()

curses.wrapper(main)