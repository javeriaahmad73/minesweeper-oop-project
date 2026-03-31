##Tkinter is the standard GUI (Graphical User Interface) library for Python.
from tkinter import *
from cell import Cell
import settings
import utilities

def restart_game():
    root.destroy()   # closes current window
    import main      # runs the game again

##Tk is a class from the tkinter library.
root = Tk()
#override the settings of window
root.configure(bg="black")
root.geometry(f'{settings.width}x{settings.height}')
root.title("Minesweeper Game")
root.resizable(False,False)

top_frame=Frame(
    root,
    bg='red', #change later to black
    width=settings.width,
    height=utilities.height_perct(25)
    )
top_frame.place(x=0,y=0)
restart_button = Button(
    top_frame,
    text="Restart",
    width=10,
    height=2,
    command=restart_game
)
restart_button.place(x=10, y=10)

game_title=Label(
    top_frame,
    bg='black',
    fg='white',
    text='Minesweeper Game',
    font=('',30)
)
game_title.place(
    x=utilities.width_perct(25),y=0
)
left_frame =Frame(
    root,
    bg='blue', #change later to blue
    width=utilities.width_perct(25),
    height=utilities.height_perct(75)
)
left_frame.place(x=0,y=utilities.height_perct(25))

center_frame=Frame(
    root,
    bg='green',#change later to green
    width=utilities.width_perct(75),
    height=utilities.height_perct(75)
)
center_frame.place(
    x=utilities.width_perct(25),
    y=utilities.height_perct(25)
    )
for x in range(settings.GRID_SIZE):
    for y in range(settings.GRID_SIZE):
        c=Cell(x,y)
        c.create_btn_object(center_frame)
        c.cell_btn_object.grid(
            column=x,row=y
        )
#call the label from the cell class
Cell.create_cell_count_label(left_frame)
Cell.cell_count_label_object.place(x=0,y=0)


Cell.randomize_mines()





#run the window
root.mainloop()
