import pygame as pg

# define some colours (R, G, B)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
DARKGREY = (40, 40, 40)
CASTELLION_BG = (249, 236, 188)
LIGHTGREY = (100, 100, 100)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
PURPLE = (92, 60, 102)
CYAN = (224, 255, 255)
ORANGE = (172, 101, 50)

# More custom colours
YELLOW_BROWN = (226, 167, 27)
BROWN = (139, 69, 19)

# game settings
WIDTH = 1081 # 16 * 64 or 32 * 32 or 64 * 16
HEIGHT = 811  # 16 * 48 or 32 * 24 or 64 * 12
FPS = 60
TITLE = "Castellion v1.0.0"
BGCOLOUR = PURPLE


pg.font.init()
FONT = pg.font.Font('freesansbold.ttf', 16)

FONT2 = pg.font.Font('freesansbold.ttf', 72)

BACKGROUND = pg.Surface((600,  600))
BACKGROUND.fill(PURPLE)
BACKGROUND_RECT = BACKGROUND.get_rect()
BACKGROUND_RECT.center = (WIDTH/2, HEIGHT/2)

FADE_TO_BLACK = pg.Surface((1081, 811))
FADE_TO_BLACK2 = pg.Surface((1081, 200))
FADE_TO_BLACK3 = pg.Surface((1081, 411))
FADE_TO_BLACK4 = pg.Surface((270, 200))
FADE_TO_BLACK5 = pg.Surface((271, 200))
FADE_TO_BLACK.fill(BLACK)
FADE_TO_BLACK.set_alpha(128)
FADE_TO_BLACK_RECT = FADE_TO_BLACK2.get_rect()
FADE_TO_BLACK2.fill(BLACK)
FADE_TO_BLACK2.set_alpha(128)
FADE_TO_BLACK_RECT2 = FADE_TO_BLACK2.get_rect()
FADE_TO_BLACK3.fill(BLACK)
FADE_TO_BLACK3.set_alpha(128)
FADE_TO_BLACK_RECT3 = FADE_TO_BLACK3.get_rect()
FADE_TO_BLACK4.fill(BLACK)
FADE_TO_BLACK4.set_alpha(128)
FADE_TO_BLACK_RECT4 = FADE_TO_BLACK4.get_rect()
FADE_TO_BLACK5.fill(BLACK)
FADE_TO_BLACK5.set_alpha(128)
FADE_TO_BLACK_RECT5 = FADE_TO_BLACK5.get_rect()


NEW_BORDER = 'new_border.png'

WINDOW = 'window-1.png'
WINDOW2 = 'window2-1.png'

MAIN = 'castellion.png'
TOP_BAR = 'top_bar1.png'

# Cards
CARD1 = 'card1.png'
CARD2 = 'card2.png'
CARD3_1 = 'card3-1.png'
CARD3_2 = 'card3-2.png'
CARD3_3 = 'card3-3.png'

# Buttons
DISCARD_BUTTON = 'discard_button.png' #
DRAW_BUTTON = 'draw_button.png' #
DREAM_TILE_BUTTON = 'dreamtile_button.png' #
HOME_BUTTON = 'home_button.png'
RESTART_BUTTON = 'restart_button.png'
ORDEAL_BUTTON = 'ordeal_button.png' #
QUIT_BUTTON = 'quit_button.png'
STATS_BUTTON = 'stats_button.png'

SCROLL = 'scroll.png'

TILESIZE = 90
GRIDWIDTH = WIDTH / TILESIZE
GRIDHEIGHT = HEIGHT / TILESIZE

TRAITOR_TILE = 'traitor.png'

CHAMELEON_CIRCLE = 'chameleoncircle.png'
CHAMELEON_TRIANGLE = 'chameleontriangle.png'
CHAMELEON_SQUARE = 'chameleonsquare.png'

SEER_CIRCLE = 'seercircle.png'
SEER_TRIANGLE = 'seertriangle.png'
SEER_SQUARE = 'seersquare.png'

PYRO_CIRCLE = 'pyrocircle.png'
PYRO_TRIANGLE = 'pyrotriangle.png'
PYRO_SQUARE = 'pyrosquare.png'

JUGGLER_CIRCLE = 'jugglercircle.png'
JUGGLER_TRIANGLE = 'jugglertriangle.png'
JUGGLER_SQUARE = 'jugglersquare.png'

# Load dream tile images

DREAM_CHAMELEON_CIRCLE = 'dream_chameleoncircle.png'
DREAM_CHAMELEON_TRIANGLE = 'dream_chameleontriangle.png'
DREAM_CHAMELEON_SQUARE = 'dream_chameleonsquare.png'

DREAM_SEER_CIRCLE = 'dream_seercircle.png'
DREAM_SEER_TRIANGLE = 'dream_seertriangle.png'
DREAM_SEER_SQUARE = 'dream_seersquare.png'

DREAM_PYRO_CIRCLE = 'dream_pyrocircle.png'
DREAM_PYRO_TRIANGLE = 'dream_pyrotriangle.png'
DREAM_PYRO_SQUARE = 'dream_pyrosquare.png'

DREAM_JUGGLER_CIRCLE = 'dream_jugglercircle.png'
DREAM_JUGGLER_TRIANGLE = 'dream_jugglertriangle.png'
DREAM_JUGGLER_SQUARE = 'dream_jugglersquare.png'


MINION = 'mob1.png'
MINION2 = 'mob2.png'
MINION3 = 'mob3.png'

# Minion animation
DEATH1 = 'mob_death1.png'
DEATH2 = 'mob_death2.png'
DEATH3 = 'mob_death3.png'
DEATH4 = 'mob_death4.png'

LINE = 'line.png'
BASTION = 'bastion.png'
TOWER = 'tower.png'

# Load some background images
LEFT_BAR = 'leftside.png'
LEFT_FIRST = 'leftfirst.png'
RIGHT_BAR = 'right_bar.png'

# Second ordeal images
SLASH = 'crossed_out.png'

SEER1_HIT_RECT = pg.Rect(0, 0, 35, 35)
