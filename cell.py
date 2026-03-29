from tkinter import Button,Label
import random #random has very specific  method that is responsible  to pick randomly some elemnts from the given collection
import settings
import ctypes
from tkinter import messagebox
import sys

class Cell:
    all=[]
    cell_count=settings.CELL_COUNT
    cell_count_label_object=None
    def __init__(self,x,y,is_mine=False):
        self.is_mine=is_mine
        self.is_opened=False
        self.is_mine_candidate=False
        self.cell_btn_object=None
        self.x=x
        self.y=y


        #Append the object to the cell.all list
        Cell.all.append(self)

    def create_btn_object(self,location):
        btn=Button(
            location,
            width=12,
            height=4,
           
        )
        btn.bind('<Button-1>',self.left_click_actions)#left click 
        btn.bind('<Button-3>',self.right_click_actions)#right click
        self.cell_btn_object=btn
    @staticmethod
    def create_cell_count_label(location):
        lbl=Label(
            location,
            bg='black',
            fg='white',
            text=f"cells left:{Cell.cell_count}",
            width=12,
            height=4,
            font=("",15)

        )
        Cell.cell_count_label_object=lbl


    def left_click_actions(self,event):
        if self.is_mine:
            self.show_mine()
        else:
            if self.surrounded_cells_mines_length==0:
                for cell_obj in self.surrounded_cells:
                    cell_obj.show_cell()

            self.show_cell()
            #if mnines count is equal to the cells left count,player won
            if Cell.cell_count==settings.MINES_COUNT:
                 ctypes.windll.user32.MessageBoxW(0,'conratulations! you won the game','Game over',0)





        #cancel left and right click events if cell is already opened:
        self.cell_btn_object.unbind('<Button-1>')
        self.cell_btn_object.unbind('<Button-3>')

    def get_cell_by_axis(self,x,y):
        #returb a cell object based on the values of x and y
        for cell in Cell.all:   # ✅ FIXED HERE
            if cell.x==x and cell.y==y:
                return cell
    

    @property
    def surrounded_cells(self):
            cells=[
            self.get_cell_by_axis(self.x-1,self.y-1),
            self.get_cell_by_axis(self.x-1,self.y),
            self.get_cell_by_axis(self.x-1,self.y+1),
            self.get_cell_by_axis(self.x,self.y-1),
            self.get_cell_by_axis(self.x+1,self.y-1),
            self.get_cell_by_axis(self.x+1,self.y),
            self.get_cell_by_axis(self.x+1,self.y+1),
            self.get_cell_by_axis(self.x,self.y+1),

            ]
            cells=[cell for cell in cells if cell is not None]
            return cells
    
    @property
    def surrounded_cells_mines_length(self):
        counter=0
        for cell in self.surrounded_cells:
            if cell.is_mine:
                counter+=1

        return counter


    def show_cell(self):
        if not self.is_opened:

            Cell.cell_count-=1
            self.cell_btn_object.configure(text=self.surrounded_cells_mines_length)
            #replace the text of cell count label with the newer count
            if Cell.cell_count_label_object:
                Cell.cell_count_label_object.configure(
                    text=f"cells left:{Cell.cell_count}"
                )
                #if this was a mine candidate ,we should 
                #configure the background color to systemButtonFace
                self.cell_btn_object.configure(
                    bg='systemButtonFace'
                )
        #marked the cell as opened(use is as the last line of this method)
        self.is_opened=True

    def show_mine(self):
        self.cell_btn_object.configure(bg='red')
        ctypes.windll.user32.MessageBoxW(0,'you clicked on mine','Game over',0)
        sys.exit()
        

    
        # print(event)
        # print("I am left clicked")

    def right_click_actions(self,event):
        if not self.is_mine_candidate:
            self.cell_btn_object.configure(
                bg='orange'
            )
            self.is_mine_candidate=True
        else:
            self.cell_btn_object.configure(
                bg='SystemButtonFace'
            )
            self.is_mine_candidate=False



    @staticmethod
    def randomize_mines():
  
        picked_cells=random.sample(
            Cell.all, settings.MINES_COUNT
            )
        for picked_cell in picked_cells:
            picked_cell.is_mine=True
       

    def __repr__(self):
        return f"cell({self.x},{self.y})"