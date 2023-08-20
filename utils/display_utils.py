import pygame
fontSpeed = 10


def type_out_text(surface, font, text, color, position, fontSpeed):
    """Display text one character at a time at a given speed."""
    typed_text = ''
    x, y = position
    for char in text:
        typed_text += char
        rendered_text = font.render(typed_text, True, color)
        surface.blit(rendered_text, (x, y))
        pygame.display.flip()
        pygame.time.wait(fontSpeed)
