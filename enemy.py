import pygame
import math
import os
from settings import PATH

pygame.init()
ENEMY_IMAGE = pygame.image.load(os.path.join("images", "enemy.png"))



class Enemy:
    def __init__(self):
        self.width = 40
        self.height = 50
        self.image = pygame.transform.scale(ENEMY_IMAGE, (self.width, self.height))
        self.health = 5
        self.max_health = 10
        self.path = PATH
        self.path_pos = 0
        self.move_count = 0
        self.stride = 1
        self.x, self.y = self.path[0]


    def draw(self, win):
        # draw enemy
        win.blit(self.image, (self.x - self.width // 2, self.y - self.height // 2))
        # draw enemy health bar
        self.draw_health_bar(win)

    def draw_health_bar(self, win):
        """
        Draw health bar on an enemy
        :param win: window
        :return: None
        """
        #設定紅色血條
        pygame.draw.rect(win, (255, 0, 0),(self.x - self.width // 2, self.y - self.height // 2,40,4))
        #設定綠色血條覆蓋在紅色之上、大小按比例
        pygame.draw.rect(win, (0,224, 0), (self.x - self.width // 2, self.y - self.height // 2, 40//self.max_health*self.health, 4))


    def move(self):
        """
        Enemy move toward path points every frame
        :return: None
        """
        #第一個位置
        ax, ay = self.path[self.path_pos]
        #第二個位置
        bx, by = self.path[self.path_pos+1]
        distance_A_B = math.sqrt((ax - bx)**2 + (ay - by)**2)
        max_count = int(distance_A_B / self.stride)  # total footsteps that needed from A to B

        if self.move_count < max_count:
            unit_vector_x = (bx - ax) / distance_A_B
            unit_vector_y = (by - ay) / distance_A_B
            delta_x = unit_vector_x * self.stride
            delta_y = unit_vector_y * self.stride

        # update the coordinate and the counter
            self.x += delta_x
            self.y += delta_y
            self.move_count += 1
        else:
            self.path_pos+=1
            self.move_count=0



class EnemyGroup:
    def __init__(self):
        self.gen_count = 0
        self.gen_period = 120   # (unit: frame)
        self.reserved_members = []
        self.expedition = [Enemy()]  # don't change this line until you do the EX.3 

    def campaign(self):
        """
        Send an enemy to go on an expedition once 120 frame
        :return: None
        """

        # Hint: self.expedition.append(self.reserved_members.pop())
        # ...(to be done)
        #if not self.is_empty() and self.gen_count == self.gen_period:
         #       self.expedition.append(self.reserved_members.pop())
          #      self.gen_count = 0
           # else:
            #    self.gen_count += 1
        pass

    def generate(self, num):
        """
        Generate the enemies in this wave
        :param num: enemy number
        :return: None
        """
        # ...(to be done)
        pass

    def get(self):
        """
        Get the enemy list
        """
        return self.expedition

    def is_empty(self):
        """
        Return whether the enemy is empty (so that we can move on to next wave)
        """
        return False if self.reserved_members else True

    def retreat(self, enemy):
        """
        Remove the enemy from the expedition
        :param enemy: class Enemy()
        :return: None
        """
        self.expedition.remove(enemy)





