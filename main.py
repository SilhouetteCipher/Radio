import pygame

pygame.init()

# Window dimensions
WIDTH, HEIGHT = 720, 720

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
LIME = (50, 205, 50)
SELECTION_BG = LIME

SELECTION_INDICATOR = "/////////////////////////////////////"

# alinment variables
LEFTSPACING = 20
TOPSPACING = 40
menuPadding = 60
menuSpacing = 80

# import a font from a directory and load it
largeFontSize = 90
smallFontSize = 20
nostOutline = pygame.font.Font('fonts/Outline/nostOutline.otf', largeFontSize)
nostReg = pygame.font.Font('fonts/Alien/nostReg.otf', smallFontSize)



# Initialize screen and clock
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("JVC 3050 Modernization Prototype")
clock = pygame.time.Clock()

# UI Elements and Variables
font_large = pygame.font.SysFont(None, 48)
font_small = pygame.font.SysFont(None, 36)
pages = ['Home', 'Page 1', 'Page 2', 'Page 3', 'Page 4']
selected_item = 1


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Navigate using up and down arrow keys
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN and selected_item < len(pages) - 1:
                selected_item += 1
            elif event.key == pygame.K_UP and selected_item > 1:
                selected_item -= 1

    screen.fill(BLACK)

    # Draw UI elements
    # Draw the page title (always at top)
    text_title = nostOutline.render(pages[0], True, LIME)
    screen.blit(text_title, (LEFTSPACING, TOPSPACING + 20 - text_title.get_height()/2))

    # Draw other pages below the title


# Inside your main loop where you draw the pages
    for i, page in enumerate(pages[1:], start=1):
        display_text = page  # Default text to display is just the page name

    # If this is the selected item, prepend and append the selection slashes
        if i == selected_item:
            display_text = "/ " + page + " " + SELECTION_INDICATOR

        text = nostReg.render(display_text, True, LIME)
        screen.blit(text, (LEFTSPACING + menuPadding, TOPSPACING + menuSpacing + (i - 1) * 40))


    pygame.display.flip()

    clock.tick(30)

pygame.quit()
