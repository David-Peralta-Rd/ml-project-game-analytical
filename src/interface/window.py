import pygame
import sys


pygame.init()

GAME_RESOLUTIONS = {
    "3840x2160": (3840, 2160),
    "2560x1140": (2560, 1140),
    "1920x1080": (1920, 1080),
    "1280x720": (1280, 720),
    "854x480": (854, 480),
    "640x480": (640, 480),
}

RESOLUTION = GAME_RESOLUTIONS["854x480"]

GAME_SCREEN = pygame.display.set_mode(RESOLUTION)
GAME_TITLE = pygame.display.set_caption("Primer Juego")
GAME_CLOCK = pygame.time.Clock()


option_color = {
    "RED": pygame.Color('red'),
    "WHITE": pygame.Color('white'),
    "BLACK": pygame.Color('black'),
    "DARK_GREY": pygame.Color(30, 30, 30)
}

DISPLAY_COLOR = option_color["DARK_GREY"]


class WindowConfig:
    def __init__(self) -> None:
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            GAME_SCREEN.fill(DISPLAY_COLOR)
            pygame.display.flip()
            GAME_CLOCK.tick(60)



WindowConfig()
