import pygame

pygame.init()

# Window dimensions
WIDTH, HEIGHT = 720, 720

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
SELECTION_BG = (100, 100, 100)

# alinment variables
LEFTSPACING = 10
TOPSPACING = 10

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
    text_title = font_large.render(pages[0], True, WHITE)
    screen.blit(text_title, (LEFTSPACING, TOPSPACING + 20 - text_title.get_height()/2))

    # Draw other pages below the title
    for i, page in enumerate(pages[1:], start=1):
        if i == selected_item:
            text_bg = pygame.Surface((WIDTH, font_small.get_height()))
            text_bg.fill(SELECTION_BG)
            screen.blit(text_bg, (0, TOPSPACING + 50 + (i - 1) * 40))
            
            text = font_small.render(page, True, BLACK, SELECTION_BG)
        else:
            text = font_small.render(page, True, WHITE)
        
        screen.blit(text, (LEFTSPACING, TOPSPACING + 50 + (i - 1) * 40))

    pygame.display.flip()

    clock.tick(30)

pygame.quit()
