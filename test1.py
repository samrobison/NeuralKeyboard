import os
import pygame
import sys
import time
import Tkinter

class Entity:
    def __init__(self, (x, y), size):
        self.x = x
        self.y = y
        self.x_prev = x
        self.y_prev = y
        self.size = size
        self.colour = (0,0,0)
        self.bg = (255,255,255)
        self.thickness = 1
        self.v_x = 0
        self.v_y = 0
    def display(self, screen):
        pygame.draw.circle(screen, self.colour, (int(self.x - (self.size / 2)), int(self.y - (self.size / 2))), self.size, self.thickness)
    def clear(self, screen):
        pygame.draw.circle(screen, self.bg, (int(self.x_prev - (self.size / 2)), int(self.y_prev - (self.size / 2))), self.size, self.thickness)
    def move(self):
        self.x_prev = self.x
        self.y_prev = self.y
        self.x += self.v_x
        self.y += self.v_y

def main():

    root = Tkinter.Tk()

    SCR_WIDTH = root.winfo_screenwidth()
    SCR_HEIGHT = root.winfo_screenheight()

    #initialize system values
    FRAMERATE = 60
    WIN_SCALE = 3
    WIN_WIDTH = SCR_WIDTH // WIN_SCALE
    WIN_HEIGHT = SCR_WIDTH // WIN_SCALE
    WIN_SIZE = [WIN_WIDTH, WIN_HEIGHT]

    WIN_X = SCR_WIDTH // 2 - WIN_WIDTH // 2
    WIN_Y = SCR_HEIGHT // 2 - WIN_HEIGHT // 2

    os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (WIN_X, WIN_Y)

    pygame.init()

    pygame.display.set_caption("NK Test 1")
    screen = pygame.display.set_mode(WIN_SIZE, pygame.DOUBLEBUF)
    screen.fill([255, 255, 255])
    
    clock = pygame.time.Clock()

    usr_entity = Entity((WIN_WIDTH // 2, WIN_HEIGHT // 2), 30)

    usr_entity.display(screen)
    pygame.display.flip()

    anchor_x = WIN_WIDTH // 2
    anchor_y = WIN_HEIGHT // 2

    move_u = 0
    move_r = 0
    move_d = 0
    move_l = 0
    move_x = 0
    move_y = 0

    return_v_x = 0
    return_v_y = 0

    while(True):

        #initialize force variables
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:                
                pygame.display.quit()
                pygame.quit()
                sys.exit()
            #recieve keyboard inputs
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    #apply upward force (-y)
                    move_u = 1
                if event.key == pygame.K_RIGHT:
                    #apply rightward force (+x)
                    move_r = 1
                if event.key == pygame.K_DOWN:
                    #apply downward force (+y)
                    move_d = 1
                if event.key == pygame.K_LEFT:
                    #apply leftward force (-x)
                    move_l = 1
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    move_u = 0
                if event.key == pygame.K_RIGHT:
                    move_r = 0
                if event.key == pygame.K_DOWN:
                    move_d = 0
                if event.key == pygame.K_LEFT:
                    move_l = 0

        if(move_u == 1 or move_d == 1):
            if(move_u == 1 and move_d == 1):
                move_y = 0
            elif(move_u == 1):
                move_y = -1
            else:
                move_y = 1
        else:
            move_y = 0

        if(move_r == 1 or move_l == 1):
            if(move_r == 1 and move_l == 1):
                move_x = 0
            elif(move_r == 1):
                move_x = 1
            else:
                move_x = -1
        else:
            move_x = 0
        
        diff_x = usr_entity.x - anchor_x
        diff_y = usr_entity.y - anchor_y
        
        #set entity velocity
        if(move_x == 0):
            #reset x to anchor
            if(abs(diff_x) > 120 / FRAMERATE):
                if(diff_x < 0):
                    return_v_x = 120 / FRAMERATE
                else:
                    return_v_x = -120 / FRAMERATE
            else:
                return_v_x = -1 * (diff_x % (120 / FRAMERATE))
            usr_entity.v_x = return_v_x
        else:
            usr_entity.v_x = (move_x * 60 / FRAMERATE)
            #do boundary check
            if(move_r == 1 and diff_x > WIN_WIDTH // 2 - WIN_WIDTH // 8 + usr_entity.size // 2):
                usr_entity.v_x = 0
            if(move_l == 1 and diff_x < (-1 * (WIN_WIDTH // 2 - WIN_WIDTH // 8) - usr_entity.size // 2)):
                usr_entity.v_x = 0
        if(move_y == 0):
            #reset x to anchor
            if(abs(diff_y) > 120 / FRAMERATE):
                if(diff_y < 0):
                    return_v_y = 120 / FRAMERATE
                else:
                    return_v_y = -120 / FRAMERATE
            else:
                return_v_y = -1 * (diff_y % (120 / FRAMERATE))
            usr_entity.v_y = return_v_y
        else:
            usr_entity.v_y = (move_y * 60 / FRAMERATE)
            #do boundary check
            if(move_d == 1 and diff_y > WIN_WIDTH // 2 - WIN_WIDTH // 8 + usr_entity.size // 2):
                usr_entity.v_y = 0
            if(move_u == 1 and diff_y < (-1 * (WIN_WIDTH // 2 - WIN_WIDTH // 8) - usr_entity.size // 2)):
                usr_entity.v_y = 0
            

        usr_entity.move()

        #display entity
        usr_entity.clear(screen)
        usr_entity.display(screen)

        pygame.display.flip()

if __name__ == "__main__":
    main()
