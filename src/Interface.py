from Tkinter import *
import tkMessageBox

window = Tk()
window.title("Tic Tac Toe")
area = Canvas(window, width=600, height=600)
area.grid(row=0, column=0)

# create and place buttons

b1 = Button(area, text=' ', width=8, height=4, font='Times 30 bold', command=lambda: play(b1))
b1.grid(row=0, column=0, sticky=S+N+E+W)

b2 = Button(area, text=' ', width=8, height=4, font='Times 30 bold', command=lambda: play(b2))
b2.grid(row=0, column=1, sticky=S+N+E+W)

b3 = Button(area, text=' ', width=8, height=4, font='Times 30 bold', command=lambda: play(b3))
b3.grid(row=0, column=2, sticky=S+N+E+W)

b4 = Button(area, text=' ', width=8, height=4, font='Times 30 bold', command=lambda: play(b4))
b4.grid(row=1, column=0, sticky=S+N+E+W)

b5 = Button(area, text=' ', width=8, height=4, font='Times 30 bold', command=lambda: play(b5))
b5.grid(row=1, column=1, sticky=S+N+E+W)

b6 = Button(area, text=' ', width=8, height=4, font='Times 30 bold', command=lambda: play(b6))
b6.grid(row=1, column=2, sticky=S+N+E+W)

b7 = Button(area, text=' ', width=8, height=4, font='Times 30 bold', command=lambda: play(b7))
b7.grid(row=2, column=0, sticky=S+N+E+W)

b8 = Button(area, text=' ', width=8, height=4, font='Times 30 bold', command=lambda: play(b8))
b8.grid(row=2, column=1, sticky=S+N+E+W)

b9 = Button(area, text=' ', width=8, height=4, font='Times 30 bold', command=lambda: play(b9))
b9.grid(row=2, column=2, sticky=S+N+E+W)

# function to see if a button has been pressed


def safe(d):

    if d['text'] == ' ':
        return True
    else:
        return False


# Checks to see if winning combination exists

def win():

    if (b1['text'] == 'X' and b2['text'] == 'X' and b3['text'] == 'X') or \
            (b4['text'] == 'X' and b5['text'] == 'X' and b6['text'] == 'X') or \
            (b7['text'] == 'X' and b8['text'] == 'X' and b9['text'] == 'X') or \
            (b1['text'] == 'X' and b4['text'] == 'X' and b7['text'] == 'X') or \
            (b2['text'] == 'X' and b5['text'] == 'X' and b8['text'] == 'X') or \
            (b3['text'] == 'X' and b6['text'] == 'X' and b9['text'] == 'X') or \
            (b1['text'] == 'X' and b5['text'] == 'X' and b9['text'] == 'X') or \
            (b3['text'] == 'X' and b5['text'] == 'X' and b7['text'] == 'X'):
        tkMessageBox.showinfo(title='Winner', message='You won!')

    elif (b1['text'] == 'O' and b2['text'] == 'O' and b3['text'] == 'O') or \
            (b4['text'] == 'O' and b5['text'] == 'O' and b6['text'] == 'O') or \
            (b7['text'] == 'O' and b8['text'] == 'O' and b9['text'] == 'O') or \
            (b1['text'] == 'O' and b4['text'] == 'O' and b7['text'] == 'O') or \
            (b2['text'] == 'O' and b5['text'] == 'O' and b8['text'] == 'O') or \
            (b3['text'] == 'O' and b6['text'] == 'O' and b9['text'] == 'O') or \
            (b1['text'] == 'O' and b5['text'] == 'O' and b9['text'] == 'O') or \
            (b3['text'] == 'O' and b5['text'] == 'O' and b7['text'] == 'O'):
        tkMessageBox.showinfo(title='Winner', message='The AI won!')


# AI player

def ai():

    # Stage 1: Search for winning Combination

    if ((b2['text'] == 'O' and b3['text'] == 'O') or (b5['text'] == 'O' and b9['text'] == 'O') or
            (b4['text'] == 'O' and b7['text'] == 'O')) and b1['text'] == ' ':
        b1['text'] = 'O'

    elif ((b1['text'] == 'O' and b3['text'] == 'O') or (b5['text'] == 'O' and b8['text'] == 'O')) and b2['text'] == ' ':
        b2['text'] = 'O'

    elif ((b1['text'] == 'O' and b2['text'] == 'O') or (b5['text'] == 'O' and b7['text'] == 'O') or
          (b6['text'] == 'O' and b9['text'] == 'O')) and b3['text'] == ' ':
        b3['text'] = 'O'

    elif ((b1['text'] == 'O' and b7['text'] == 'O') or (b5['text'] == 'O' and b6['text'] == 'O')) and b1['text'] == ' ':
        b4['text'] = 'O'

    elif ((b1['text'] == 'O' and b9['text'] == 'O') or (b2['text'] == 'O' and b8['text'] == 'O') or
          (b3['text'] == 'O' and b7['text'] == 'O') or (b4['text'] == 'O' and b6['text'] == 'O')) and \
            b5['text'] == ' ':
        b5['text'] = 'O'

    elif ((b3['text'] == 'O' and b9['text'] == 'O') or (b4['text'] == 'O' and b5['text'] == 'O')) and b6['text'] == ' ':
        b6['text'] = 'O'

    elif ((b1['text'] == 'O' and b4['text'] == 'O') or (b3['text'] == 'O' and b5['text'] == 'O') or
          (b8['text'] == 'O' and b9['text'] == 'O')) and b7['text'] == ' ':
        b7['text'] = 'O'

    elif ((b2['text'] == 'O' and b5['text'] == 'O') or (b7['text'] == 'O' and b9['text'] == 'O')) and b8['text'] == ' ':
        b8['text'] = 'O'

    elif ((b1['text'] == 'O' and b5['text'] == 'O') or (b3['text'] == 'O' and b6['text'] == 'O') or
          (b7['text'] == 'O' and b8['text'] == 'O')) and b9['text'] == ' ':
        b9['text'] = 'O'

    # Stage 2: Search for defense against winning combination

    elif ((b2['text'] == 'X' and b3['text'] == 'X') or (b5['text'] == 'X' and b9['text'] == 'X') or
          (b4['text'] == 'X' and b7['text'] == 'X')) and b1['text'] == ' ':
        b1['text'] = 'O'

    elif ((b1['text'] == 'X' and b3['text'] == 'X') or (b5['text'] == 'X' and b8['text'] == 'X')) and b2['text'] == ' ':
        b2['text'] = 'O'

    elif ((b1['text'] == 'X' and b2['text'] == 'X') or (b5['text'] == 'X' and b7['text'] == 'X') or
          (b6['text'] == 'X' and b9['text'] == 'X')) and b3['text'] == ' ':
        b3['text'] = 'O'

    elif ((b1['text'] == 'X' and b7['text'] == 'X') or (b5['text'] == 'X' and b6['text'] == 'X')) and b4['text'] == ' ':
        b4['text'] = 'O'

    elif ((b1['text'] == 'X' and b9['text'] == 'X') or (b2['text'] == 'X' and b8['text'] == 'X') or
          (b3['text'] == 'X' and b7['text'] == 'X') or (b4['text'] == 'X' and b6['text'] == 'X')) and \
            b5['text'] == ' ':
        b5['text'] = 'O'

    elif ((b3['text'] == 'X' and b9['text'] == 'X') or (b4['text'] == 'X' and b5['text'] == 'X')) and b6['text'] == ' ':
        b6['text'] = 'O'

    elif ((b1['text'] == 'X' and b4['text'] == 'X') or (b3['text'] == 'X' and b5['text'] == 'X') or
          (b8['text'] == 'X' and b9['text'] == 'X')) and b7['text'] == ' ':
        b7['text'] = 'O'

    elif ((b2['text'] == 'X' and b5['text'] == 'X') or (b7['text'] == 'X' and b9['text'] == 'X')) and b8['text'] == ' ':
        b8['text'] = 'O'

    elif ((b1['text'] == 'X' and b5['text'] == 'X') or (b3['text'] == 'X' and b6['text'] == 'X') or
          (b7['text'] == 'X' and b8['text'] == 'X')) and b9['text'] == ' ':
        b9['text'] = 'O'

    # Stage 3: Random Move

    else:
        group = (b1, b2, b3, b4, b5, b6, b7, b8, b9)
        for i in range(0, len(group)):
            if safe(group[i]):
                group[i]['text'] = 'O'
                break


click = True
b = StringVar()
counter = 0


def play(c):

    global click
    global counter

    if c['text'] == ' ' and click:

        c['text'] = 'X'
        click = False
        win()

    elif not click:

        ai()
        click = True
        win()

    counter += 1

    if counter == 9:
        tkMessageBox.showinfo(title='Draw', message='It is a tie!')


window.mainloop()
