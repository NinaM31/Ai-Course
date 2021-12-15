import pygame
import math

from GUI.config import *

class Knight(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self.path = []
        
        self._layer = KNIGHT_LAYER
        self.groups = self.game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x * TILESIZE
        self.y = y * TILESIZE

        self.facing = 'down'
        self.animation_loop = 0

        self.image = self.game.knight_sprite.get_sprite(3, 0, TILESIZE, TILESIZE)

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y


    def update(self):
        self.movement()
        self.collide()

    def movement(self):
        if isinstance(self.path, str): return
        if len(self.path) == 0: return 

        move = self.path.pop(0)
        self.rect.x = move[1] * TILESIZE
        self.rect.y = move[0] * TILESIZE

    def collide(self):
        hits = pygame.sprite.spritecollide(self, self.game.wall, True)
       

class Princess(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self._layer = PRINCESS_LAYER
        self.groups = self.game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x * TILESIZE
        self.y = y * TILESIZE

        self.x_change = 0
        self.y_change = 0

        self.animation_loop = 0
        self.image = self.game.princess_sprite.get_sprite(3, 34, TILESIZE, TILESIZE)

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    def update(self):
        pass        