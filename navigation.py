import curses
import time
import curses
import json



def handle_navigation(key, current_row, max_rows, action_dispatch, menu_items):
    if key == curses.KEY_UP and current_row > 0:
        current_row -= 1
    elif key == curses.KEY_DOWN and current_row < max_rows - 1:
        current_row += 1
    elif key in [curses.KEY_ENTER, 10]: 
        selected_action = menu_items[current_row]["action"]
        if selected_action in action_dispatch:
            action_dispatch[selected_action]()
    
    return current_row


# function to setup the basic screen
def setup_screen(padding_top, padding_left, menu_start_position, header_art, x, y, main_menu_items, action_dispatch):
    import handlers
    def main(stdscr):
        # menu drawn bool so only runs once
        menu_drawn = False
        diag_drawn = False
        curses.start_color()
        curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
        curses.curs_set(0)
        current_row = 0

        while True:
            stdscr.clear()
            stdscr.bkgd(curses.color_pair(1))

            # Display the ASCII art at the very top, iterate line so the whole graphic shifts
            for i, line in enumerate(header_art.splitlines()):
                stdscr.addstr(y + i, x, line)

            # Display menu items below the ASCII art
            if not menu_drawn:
                for idx, item in enumerate(main_menu_items):
                    if idx == current_row:
                        handlers.type_out(stdscr, padding_top + menu_start_position + idx, padding_left, item["name"], curses.A_REVERSE | curses.color_pair(1))
                    else:
                        handlers.type_out(stdscr, padding_top + menu_start_position + idx, padding_left, item["name"], curses.color_pair(1))
                menu_drawn = True
            else:
                for idx, item in enumerate(main_menu_items):
                    if idx == current_row:
                        stdscr.addstr(padding_top + menu_start_position + idx, padding_left, item["name"], curses.A_REVERSE | curses.color_pair(1))
                    else:
                        stdscr.addstr(padding_top + menu_start_position + idx, padding_left, item["name"], curses.color_pair(1))

            # Display fake diagnostic text in the second column
            if not diag_drawn:
                diagnostic_start_x = padding_left + 20  # Adjust the starting x-coordinate as needed
                handlers.type_out(stdscr, padding_top + menu_start_position, diagnostic_start_x, "| System Info", 1)
                handlers.type_out(stdscr, padding_top + menu_start_position + 1, diagnostic_start_x, "| CPU: 23%", 1)
                handlers.type_out(stdscr, padding_top + menu_start_position + 2, diagnostic_start_x, "| RAM: 1.2 GB", 1)
                handlers.type_out(stdscr, padding_top + menu_start_position + 3, diagnostic_start_x, "| NET: UP", 1)
                diag_drawn = True
            else:
                diagnostic_start_x = padding_left + 20  # Adjust the starting x-coordinate as needed
                stdscr.addstr(padding_top + menu_start_position, diagnostic_start_x, "| System Info", curses.color_pair(1))
                stdscr.addstr(padding_top + menu_start_position + 1, diagnostic_start_x, "| CPU: 23%", curses.color_pair(1))
                stdscr.addstr(padding_top + menu_start_position + 2, diagnostic_start_x, "| RAM: 1.2 GB", curses.color_pair(1))
                stdscr.addstr(padding_top + menu_start_position + 3, diagnostic_start_x, "| NET: UP", curses.color_pair(1))

            key = stdscr.getch()
            current_row = handle_navigation(key, current_row, len(main_menu_items), action_dispatch, main_menu_items)

    curses.wrapper(main)
