import os
import pygame
from pygame.sprite import Sprite
from dino_runner.utils.constants import RAGE_BAR
from dino_runner.components.obstacles.obstacle_manager import ObstacleManager
from dino_runner.components.dinosaur import Dinosaur
from dino_runner.components.obstacles.obstacle import Obstacle
class Rage(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.IMAGEM_RAGE = []
        for i in range(5):
            img = RAGE_BAR.subsurface((i * 32, 0), (32,32))
            img = pygame.transform.scale(img, (32*20, 32*7))
            self.IMAGEM_RAGE.append(img)
        self.index_lista = 0
        self.image = self.IMAGEM_RAGE[self.index_lista]
        self.rect = self.image.get_rect()
        self.start_time = 0
        self.duration = 6
    

    def update(self, user_input):
        if user_input[pygame.K_f]:
            self.index_lista += 1
        if self.index_lista == 5:
            self.index_lista = 0
        self.image = self.IMAGEM_RAGE[int(self.index_lista)]


    def draw(self, screen):
        screen.blit(self.image, (180, 450))