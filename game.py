import numpy as np
import random
import var
import tkinter
import sys
import time

def fail():
    print('You Lose.') 
    print(var.score)
def new_food():
    while True:
        food_pos.clear()
        food_pos.append([random.randint(0,var.block_amount-1),random.randint(0,var.block_amount-1)])
        if snake_pos.count(food_pos[0])==0:
            break
class action:
    def left():
        head=[snake_pos[0][0],snake_pos[0][1]-1]
        snake_pos.pop()
        snake_pos.insert(0,head)
        if snake_pos[0][1]==-1:#死亡判定(撞墻)
            fail()
            sys.exit(0)

        if snake_pos.count(food_pos[0])>0:#吃到食物獲得獎勵、增加長度並重置食物位置
            var.score+=10
            snake_pos.append([snake_pos[-1][0],snake_pos[-1][1]])
            new_food()
        if snake_pos.count(head)>1:#死亡判定(自噬)
            fail()
            sys.exit(0)
    def right():
        head=[snake_pos[0][0],snake_pos[0][1]+1]

        snake_pos.pop()
        snake_pos.insert(0,head)
        if snake_pos[0][1]>var.block_amount-1:#死亡判定(撞墻)
            fail()
            sys.exit(0)


        if snake_pos.count(food_pos[0])>0:#吃到食物獲得獎勵、增加長度並重置食物位置
            var.score+=10
            snake_pos.append([snake_pos[-1][0],snake_pos[-1][1]])
            new_food()
        if snake_pos.count(head)>1:#死亡判定(自噬)
            fail()
            sys.exit(0)  

    def up():
        head=[snake_pos[0][0]-1,snake_pos[0][1]]
        snake_pos.pop()
        snake_pos.insert(0,head)
        if snake_pos[0][0]==-1:#死亡判定(撞墻)
            fail()
            sys.exit(0)


        if snake_pos.count(food_pos[0])>0:#吃到食物獲得獎勵、增加長度並重置食物位置
            var.score+=10
            snake_pos.append([snake_pos[-1][0],snake_pos[-1][1]])
            new_food()
        if snake_pos.count(head)>1:#死亡判定(自噬)
            fail()
            sys.exit(0)      

    def down():
        head=[snake_pos[0][0]+1,snake_pos[0][1]]

        snake_pos.pop()
        snake_pos.insert(0,head)
        if snake_pos[0][0]>var.block_amount-1:#死亡判定(撞墻)
            fail()
            sys.exit(0)


        if snake_pos.count(food_pos[0])>0:#吃到食物獲得獎勵、增加長度並重置食物位置
            var.score+=10
            snake_pos.append([snake_pos[-1][0],snake_pos[-1][1]])
            new_food()
        if snake_pos.count(head)>1:#死亡判定(自噬)
            fail()
            sys.exit(0)  


direction='right'
def change_direction(new_direction):
    global direction
    if direction=='left' and new_direction!='right':
        direction=new_direction
    elif direction=='right' and new_direction!='left':
        direction=new_direction
    elif direction=='up' and new_direction!='down':
        direction=new_direction
    elif direction=='down' and new_direction!='up':
        direction=new_direction
    else:
        pass

    
#蛇和食物的位置
snake_pos=[]
food_pos=[]
snake_pos.append([round(var.block_amount/2),round(var.block_amount/2)])
snake_pos.append([round(var.block_amount/2),round(var.block_amount/2)-1])
new_food()



window=tkinter.Tk()
window.title('Snake Game V2')
window.resizable(0,0)

textvar=tkinter.StringVar()
textvar.set('Score:'+str(var.score))
score_box=tkinter.Label(window,fg='Orange',bg='Black',textvariable=textvar)
score_box.pack()
screen=tkinter.Canvas(window,width=var.width,height=var.height,bg='Black')
screen.pack()#游戲屏幕完成


while True:
    screen.delete('all')
    if direction=='left':
        action.left()
    if direction=='right':
            action.right()
    if direction=='up':
        action.up()
    if direction=='down':
        action.down()
    print(direction)
    screen.create_rectangle(var.block_edge_length*food_pos[0][1],var.block_edge_length*food_pos[0][0],var.block_edge_length*food_pos[0][1]+var.block_edge_length,var.block_edge_length*food_pos[0][0]+var.block_edge_length,fill='Yellow')
    for x,y in snake_pos:
        if snake_pos[0]==[x,y]:
            screen.create_oval(var.block_edge_length*y,var.block_edge_length*x,var.block_edge_length*y+var.block_edge_length,var.block_edge_length*x+var.block_edge_length,fill='Red')
            continue
        screen.create_rectangle(var.block_edge_length*y,var.block_edge_length*x,var.block_edge_length*y+var.block_edge_length,var.block_edge_length*x+var.block_edge_length,fill='Green')
    screen.pack()
    textvar.set('Score:'+str(var.score))
    window.bind('<Left>', lambda event: change_direction('left'))
    window.bind('<Right>', lambda event: change_direction('right'))
    window.bind('<Up>', lambda event: change_direction('up'))
    window.bind('<Down>', lambda event: change_direction('down'))

    
    time.sleep(var.react)
    window.update()


