'''
author: Doaa Ali El-sayed Mohamed 
this a python code for game number scrabble
'''

# import tkinter libarary for GUI 
from tkinter import *
from tkinter import messagebox

#intialize the window
window = Tk()
window.title("NUBMER SCRABBLE")
window.geometry("600x350")
window.resizable(False, False)
window.configure(bg='#FFEBCD')


player_1 = []
player_2 = []
winner_num = []
turn = 1
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# create labels
lb1 = Label(window,text='NUMBER SCRABBLE GAME',font=('bold 15'), bg='#FFEBCD').grid(column=0, row=0)
lb2 = Label(window,text=(f"Player 1: "),font= 15,fg='red').grid(column=0,row=1)
lb3 = Label(window,text=(f"Player 2: "),font= 15,fg='green').grid(column=0, row=2)

#create functions to update numbers' buttons once clicked for each player
def click_1():
    global turn, player_1, player_2
    if turn==1:
        turn = 2
        btn1["state"] = DISABLED
        btn1["bg"] = "red"
        player_1.append(btn1["text"])
        # update player's label to display his numbers
        lb2 = Label( window, text=(f"Player 1: {player_1}"), font=15, fg='red').grid( column=0, row=1 )
        numbers.remove(btn1["text"])
        # this is a function to check if the winner 
        check(player_1, "player 1", numbers)
        return player_1, numbers
    elif turn==2:
        turn = 1
        btn1["state"] = DISABLED
        btn1["bg"] = "green"
        player_2.append(btn1["text"])
        lb3 = Label( window, text=(f"Player 2: {player_2}"), font=15, fg='green').grid( column=0, row=2 )
        numbers.remove(btn1["text"])
        check(player_2, "player 2", numbers)
        return player_2, numbers

def click_2():
    global turn, player_1, player_2
    if turn==1:
        turn = 2
        btn2["state"] = DISABLED
        btn2["bg"] = "red"
        player_1.append(btn2["text"])
        lb2 = Label( window, text=(f"Player 1: {player_1}"), font=15, fg='red').grid( column=0, row=1 )
        numbers.remove(btn2["text"])
        check(player_1, "player 1", numbers)
        return player_1, numbers
    elif turn==2:
        turn = 1
        btn2["state"] = DISABLED
        btn2["bg"] = "green"
        player_2.append(btn2["text"])
        lb3 = Label( window, text=(f"Player 2: {player_2}"), font=15, fg='green').grid( column=0, row=2 )
        numbers.remove(btn2["text"])
        check(player_2, "player 2", numbers)
        return player_2, numbers

def click_3():
    global turn, player_1, player_2
    if turn==1:
        turn = 2
        btn3["state"] = DISABLED
        btn3["bg"] = "red"
        player_1.append(btn3["text"])
        lb2 = Label( window, text=(f"Player 1: {player_1}"), font=15, fg='red').grid( column=0, row=1 )
        numbers.remove(btn3["text"])
        check(player_1, "player 1", numbers)
        return player_1, numbers
    elif turn==2:
        turn = 1
        btn3["state"] = DISABLED
        btn3["bg"] = "green"
        player_2.append(btn3["text"])
        lb3 = Label( window, text=(f"Player 2: {player_2}"), font=15, fg='green').grid( column=0, row=2 )
        numbers.remove(btn3["text"])
        check(player_2, "player 2", numbers)
        return player_2, numbers

def click_4():
    global turn, player_1, player_2
    if turn==1:
        turn = 2
        btn4["state"] = DISABLED
        btn4["bg"] = "red"
        player_1.append(btn4["text"])
        lb2 = Label( window, text=(f"Player 1: {player_1}"), font=15, fg='red').grid( column=0, row=1 )
        numbers.remove(btn4["text"])
        check(player_1, "player 1", numbers)
        return player_1, numbers
    elif turn==2:
        turn = 1
        btn4["state"] = DISABLED
        btn4["bg"] = "green"
        player_2.append(btn4["text"])
        lb3 = Label( window, text=(f"Player 2: {player_2}"), font=15, fg='green').grid( column=0, row=2 )
        numbers.remove(btn4["text"])
        check(player_2, "player 2", numbers)
        return player_2, numbers

def click_5():
    global turn, player_1, player_2
    if turn==1:
        turn = 2
        btn5["state"] = DISABLED
        btn5["bg"] = "red"
        player_1.append(btn5["text"])
        lb2 = Label( window, text=(f"Player 1: {player_1}"), font=15, fg='red').grid( column=0, row=1 )
        numbers.remove(btn5["text"])
        check(player_1, "player 1", numbers)
        return player_1, numbers
    elif turn==2:
        turn = 1
        btn5["state"] = DISABLED
        btn5["bg"] = "green"
        player_2.append(btn5["text"])
        lb3 = Label( window, text=(f"Player 2: {player_2}"), font=15, fg='green').grid( column=0, row=2 )
        numbers.remove(btn5["text"])
        check(player_2, "player 2", numbers)
        return player_2, numbers

def click_6():
    global turn, player_1, player_2
    if turn==1:
        turn = 2
        btn6["state"] = DISABLED
        btn6["bg"] = "red"
        player_1.append(btn6["text"])
        lb2 = Label( window, text=(f"Player 1: {player_1}"), font=15, fg='red').grid( column=0, row=1 )
        numbers.remove(btn6["text"])
        check(player_1, "player 1", numbers)
        return player_1, numbers
    elif turn==2:
        turn = 1
        btn6["state"] = DISABLED
        btn6["bg"] = "green"
        player_2.append(btn6["text"])
        lb3 = Label( window, text=(f"Player 2: {player_2}"), font=15, fg='green').grid( column=0, row=2 )
        numbers.remove(btn6["text"])
        check(player_2, "player 2", numbers)
        return player_2, numbers

def click_7():
    global turn, player_1, player_2
    if turn==1:
        turn = 2
        btn7["state"] = DISABLED
        btn7["bg"] = "red"
        player_1.append(btn7["text"])
        lb2 = Label( window, text=(f"Player 1: {player_1}"), font=15, fg='red').grid( column=0, row=1 )
        numbers.remove(btn7["text"])
        check(player_1, "player 1", numbers)
        return player_1, numbers
    elif turn==2:
        turn = 1
        btn7["state"] = DISABLED
        btn7["bg"] = "green"
        player_2.append(btn7["text"])
        lb3 = Label( window, text=(f"Player 2: {player_2}"), font=15, fg='green').grid( column=0, row=2 )
        numbers.remove(btn7["text"])
        check(player_2, "player 2", numbers)
        return player_2, numbers

def click_8():
    global turn, player_1, player_2
    if turn==1:
        turn = 2
        btn8["state"] = DISABLED
        btn8["bg"] = "red"
        player_1.append(btn8["text"])
        lb2 = Label( window, text=(f"Player 1: {player_1}"), font=15, fg='red').grid( column=0, row=1 )
        numbers.remove(btn8["text"])
        check(player_1, "player 1", numbers)
        return player_1, numbers
    elif turn==2:
        turn = 1
        btn8["state"] = DISABLED
        btn8["bg"] = "green"
        player_2.append(btn8["text"])
        lb3 = Label( window, text=(f"Player 2: {player_2}"), font=15, fg='green').grid( column=0, row=2 )
        numbers.remove(btn8["text"])
        check(player_2, "player 2", numbers)
        return player_2, numbers
        
def click_9():
    global turn, player_1, player_2
    if turn==1:
        turn = 2
        btn9["state"] = DISABLED
        btn9["bg"] = "red"
        player_1.append(btn9["text"])
        lb2 = Label( window, text=(f"Player 1: {player_1}"), font=15, fg='red').grid( column=0, row=1 )
        numbers.remove(btn9["text"])
        check(player_1, "player 1", numbers)
        return player_1, numbers
    elif turn==2:
        turn = 1
        btn9["state"] = DISABLED
        btn9["bg"] = "green"
        player_2.append(btn9["text"])
        lb3 = Label( window, text=(f"Player 2: {player_2}"), font=15, fg='green').grid( column=0, row=2 )
        numbers.remove(btn9["text"])
        check(player_2, "player 2", numbers)
        return player_2, numbers

# create a function to cheak if a player gets 15 or not

def check(list_player, win, list_numbers):
    global winner_num
    # check if player's list has three numbers get 15 or not
    if len(list_player) >= 3:
        for i in range(0, len(list_player)-2):
            for j in range(i+1, len(list_player)-1):
                for k in range(j+1,len(list_player)):
                    if_15 = list_player[i]+ list_player[j]+ list_player[k]
                    if if_15 == 15:
                        winner_num.append(list_player[i])
                        winner_num.append(list_player[j])
                        winner_num.append(list_player[k])
                        winner_num = tuple(winner_num)
                        # this is a function to display the winner if there's a one
                        winner(win, winner_num)
                        return winner_num
    # if no one gets 15 and all numbers are picked, display draw message                 
    if len(list_numbers) == 0 and len(winner_num) == 0:
        no_player()

# create a function to display a message with the winner and end the game
def winner(player, nums):
    winner = player
    message = "CONGRATULATIONS\n"+ winner +" wins \n"+str(nums)
    messagebox.showinfo("GAME OVER", message)
    window.destroy()

# create a function to display a draw message and end the game
def no_player():
    message = "DRAW\nTRY NEXT TIME"
    messagebox.showinfo("GAME OVER", message)
    window.destroy()


# create the numers' buttons

btn1 = Button(window, text=1,bg="#8B4513", fg="white",width=6,height=2,font=('Helvetica 20'), command=click_1)
btn1.grid(column=1, row=1)
btn2 = Button(window, text=2,bg="#8B4513", fg="white",width=6,height=2,font=('Helvetica 20'), command=click_2)
btn2.grid(column=2, row=1)
btn3 = Button(window, text=3,bg="#8B4513", fg="white",width=6,height=2,font=('Helvetica 20'), command=click_3)
btn3.grid(column=3, row=1)
btn4 = Button(window, text=4,bg="#8B4513", fg="white",width=6,height=2,font=('Helvetica 20'), command=click_4)
btn4.grid(column=1, row=2)
btn5 = Button(window, text=5,bg="#8B4513", fg="white",width=6,height=2,font=('Helvetica 20'), command=click_5)
btn5.grid(column=2, row=2)
btn6 = Button(window, text=6,bg="#8B4513", fg="white",width=6,height=2,font=('Helvetica 20'), command=click_6)
btn6.grid(column=3, row=2)
btn7 = Button(window, text=7,bg="#8B4513", fg="white",width=6,height=2,font=('Helvetica 20'), command=click_7)
btn7.grid(column=1, row=3)
btn8 = Button(window, text=8,bg="#8B4513", fg="white",width=6,height=2,font=('Helvetica 20'), command=click_8)
btn8.grid(column=2, row=3)
btn9 = Button(window, text=9,bg="#8B4513", fg="white",width=6,height=2,font=('Helvetica 20'), command=click_9)
btn9.grid(column=3, row=3)


window.mainloop()
