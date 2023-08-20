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
fontSpeed = 10

# Initialize screen and clock
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("JVC 3050 Modernization Prototype")
clock = pygame.time.Clock()

# UI Elements and Variables
font_large = pygame.font.SysFont(None, 48)
font_small = pygame.font.SysFont(None, 36)
pages = ['Home', 'Page 1', 'Page 2', 'Page 3', 'Page 4']
selected_item = 1

def type_out_text(surface, font, text, color, position, speed=fontSpeed):
    """Display text one character at a time at a given speed."""
    typed_text = ''
    x, y = position
    for char in text:
        typed_text += char
        rendered_text = font.render(typed_text, True, color)
        surface.blit(rendered_text, (x, y))
        pygame.display.flip()
        pygame.time.wait(speed)

typed_out = False # This is a flag to indicate whether or not the text has been typed out
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

    # If text hasn't been typed out yet, do it
    if not typed_out:
        for i, page in enumerate(pages[1:], start=1):
            display_text = page

            if i == selected_item:
                display_text =  "/// " + page + " " + SELECTION_INDICATOR

            type_out_text(screen, nostReg, display_text, LIME, (LEFTSPACING + menuPadding, TOPSPACING + menuSpacing + (i - 1) * 40))
        
        typed_out = True  # Set flag to True so we don't type out text again

    # If text has already been typed out, just blit it as usual
    else:
        for i, page in enumerate(pages[1:], start=1):
            display_text = page

            if i == selected_item:
                display_text = "/// " + page + " " + SELECTION_INDICATOR

            text = nostReg.render(display_text, True, LIME)
            screen.blit(text, (LEFTSPACING + menuPadding, TOPSPACING + menuSpacing + (i - 1) * 40))

        #below is the non typed text readout
        #screen.blit(text, (LEFTSPACING + menuPadding, TOPSPACING + menuSpacing + (i - 1) * 40))


    pygame.display.flip()

    clock.tick(30)

pygame.quit()
