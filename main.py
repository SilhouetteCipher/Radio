import pygame
import json
from utils.display_utils import type_out_text, fontSpeed
# Import your page functions when you've defined them, e.g.:
# from pages.home_page import home_function

pygame.init()

# Constants and Variables Initialization
# Window dimensions
WIDTH, HEIGHT = 720, 720

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
LIME = (50, 205, 50)
SELECTION_BG = LIME
SELECTION_INDICATOR = "/////////////////////////////////////"

# Alignment variables
LEFTSPACING = 20 # Padding from left side of screen to text for titles
TOPSPACING = 40 # Padding from top of screen to text for titles
menuPadding = 60 # Padding from left side of screen to menu text
menuSpacing = 40 # Spacing between menu items
menuFirstItem = 60 # Vertical position of first menu item

# Fonts
largeFontSize = 90
smallFontSize = 20
nostOutline = pygame.font.Font('fonts/Outline/nostOutline.otf', largeFontSize)
nostReg = pygame.font.Font('fonts/Alien/nostReg.otf', smallFontSize)


# Screen and Clock Initialization
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("JVC 3050 Modernization Prototype")
clock = pygame.time.Clock()

# Loading menu from JSON
with open('menu.json', 'r') as file:
    menu = json.load(file)

selected_item = 1
typed_out = False

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Navigate using up and down arrow keys
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN and selected_item < len(menu) - 1:
                selected_item += 1
            elif event.key == pygame.K_UP and selected_item > 1:
                selected_item -= 1

    screen.fill(BLACK)

    # Draw the page title (always at top)
    text_title = nostOutline.render(menu[0]["title"], True, LIME)
    screen.blit(text_title, (LEFTSPACING, TOPSPACING + 20 - text_title.get_height()/2))

    # Check if text has been typed out
    if not typed_out:
        for i, page in enumerate(menu[1:], start=1):
            display_text = page["title"]

            if i == selected_item:
                display_text =  "/// " + page["title"] + " " + SELECTION_INDICATOR

            type_out_text(screen, nostReg, display_text, LIME, (LEFTSPACING + menuPadding, menuFirstItem + menuSpacing + (i - 1) * menuSpacing), fontSpeed)
        
        typed_out = True

    # If text has been typed out, display normally
    else:
        for i, page in enumerate(menu[1:], start=1):
            display_text = page["title"]

            if i == selected_item:
                display_text = "/// " + page["title"] + " " + SELECTION_INDICATOR

            text = nostReg.render(display_text, True, LIME)
            screen.blit(text, (LEFTSPACING + menuPadding, menuFirstItem + menuSpacing + (i - 1) * menuSpacing))

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
