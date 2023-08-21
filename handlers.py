import time
delay = 0.1

def internet_radio():
    # Code to handle Internet Radio action
    pass

def spotify():
    # Code to handle Spotify action
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