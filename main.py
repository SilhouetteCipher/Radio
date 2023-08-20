import curses
import json
from handlers import internet_radio, spotify, casting, podcasts, load_ascii_art, type_out


# Load the JSON menu
with open('menu.json', 'r') as file:
    menu_data = json.load(file)
    main_menu_items = menu_data["main_menu"]

# Define some padding
pad_top = 5
pad_left = 10
menu_start_position = 5




# The dispatch table mapping action names to functions
action_dispatch = {
    "internet_radio": internet_radio,
    "spotify": spotify,
    "casting": casting,
    "podcasts": podcasts,
    "exit_program": exit
}

header_art = load_ascii_art("header.txt")


def main(stdscr):
    #menu drawn bool so only runs once
    menu_drawn = False
    diag_drawn = False
    curses.start_color()
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.curs_set(0)
    current_row = 0

    while True:
        stdscr.clear()
        stdscr.bkgd(curses.color_pair(1))

        # Display the ASCII art at the very top
        stdscr.addstr(0, 0, header_art)
        
        

        # Display menu items below the ASCII art
        if not menu_drawn:
            for idx, item in enumerate(main_menu_items):
                if idx == current_row:
                    type_out(stdscr, pad_top + menu_start_position + idx, pad_left, item["name"], curses.A_REVERSE | curses.color_pair(1))
                else:
                    type_out(stdscr, pad_top + menu_start_position + idx, pad_left, item["name"], curses.color_pair(1))
            menu_drawn = True
        else:
            for idx, item in enumerate(main_menu_items):
                if idx == current_row:
                    stdscr.addstr(pad_top + menu_start_position + idx, pad_left, item["name"], curses.A_REVERSE | curses.color_pair(1))
                else:
                    stdscr.addstr(pad_top + menu_start_position + idx, pad_left, item["name"], curses.color_pair(1))

        # Display fake diagnostic text in the second column
        if not diag_drawn:
            diagnostic_start_x = pad_left + 20  # Adjust the starting x-coordinate as needed
            type_out(stdscr, pad_top + menu_start_position, diagnostic_start_x, "| System Info", 1)
            type_out(stdscr, pad_top + menu_start_position + 1, diagnostic_start_x, "| CPU: 23%", 1)
            type_out(stdscr, pad_top + menu_start_position + 2, diagnostic_start_x, "| RAM: 1.2 GB", 1)
            type_out(stdscr, pad_top + menu_start_position + 3, diagnostic_start_x, "| NET: UP", 1)
            diag_drawn = True
        else:
            diagnostic_start_x = pad_left + 20  # Adjust the starting x-coordinate as needed
            stdscr.addstr(pad_top + menu_start_position, diagnostic_start_x, "System Info", curses.color_pair(1))
            stdscr.addstr(pad_top + menu_start_position + 1, diagnostic_start_x, "CPU: 23%", curses.color_pair(1))
            stdscr.addstr(pad_top + menu_start_position + 2, diagnostic_start_x, "RAM: 1.2 GB", curses.color_pair(1))
            stdscr.addstr(pad_top + menu_start_position + 3, diagnostic_start_x, "NET: UP", curses.color_pair(1))
            

# Wait for user input


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