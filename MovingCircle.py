import os
import pygame
import sys
import time
import Tkinter as tk
from PIL import Image, ImageTk


class Game:

    def __init__(self):
        self.parent = tk.Tk()
        self.screen_width = self.parent.winfo_screenwidth()
        self.screen_height = self.parent.winfo_screenheight()

        self.canvas = tk.Canvas(self.parent, width=500, height=500)
        self.x = 250
        self.y=250
        self.r = 20
        self.circle = ImageTk.PhotoImage(Image.open("resources/images/circle.jpg"))
        self.canvas.create_image(self.x, self.y, image=self.circle)
        self.canvas.pack()
        self.parent.update_idletasks()


    def moveThing(self, direction):
        moveconst = 25
        if direction == 0 :
            self.y -= moveconst
        if direction == 1:
            self.x += moveconst
        if direction == 2:
            self.y += moveconst
        if direction == 3:
            self.x -= moveconst
        self.canvas.delete('all')
        self.canvas.create_image(self.x, self.y, image=self.circle)
        self.canvas.pack()
        self.parent.update_idletasks()

    def resetPosition(self):
        self.x = 250
        self.y=250
        self.canvas.delete('all')
        self.canvas.create_image(self.x, self.y, image=self.circle)
        self.canvas.pack()
        self.parent.update_idletasks()


#def moveThing(self, direction):
    #     #direction: 0=up 1=right 2=down 3=left
    #     #initialize force variables
    #     moveconst = 1
    #
    #     if direction == 0 :
    #         #apply upward force (-y)
    #         self.move_u = moveconst
    #     if direction == 1:
    #         #apply rightward force (+x)
    #         self.move_r = moveconst
    #     if direction == 2:
    #         #apply downward force (+y)
    #         self.move_d = moveconst
    #     if direction == 3:
    #         #apply leftward force (-x)
    #         self.move_l = moveconst
    #     #
    #     # if event.key == pygame.K_UP  or event.key == pygame.K_w:
    #     #     self.move_u = 0
    #     # if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
    #     #     self.move_r = 0
    #     # if event.key == pygame.K_DOWN or event.key == pygame.K_s:
    #     #     self.move_d = 0
    #     # if event.key == pygame.K_LEFT or event.key == pygame.K_a:
    #     #     self.move_l = 0
    #
    #     if(self.move_u == 1 or self.move_d == 1):
    #         if(self.move_u == moveconst and self.move_d == moveconst):
    #             self.move_y = 0
    #         elif(self.move_u == moveconst):
    #             self.move_y = -moveconst
    #         else:
    #             self.move_y = moveconst
    #     else:
    #         self.move_y = 0
    #
    #     if(self.move_r == moveconst or self.move_l == moveconst):
    #         if(self.move_r == moveconst and self.move_l == moveconst):
    #             self.move_x = 0
    #         elif(self.move_r == moveconst):
    #             self.move_x = moveconst
    #         else:
    #             self.move_x = -moveconst
    #     else:
    #         self.move_x = 0
    #
    #     diff_x = self.usr_entity.x - self.anchor_x
    #     diff_y = self.usr_entity.y - self.anchor_y
    #
    #     #set entity velocity
    #     if(self.move_x == 0):
    #         #reset x to anchor
    #         if(abs(diff_x) > 120 / self.FRAMERATE):
    #             if(diff_x < 0):
    #                 return_v_x = 120 / self.FRAMERATE
    #             else:
    #                 return_v_x = -120 / self.FRAMERATE
    #         else:
    #             return_v_x = -1 * (diff_x % (120 / self.FRAMERATE))
    #         self.usr_entity.v_x = return_v_x
    #     else:
    #         self.usr_entity.v_x = (self.move_x * 60 / self.FRAMERATE)
    #         #do boundary check
    #         if(self.move_r == moveconst and diff_x > self.WIN_WIDTH // 2 - self.WIN_WIDTH // 8 + self.usr_entity.size // 2):
    #             self.usr_entity.v_x = 0
    #         if(self.move_l == moveconst and diff_x < (-1 * (self.WIN_WIDTH // 2 - self.WIN_WIDTH // 8) - self.usr_entity.size // 2)):
    #             self.usr_entity.v_x = 0
    #     if(self.move_y == 0):
    #         #reset x to anchor
    #         if(abs(diff_y) > 120 / self.FRAMERATE):
    #             if(diff_y < 0):
    #                 return_v_y = 120 / self.FRAMERATE
    #             else:
    #                 return_v_y = -120 / self.FRAMERATE
    #         else:
    #             return_v_y = -1 * (diff_y % (120 / self.FRAMERATE))
    #         self.usr_entity.v_y = return_v_y
    #     else:
    #         self.usr_entity.v_y = (self.move_y * 60 / self.FRAMERATE)
    #         #do boundary check
    #         if(self.move_d == moveconst and diff_y > self.WIN_WIDTH // 2 - self.WIN_WIDTH // 8 + self.usr_entity.size // 2):
    #             self.usr_entity.v_y = 0
    #         if(self.move_u == moveconst and diff_y < (-1 * (self.WIN_WIDTH // 2 - self.WIN_WIDTH // 8) - self.usr_entity.size // 2)):
    #             self.usr_entity.v_y = 0
    #
    #
    #     self.usr_entity.move()
    #
    #     #display entity
    #     self.usr_entity.clear(self.screen)
    #     self.usr_entity.display(self.screen)
    #
    #     pygame.display.flip()
    #     self.move_u = 0
    #     self.move_r = 0
    #     self.move_d = 0
    #     self.move_l = 0
    #     self.move_x = 0
    #     self.move_y = 0
    #
    #     self.return_v_x = 0
    #     self.return_v_y = 0
