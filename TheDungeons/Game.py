import pygame
import os
import sys

from GUI.config import *
from GUI.Characters import Knight, Princess
from GUI.Obstacles import Ground, Border, Wall
from GUI.Input import Button, Text_Input

from problem import Problem
from BFS import BFS
from ASTAR import ASTAR
from helper import resource_path

class SpriteSheet:
    def __init__(self, png_file):
        dirname = os.path.dirname(__file__)
        file = os.path.join(dirname, png_file)
        
        asset_url = resource_path(file)
        self.sheet = pygame.image.load(asset_url).convert()
    
    def get_sprite(self, x, y, width, height):
        sprite = pygame.Surface( [width, height] )
        sprite.set_colorkey(BLACK)
        
        sprite.blit(self.sheet, (0,0), (x, y, width, height))
        sprite = pygame.transform.scale(sprite, (WIN_WIDTH, WIN_HEIGHT))
        return sprite

class Screen:
    def __init__(self, title, width, height, fill=BLACK):
        self.title = title
        self.width = width
        self.height = height
        self.fill = fill
        self.current = False

    def make_current(self):
        pygame.display.set_caption(self.title)
        self.current = True
        self.screen = pygame.display.set_mode( (self.width, self.height) )
    
    def end_current(self):
        self.current = False

    def update(self):
        if self.current:
            self.screen.fill(self.fill)

class Game:
    def __init__(self):
        pygame.init()

        
        self.menue_width = MIN_WIDTH
        self.menue_height = MIN_HEIGHT

        self.menue_screen = Screen('Menue', self.menue_width, self.menue_height)
        self.menue_screen.make_current()
        self.screen = self.menue_screen.screen 

        self.clock = pygame.time.Clock()
       
        self.background = pygame.image.load(resource_path('./GUI/assets/intro.png'))
        self.knight_sprite = SpriteSheet(resource_path('./GUI/assets/knight.png'))
        self.princess_sprite = SpriteSheet(resource_path('./GUI/assets/princess.png'))
        self.game_sprite = SpriteSheet(resource_path('./GUI/assets/all.png'))
        
        self.running = True
        self.font = pygame.font.Font(resource_path('./GUI/assets/fonts/Arial.ttf'), 18)

    def init_problem(self, file):
        self.problem = Problem(file)
        self.map = self.problem.map
        self.border = self.problem.border

        self.screen_width = (self.problem.N + 1) * WIN_WIDTH
        self.screen_height = (self.problem.M + 1) * WIN_HEIGHT
     
        self.game_screen = Screen('The Dungeon', self.screen_width, self.screen_height)
        self.create_tile_map()
        self.create_border()

    def create_tile_map(self):
        for i, row in enumerate(self.map):
            for j, col in enumerate(row):
                if col == 'K':
                    Ground(self, j, i)
                    self.knight = Knight(self, j, i)

                elif col == 'P':
                    Ground(self, j, i)
                    Princess(self, j, i)

                elif col == 'X':
                    Ground(self, j, i)
                    Wall(self, j, i)

                elif col == '.':
                    Ground(self, j, i)

    def create_border(self):
        for i, row in enumerate(self.border):
                for j, col in enumerate(row):
                    Border(self, j, i)
        
    def new(self):
        self.playing = True
        self.all_sprites = pygame.sprite.LayeredUpdates()
        self.wall = pygame.sprite.LayeredUpdates()

    def event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False

    def update(self):
        self.all_sprites.update()

    def draw(self):
        self.game_screen.make_current()
        self.screen = self.game_screen.screen

        self.screen.fill(BLACK)
        self.all_sprites.draw(self.screen)
        self.clock.tick(FPS)
        pygame.display.update()

    def main(self):
        while self.playing:
            self.event()
            self.update()
            self.draw()
            if len(self.knight.path) == 0 or isinstance(self.knight.path, str):
                self.playing = False

    def end(self):
        Back_button = Button(WIN_WIDTH, self.game_screen.height-WIN_HEIGHT, 60, WIN_WIDTH, BLACK, GREEN, PINK_HV, 'Back', 16)
        
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            
            mouse_pos = pygame.mouse.get_pos()
            mouse_pressed = pygame.mouse.get_pressed()

            Back_button.on_hover(mouse_pos)

            if Back_button.is_pressed(mouse_pos, mouse_pressed):
                for sprite in self.all_sprites:
                    sprite.kill()

                self.new()
                self.intro()
                self.main()

            self.screen.blit(Back_button.image, Back_button.rect)
            self.clock.tick(60)
            pygame.display.update()

    def intro(self):
        self.menue_screen.make_current()
        self.screen = self.menue_screen.screen

        intro = True
        title = self.font.render('The Dungeon', True, BLACK)
      
        title_rect = title.get_rect()

        title_rect.centerx = self.menue_width//2  
        title_rect.top = 8  
        center = self.menue_width//2
        BFS_button = Button(center, WIN_HEIGHT+4 + title_rect.top, 70, 32, BLACK, PINK, GREEN_HV, 'BFS', 16)
        ASTAR_button = Button(center, WIN_HEIGHT-6 + title_rect.top*8, 70, 32, BLACK, PINK, GREEN_HV, 'A*', 16)
        obst_input = Text_Input(center, center + (WIN_HEIGHT + 20), 30, 32, GREEN_HV, PINK, BLACK, YELLOW, self, '0')
        file_input = Text_Input(center, center + (WIN_HEIGHT + 60), 120, 32, GREEN_HV, PINK, BLACK, YELLOW, self, 'data/test.txt')

        while intro:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    intro = False
                    self.running = False
                
                if event.type == pygame.KEYDOWN:
                    if file_input.active:
                        if event.key == pygame.K_BACKSPACE:
                            file_input.input = file_input.input[:-1]
                        else:
                            file_input.input += event.unicode
                    if obst_input.active:
                        if event.key == pygame.K_BACKSPACE:
                            obst_input.input = obst_input.input[:-1]
                        else:
                            if event.unicode.isdigit() and len(obst_input.input) < 2:
                                obst_input.input += event.unicode
            
            mouse_pos = pygame.mouse.get_pos()
            mouse_pressed = pygame.mouse.get_pressed()

            BFS_button.on_hover(mouse_pos)
            ASTAR_button.on_hover(mouse_pos)
            
            if BFS_button.is_pressed(mouse_pos, mouse_pressed):
                self.init_problem(file_input.input)
                self.knight.path = BFS(self.problem, int(obst_input.input) )
                self.menue_screen.end_current()
                intro = False

            elif ASTAR_button.is_pressed(mouse_pos, mouse_pressed):
                self.init_problem(file_input.input)
                self.knight.path = ASTAR(self.problem, int(obst_input.input) )
                self.menue_screen.end_current()
                intro = False

            
            self.screen.blit(self.background, (0,0))
            self.screen.blit(title, title_rect)
            self.screen.blit(ASTAR_button.image, ASTAR_button.rect)
            self.screen.blit(BFS_button.image, BFS_button.rect)
            self.clock.tick(60)
            file_input.draw_input()
            obst_input.draw_input()
            pygame.display.update()

g = Game()
g.new()
g.intro()

while g.running:
    g.main()
    g.end()
    
pygame.quit()
sys.exit()