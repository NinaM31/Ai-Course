import pygame

from helper import resource_path
class Button:
    def __init__(self, x, y, width, height, fg, bg, hbg, content, fontsize):
        self.font = pygame.font.Font(resource_path('./GUI/assets/fonts/Arial.ttf'), fontsize)
        self.content = content

        self.x = x
        self.y = y 

        self.width = width
        self.height = height

        self.fg = fg
        self.bg = bg
        self.hbg = hbg

        self.image = pygame.Surface((self.width, self.height))
        self.image.fill(self.bg)

        self.rect = self.image.get_rect()  
        self.rect.centerx = self.x
        self.rect.y = self.y   

        self.text = self.font.render(self.content, True, self.fg)
        self.text_rect = self.text.get_rect( center=(self.width/2, self.height/2) ) 
        self.image.blit(self.text, self.text_rect)  

    def on_hover(self, pos):
        if self.rect.collidepoint(pos):
            self.image.fill(self.hbg)
        else:
            self.image.fill(self.bg)
        self.image.blit(self.text, self.text_rect) 

    def is_pressed(self, pos, pressed):
        if self.rect.collidepoint(pos):
            if pressed[0]:
                return True
            return False
        return False

class Text_Input:
    def __init__(self, x, y, width, height, actv, pasv, fg, bg, game, holder):
        self.font = game.font
        self.input_rect = pygame.Rect(0, y, width, height)
        self.input_rect.centerx = x
        self.input = holder
        self.game = game
        self.active = False
        self.color_active = actv
        self.color_passive = pasv
        self.game = game
        self.fg = fg
        self.bg = bg
 
    def draw_input(self):
        pos = pygame.mouse.get_pos()

        if self.input_rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1:
                self.active = True

        elif pygame.mouse.get_pressed()[0] == 1:
            self.active = False

        if self.active:
            color = self.color_active 
        else:
            color = self.color_passive

        pygame.draw.rect(self.game.screen, self.bg, self.input_rect)
        pygame.draw.rect(self.game.screen, color, self.input_rect, 3)
        
        text_surface = self.font.render(self.input, True, self.fg)
        self.game.screen.blit(text_surface,  (self.input_rect.x + 10, self.input_rect.y + 5))
