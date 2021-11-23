# from tkinter.constants import FALSE
# import pygame
# from pygame import mouse
# from pygame.constants import MOUSEBUTTONDOWN, QUIT
# import pygame.display
# import pygame.event
# import pygame.draw
# import pygame.mouse
# from pygame.time import Clock
# import pygame.time
# import pygame.font
# import pygame.image


# pygame.init()


# def helpBlock():#block 'NO' numb1
#     pygame.draw.circle(screen,WHITE, (225,150),25)
#     pygame.draw.circle(screen,WHITE, (275,150),25)
#     pygame.draw.rect(screen,WHITE,(225,125,50,50))
#     screen.blit(playContent,(218,138))
    


# def playBlock():#block 'NO' numb2
#     pygame.draw.circle(screen,WHITE, (225,250),25)
#     pygame.draw.circle(screen,WHITE, (275,250),25)
#     pygame.draw.rect(screen,WHITE,(225,225,50,50))
#     screen.blit(helpContent,(217,238))
    


# def menuBlock():#content
#     pygame.draw.circle(screen,WHITE, (225,250),25)
#     pygame.draw.circle(screen,WHITE, (275,250),25)
#     pygame.draw.rect(screen,WHITE,(225,225,50,50))
#     screen.blit(menuContent,(216,235))
    
# def coverBlock():
#     pygame.draw.rect(screen,GREY,(200,200,100,50)) 
    
# #STACIC 
# screen = pygame.display.set_mode((500,500))
# GREY = (120,120,120)
# WHITE = (255,255,255)
# BLACK = (0,0,0)

# running = True


# #text format/ the answer 
# font1 = pygame.font.SysFont('Consolas',30,True, True)
# helpContent= font1.render("Help",True,BLACK)
# playContent=font1.render("Play",True,BLACK)

# #text format/ the question
# font = pygame.font.SysFont('Consolas',30, True)
# menuContent = font.render("Menu",True,BLACK)


# while running:
        
#         clock= pygame.time.Clock()
#         clock.tick(75)
#         screen.fill(GREY)
#         inMenu = False
        
#         menuBlock()
        
#         mouse_x,mouse_y=pygame.mouse.get_pos()
#         print(str(mouse_x)+" "+str(mouse_y))
#         for event in  pygame.event.get():
            
#             #quit
#             if event.type == pygame.QUIT:
#                 running = False
                
#             #nhận biết con trỏ chuột
#             if event.type == MOUSEBUTTONDOWN:
#                 if (200<mouse_x<300) and (225<mouse_y<250):
#                     inMenu = True
#                     #chuyển đến bảng menu
#                     while inMenu:
#                         #quit
#                         mouse_x,mouse_y=pygame.mouse.get_pos()
#                         print(str(mouse_x)+" "+str(mouse_y))
#                         for eventMenu in pygame.event.get():
#                             if eventMenu.type == pygame.QUIT:
#                                 inMenu = False
#                                 running = False
#                         #in ra lựa chọn
#                         helpBlock()
                        
#                         playBlock()
                        
#                         pygame.display.update()
#         pygame.display.update()
