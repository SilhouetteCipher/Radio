import time
import curses
import json
import navigation

delay = 0.1

def internet_radio():
    # Code to handle Internet Radio action
    header_art = load_ascii_art("headers/radio.txt")
    with open('menu.json', 'r') as file:
        menu_data = json.load(file)
        main_menu_items = menu_data["internet_radio"]

    action_dispatch = {
    "internet_radio": internet_radio,
    "spotify": spotify,
    "casting": casting,
    "podcasts": podcasts,
    "exit_program": exit,
    "back": back
}

    navigation.setup_screen(5, 10, 5, header_art, 5, 0, main_menu_items, action_dispatch)
    return



def spotify():
    # Code to handle Spotify action
    header_art = load_ascii_art("headers/spotify.txt")
    with open('menu.json', 'r') as file:
        menu_data = json.load(file)
        main_menu_items = menu_data["spotify"]

    action_dispatch = {
    "internet_radio": internet_radio,
    "spotify": spotify,
    "casting": casting,
    "podcasts": podcasts,
    "exit_program": exit,
    "back": back
}
    navigation.setup_screen(5, 10, 5, header_art, main_menu_items, action_dispatch)


    pass

def casting():
    # Code to handle Casting action
    pass

def podcasts():
    # Code to handle Podcasts action
    pass

def load_ascii_art(filename):
    # Load the ASCII art from the file
    with open(filename, 'r') as file:
        return file.read()

# define a empty function called back
def back():
    # Code to handle Back action in my curse menu structure
    pass


def type_out(stdscr, y, x, text, color=None, delay=0.01):
    for char in text:
        if color:
            stdscr.addch(y, x, char, color)
        else:
            stdscr.addch(y, x, char)
        x += 1  # move the x-coordinate for the next character
        stdscr.refresh()  # update the screen
        time.sleep(delay)  # introduce a delay