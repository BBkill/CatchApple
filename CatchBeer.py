
from tkinter import * 
from time import sleep
from PIL import ImageTk, Image
from random import randint
#from playsound import playsound

#độ rộng của cửa nền
Width=700
Hight=525
#khoảng xuất hiện táo
rangeR=680 
rangeL=20
x=randint(rangeL,rangeR)
y=-40
fallingSpeed=1/80 #tốc độ của vật thể rơi
movingSpeed=40 #tốc độ của cái bát

Score=0 # điểm
file = open('HighestScore.txt','r')
highestScore = int(file.readline())
file.close()
live = 3 # mạng
game=Tk()
game.title("Catch Beer")
canvas=Canvas(master=game,width=Width,height=Hight,background="white",bd=5)
canvas.pack()


img=[0,0,0,0,0,0,0,0,0]
img[0]=ImageTk.PhotoImage(Image.open("backgr.png"))
img[1]=ImageTk.PhotoImage(Image.open("bowl.png"))
img[2]=ImageTk.PhotoImage(Image.open("apple.png"))
img[3]=ImageTk.PhotoImage(Image.open("bomb.png"))
img[4]=ImageTk.PhotoImage(Image.open("bomm.png"))
img[5]=ImageTk.PhotoImage(Image.open("heart.png"))
img[6]=ImageTk.PhotoImage(Image.open("heart.png"))
img[7]=ImageTk.PhotoImage(Image.open("heart.png"))
img[8]=ImageTk.PhotoImage(Image.open("over.png"))
heart = [0,0,0]

backgr=canvas.create_image(0,0,anchor=NW,image=img[0])
bowl=canvas.create_image(0,420,anchor=NW,image=img[1])
apple=canvas.create_image(x,y,anchor=NW,image=img[2])
bomb=canvas.create_image(x,y,anchor=NW,image=img[3])

heart[0] = canvas.create_image(20,10,anchor=NW,image=img[5])
heart[1] = canvas.create_image(45,10,anchor=NW,image=img[6])
heart[2] = canvas.create_image(70,10,anchor=NW,image=img[7])



CoutingtScore=canvas.create_text(570,20,text="Score: "+str(Score),font=("Consolas",14),fill="red")
HighestScore = canvas.create_text(610,40,text="Highest Score: "+str(highestScore),font=("Consolas",14),fill="red")

#táo rơi
def fallingApple():
    global apple,Score,highestScore,file
    canvas.move(apple,0,8)
    if canvas.coords(apple)[1]>550:
        canvas.delete(apple)
        y=-20
        x=randint(rangeL,rangeR)
        apple=canvas.create_image(x,y,anchor=NW,image=img[2])
    if (canvas.coords(apple)[0]>=canvas.coords(bowl)[0] and canvas.coords(apple)[0]+50<=canvas.coords(bowl)[0]+120) and (canvas.coords(apple)[1]+50>=canvas.coords(bowl)[1] and canvas.coords(apple)[1]+50<=canvas.coords(bowl)[1]+40):
        canvas.delete(apple)
        y=-20
        x=randint(rangeL,rangeR)
        apple=canvas.create_image(x,y,anchor=NW,image=img[2])
        Score=Score+1
        if highestScore<Score:
            highestScore=Score
            canvas.itemconfig(HighestScore,text="Highest Score: "+str(Score))
        canvas.itemconfig(CoutingtScore,text="Score: "+str(Score))
        file = open('HighestScore.txt','w')
        file.write(str(highestScore))
        file.close()
    canvas.update()


gameOver=False

#bom rơi
def fallingBomb():
    global bomb,Score,live,gameOver
    canvas.move(bomb,0,8)
    if canvas.coords(bomb)[1]>550:
        canvas.delete(bomb)
        y=-20
        x=randint(rangeL,rangeR)
        bomb=canvas.create_image(x,-20,anchor=NW,image=img[3])
    if (canvas.coords(bomb)[0]>=canvas.coords(bowl)[0]-30 and canvas.coords(bomb)[0]+50<=canvas.coords(bowl)[0]+120) and (canvas.coords(bomb)[1]+50>=canvas.coords(bowl)[1] and canvas.coords(bomb)[1]+50<=canvas.coords(bowl)[1]+40):
        canvas.delete(bomb)
        y=-20
        x=randint(rangeL,rangeR)
        bomb=canvas.create_image(x,y,anchor=NW,image=img[3])
        Score=Score-1
        live = live -1
        canvas.delete(heart[live])
        if live==0: gameOver = True 
        bomm=canvas.create_image(100,20,anchor=NW,image=img[4])
        canvas.update()
        sleep(2)
        canvas.delete(bomm)
        canvas.itemconfig(CoutingtScore,text="Score: "+str(Score))
    canvas.update()
    
    
    
#di chuyển cái bát qua phải
def right():
    global bowl
    if canvas.coords(bowl)[0]<680:
        canvas.move(bowl,movingSpeed,0)
    canvas.update()

#di chuyển cái bát qua trái
def left():
    global bowl
    if canvas.coords(bowl)[0]>0:
        canvas.move(bowl,-movingSpeed,0)
    canvas.update()
    
#nhận biết phím điều hướng
def keyPress(event):
    if event.keysym=="Right":
        right()
    if event.keysym=="Left":
        left()


canvas.bind_all("<KeyPress>",keyPress)
while not gameOver:
    fallingApple()
    fallingBomb()
    sleep(fallingSpeed)
over=canvas.create_image(180,70,anchor=NW,image = img[8])


canvas.update()
game.mainloop()

