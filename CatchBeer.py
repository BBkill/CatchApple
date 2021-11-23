# Menu
from os import system
import sys

from tkinter.constants import FALSE
from typing import Tuple
import pygame
from pygame import mouse
from pygame.constants import K_BACKSPACE, K_ESCAPE, MOUSEBUTTONDOWN, QUIT
import pygame.display
import pygame.event
import pygame.draw
import pygame.mouse
from pygame.time import Clock
import pygame.time
import pygame.font
import pygame.image


pygame.init()


def helpBlock():  # block 'NO' numb2
    pygame.draw.circle(screen, WHITE, (225, 250), 25)
    pygame.draw.circle(screen, WHITE, (275, 250), 25)
    pygame.draw.rect(screen, WHITE, (225, 225, 50, 50))
    screen.blit(helpContent,(217,238))


def playBlock():  # block 'NO' numb1
    pygame.draw.circle(screen, WHITE, (225, 150), 25)
    pygame.draw.circle(screen, WHITE, (275, 150), 25)
    pygame.draw.rect(screen, WHITE, (225, 125, 50, 50))
    screen.blit(playContent,(218,138))


def menuBlock():  # content
    pygame.draw.circle(screen, WHITE, (225, 250), 25)
    pygame.draw.circle(screen, WHITE, (275, 250), 25)
    pygame.draw.rect(screen, WHITE, (225, 225, 50, 50))
    screen.blit(menuContent,(216,235))


def coverBlock():
    pygame.draw.rect(screen, WHITE, (100, 340, 300, 100))
    screen.blit(guildContent_line_1,(120,360))
    screen.blit(guildContent_line_2,(120,390))


# STACIC
screen = pygame.display.set_mode((500, 500))
GREY = (120, 120, 120)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

running = True


# text format
font = pygame.font.SysFont("Consolas", 30, True)
font1 = pygame.font.SysFont("Consolas", 30, True, True)
font_2 = pygame.font.SysFont("Consolas", 28, True)

helpContent = font1.render("Help", True, BLACK)
playContent = font1.render("Play", True, BLACK)
menuContent = font.render("Menu", True, BLACK)
guildContent_line_1 = font_2.render("Use right/left to", True, BLACK)
guildContent_line_2 = font_2.render("  move the bowl", True, BLACK)

image = pygame.image.load('backgr.png') 

while running:

    clock = pygame.time.Clock()
    clock.tick(40)
    screen.fill(GREY)
    screen.blit(image,(0,0))
    inMenu = False

    menuBlock()
    mouse_x, mouse_y = pygame.mouse.get_pos()

    for event in pygame.event.get():

        # quit
        if event.type == pygame.QUIT:
            running = False
            sys.exit()
        # nhận biết con trỏ chuột
        if event.type == MOUSEBUTTONDOWN:
            if (200 < mouse_x < 300) and (225 < mouse_y < 250):
                inMenu = True
                # chuyển đến bảng menu
                helpCheck = False
                while inMenu:
                    
                    playBlock()
                    helpBlock()
                    # in ra lựa chọn
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                  
                    
                    for eventMenu in pygame.event.get():
                        #quit
                        if eventMenu.type == pygame.QUIT:
                            sys.exit()
                        if eventMenu.type == MOUSEBUTTONDOWN:
                            #play
                            if (200 < mouse_x < 300) and (125 < mouse_y < 175):
                                inMenu = False
                                running = False
                                break
                            #help
                            if (200 < mouse_x < 300) and (210 < mouse_y < 290):
                                helpCheck = True
                                break
                    if helpCheck == True:
                        coverBlock()
                        pygame.display.update()
                    pygame.display.update()
    pygame.display.update()
pygame.display.quit()


# Game


from tkinter import *
from time import sleep
from PIL import ImageTk, Image
from random import randint

# from Menu import *
# from playsound import playsound

# độ rộng của cửa nền
Width = 700
Hight = 525
# khoảng xuất hiện táo
rangeR = 680
rangeL = 20
x = randint(rangeL, rangeR)
y = -40
fallingSpeed = 1 / 80  # tốc độ của vật thể rơi
movingSpeed = 40  # tốc độ của cái bát

Score = 0  # điểm
file = open("HighestScore.txt", "r")
highestScore = int(file.readline())
file.close()
live = 3  # mạng
game = Tk()
game.title("Catch Beer")
canvas = Canvas(master=game, width=Width, height=Hight, background="white", bd=5)
canvas.pack()


img = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
img[0] = ImageTk.PhotoImage(Image.open("backgr.png"))
img[1] = ImageTk.PhotoImage(Image.open("bowl.png"))
img[2] = ImageTk.PhotoImage(Image.open("apple.png"))
img[3] = ImageTk.PhotoImage(Image.open("bomb.png"))
img[4] = ImageTk.PhotoImage(Image.open("bomm.png"))
img[5] = ImageTk.PhotoImage(Image.open("heart.png"))
img[6] = ImageTk.PhotoImage(Image.open("heart.png"))
img[7] = ImageTk.PhotoImage(Image.open("heart.png"))
img[8] = ImageTk.PhotoImage(Image.open("over.png"))
img[9] = ImageTk.PhotoImage(Image.open("replay.png"))
heart = [0, 0, 0]

backgr = canvas.create_image(0, 0, anchor=NW, image=img[0])
bowl = canvas.create_image(0, 420, anchor=NW, image=img[1])
apple = canvas.create_image(x, y, anchor=NW, image=img[2])
bomb = canvas.create_image(x, y, anchor=NW, image=img[3])

heart[0] = canvas.create_image(20, 10, anchor=NW, image=img[5])
heart[1] = canvas.create_image(45, 10, anchor=NW, image=img[6])
heart[2] = canvas.create_image(70, 10, anchor=NW, image=img[7])


CoutingtScore = canvas.create_text(
    570, 20, text="Score: " + str(Score), font=("Consolas", 14), fill="red"
)
HighestScore = canvas.create_text(
    610,
    40,
    text="Highest Score: " + str(highestScore),
    font=("Consolas", 14),
    fill="red",
)

# táo rơi
def fallingApple():
    global apple, Score, highestScore, file
    canvas.move(apple, 0, 8)
    if canvas.coords(apple)[1] > 550:
        canvas.delete(apple)
        y = -20
        x = randint(rangeL, rangeR)
        apple = canvas.create_image(x, y, anchor=NW, image=img[2])
    if (
        canvas.coords(apple)[0] >= canvas.coords(bowl)[0]
        and canvas.coords(apple)[0] + 50 <= canvas.coords(bowl)[0] + 120
    ) and (
        canvas.coords(apple)[1] + 50 >= canvas.coords(bowl)[1]
        and canvas.coords(apple)[1] + 50 <= canvas.coords(bowl)[1] + 40
    ):
        canvas.delete(apple)
        y = -20
        x = randint(rangeL, rangeR)
        apple = canvas.create_image(x, y, anchor=NW, image=img[2])
        Score = Score + 1
        if highestScore < Score:
            highestScore = Score
            canvas.itemconfig(HighestScore, text="Highest Score: " + str(Score))
        canvas.itemconfig(CoutingtScore, text="Score: " + str(Score))
        file = open("HighestScore.txt", "w")
        file.write(str(highestScore))
        file.close()
    canvas.update()


gameOver = False

# bom rơi
def fallingBomb():
    global bomb, Score, live, gameOver
    canvas.move(bomb, 0, 8)
    if canvas.coords(bomb)[1] > 550:
        canvas.delete(bomb)
        y = -20
        x = randint(rangeL, rangeR)
        bomb = canvas.create_image(x, -40, anchor=NW, image=img[3])

    if (
        canvas.coords(bomb)[0] >= canvas.coords(bowl)[0] - 30
        and canvas.coords(bomb)[0] + 50 <= canvas.coords(bowl)[0] + 120
    ) and (
        canvas.coords(bomb)[1] + 50 >= canvas.coords(bowl)[1]
        and canvas.coords(bomb)[1] + 50 <= canvas.coords(bowl)[1] + 40
    ):
        canvas.delete(bomb)
        y = -20
        x = randint(rangeL, rangeR)
        bomb = canvas.create_image(x, y, anchor=NW, image=img[3])
        Score = Score - 1
        live = live - 1
        canvas.delete(heart[live])
        if live == 0:
            gameOver = True
        bomm = canvas.create_image(100, 20, anchor=NW, image=img[4])
        canvas.update()
        sleep(1)
        canvas.delete(bomm)
        canvas.itemconfig(CoutingtScore, text="Score: " + str(Score))
    canvas.update()


# di chuyển cái bát qua phải
def right():
    global bowl
   
    if canvas.coords(bowl)[0] < 680:
        canvas.move(bowl, movingSpeed, 0)
    canvas.update()


# di chuyển cái bát qua trái
def left():
    global bowl
    if canvas.coords(bowl)[0] > 0:
        canvas.move(bowl, -movingSpeed, 0)
    canvas.update()


# nhận biết phím điều hướng
def keyPress(event):
    if event.keysym == "Right":
        right()
    if event.keysym == "Left":
        left()

    if event.keysym == "Enter":
        gameOver = False



canvas.bind_all("<KeyPress>", keyPress)

while True:

    check = True
    while not gameOver:
        fallingApple()
        fallingBomb()
        sleep(fallingSpeed)
    over = canvas.create_image(180, 70, anchor=NW, image=img[8])
    canvas.update()
    game.mainloop()
    
