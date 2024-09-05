import tkinter as tk
import tkinter.font as tkFont
from PIL import ImageTk, Image
from Battlefield import Battlefield
from Game import Game
from Halb import Halb
from Cav import Cav
from Musket import Musket
from Computer import Computer

import time
import threading


class App:

    def __init__(self, root):

        self.bf = Battlefield()
        root.title("Game")
        root.geometry("1000x800")

        self.musket = tk.PhotoImage(file="Musket.png")
        self.halbadier = tk.PhotoImage(file="Halbadier.png")
        self.knight = tk.PhotoImage(file="Knight.png")

        self.counter = 0
        self.lst = []
        self.lst.append((1, 2))
        self.lst.append((2, 3))
        self.lst.append((1, 9))

        frame = tk.Frame(root)
        frame.pack()
        self.cell1 = tk.Label(root, borderwidth=2, relief="solid")
        self.cell1.place(x=150, y=350, width=50, height=50)

        self.status1 = tk.Label(root, text="", fg="blue")
        self.status1.place(x=150, y=400, width=60, height=50)

        self.cell2 = tk.Label(root, borderwidth=2, relief="solid")
        self.cell2.place(x=220, y=350, width=50, height=50)

        self.status2 = tk.Label(root, text="", fg="blue")
        self.status2.place(x=220, y=400, width=60, height=50)

        self.cell3 = tk.Label(root, borderwidth=2, relief="solid")
        self.cell3.place(x=290, y=350, width=50, height=50)

        self.status3 = tk.Label(root, text="", fg="blue")
        self.status3.place(x=290, y=400, width=60, height=50)

        self.cell4 = tk.Label(root, borderwidth=2, relief="solid")
        self.cell4.place(x=360, y=350, width=50, height=50)

        self.status4 = tk.Label(root, text="", fg="blue")
        self.status4.place(x=360, y=400, width=60, height=50)

        self.cell5 = tk.Label(root, borderwidth=2, relief="solid")
        self.cell5.place(x=430, y=350, width=50, height=50)

        self.status5 = tk.Label(root, text="", fg="blue")
        self.status5.place(x=430, y=400, width=60, height=50)

        self.cell6 = tk.Label(root, borderwidth=2, relief="solid")
        self.cell6.place(x=500, y=350, width=50, height=50)

        self.status6 = tk.Label(root, text="", fg="blue")
        self.status6.place(x=500, y=400, width=60, height=50)

        self.cell7 = tk.Label(root, borderwidth=2, relief="solid")
        self.cell7.place(x=570, y=350, width=50, height=50)

        self.status7 = tk.Label(root, text="", fg="blue")
        self.status7.place(x=570, y=400, width=60, height=50)

        self.cell8 = tk.Label(root, borderwidth=2, relief="solid")
        self.cell8.place(x=640, y=350, width=50, height=50)

        self.status8 = tk.Label(root, text="", fg="blue")
        self.status8.place(x=640, y=400, width=60, height=50)

        self.cell9 = tk.Label(root, borderwidth=2, relief="solid")
        self.cell9.place(x=710, y=350, width=50, height=50)

        self.status9 = tk.Label(root, text="", fg="blue")
        self.status9.place(x=710, y=400, width=60, height=50)

        self.cell10 = tk.Label(root, borderwidth=2, relief="solid")
        self.cell10.place(x=780, y=350, width=50, height=50)

        self.status10 = tk.Label(root, text="", fg="blue")
        self.status10.place(x=780, y=400, width=60, height=50)

        self.list_of_cells = []
        self.list_of_cells.append(self.cell1)
        self.list_of_cells.append(self.cell2)
        self.list_of_cells.append(self.cell3)
        self.list_of_cells.append(self.cell4)
        self.list_of_cells.append(self.cell5)
        self.list_of_cells.append(self.cell6)
        self.list_of_cells.append(self.cell7)
        self.list_of_cells.append(self.cell8)
        self.list_of_cells.append(self.cell9)
        self.list_of_cells.append(self.cell10)

        self.list_of_status = []
        self.list_of_status.append(self.status1)
        self.list_of_status.append(self.status2)
        self.list_of_status.append(self.status3)
        self.list_of_status.append(self.status4)
        self.list_of_status.append(self.status5)
        self.list_of_status.append(self.status6)
        self.list_of_status.append(self.status7)
        self.list_of_status.append(self.status8)
        self.list_of_status.append(self.status9)
        self.list_of_status.append(self.status10)

        generate_random_units = tk.Button(root)
        generate_random_units["text"] = "Generate Random Units"
        generate_random_units.place(x=430, y=570, width=150, height=25)
        generate_random_units["command"] = self.generate_random_units

        self.set_units_label = tk.Label(root, text="Set units:")
        self.set_units_label.place(x=350, y=600, width=50, height=50)

        self.set_units_entry = tk.Entry(root)
        self.set_units_entry.place(x=410, y=610, width=200, height=30)

        set_units = tk.Button(root)
        set_units["text"] = "OK"
        set_units.place(x=620, y=610, width=30, height=30)
        set_units["command"] = self.set_units

        next_move = tk.Button(root)
        next_move["text"] = "Play next move"
        next_move.place(x=430, y=700, width=150, height=30)
        next_move["command"] = self.play_move

        self.init_state_easy = ['_', '_', '_', 'H', 'M', 'C', 'H', '_', '_', '_']

        self.moves = Computer().start("DFS")
        self.set_units_m(self.init_state_easy)
        root.mainloop()

    def generate_random_units(self):

        self.bf = Battlefield()
        self.bf.regroup()

        self.set_units_entry.delete(0, "end")
        self.set_units_entry.insert(0, ''.join(self.bf.init_state))

        for i in range(10):
            if type(self.bf.battlefield[i]) is Musket:
                self.list_of_cells[i].configure(image=self.musket)
            elif type(self.bf.battlefield[i]) is Halb:
                self.list_of_cells[i].configure(image=self.halbadier)
            elif type(self.bf.battlefield[i]) is Cav:
                self.list_of_cells[i].configure(image=self.knight)
            elif type(self.bf.battlefield[i]) is type(None):
                self.list_of_cells[i].configure(image='')
        self.set_default_status()

    def set_units(self):
        self.bf = Battlefield()
        self.bf.fill_battlefield(self.set_units_entry.get())
        self.bf.regroup()

    def set_units_m(self,units):
        self.bf = Battlefield(units)
       # self.bf.fill_battlefield(units)
        self.bf.regroup()

        for i in range(10):
            if type(self.bf.battlefield[i]) is Musket:
                self.list_of_cells[i].configure(image=self.musket)
            elif type(self.bf.battlefield[i]) is Halb:
                self.list_of_cells[i].configure(image=self.halbadier)
            elif type(self.bf.battlefield[i]) is Cav:
                self.list_of_cells[i].configure(image=self.knight)
            elif type(self.bf.battlefield[i]) is type(None):
                self.list_of_cells[i].configure(image='')
        self.set_default_status()

        for i in range(10):
            if type(self.bf.battlefield[i]) is Musket:
                self.list_of_cells[i].configure(image=self.musket)
            elif type(self.bf.battlefield[i]) is Halb:
                self.list_of_cells[i].configure(image=self.halbadier)
            elif type(self.bf.battlefield[i]) is Cav:
                self.list_of_cells[i].configure(image=self.knight)
            elif type(self.bf.battlefield[i]) is type(None):
                self.list_of_cells[i].configure(image='')
        self.set_default_status()

    def set_default_status(self):
        for i in range(10):
            if type(self.bf.battlefield[i]) is Musket:
                self.list_of_status[i]['text'] = 'AP : 2\nHP : 10'
            elif type(self.bf.battlefield[i]) is Halb:
                self.list_of_status[i]['text'] = 'AP : 2\nHP : 10'
            elif type(self.bf.battlefield[i]) is Cav:
                self.list_of_status[i]['text'] = 'AP : 3\nHP : 10'
            elif type(self.bf.battlefield[i]) is type(None):
                self.list_of_status[i]['text'] = ''

    def attack(self, pos1, pos2):
        canvas = tk.Canvas(root, width=680, height=20)
        canvas.place(x=150, y=300)
        line = canvas.create_line(70 * pos1 + 25, 10, 70 * pos2 + 25, 10, fill="red", arrow=tk.LAST)




    def swap(self, pos1, pos2):
        canvas = tk.Canvas(root, width=680, height=20)
        canvas.place(x=150, y=300)
        line = canvas.create_line(70 * pos1 + 25, 10, 70 * pos2 + 25, 10, fill="blue", arrow='both')

    def refresh_cells(self):
        for i in range(10):
            if self.bf.battlefield[i] is not None:
                if type(self.bf.battlefield[i]) is Musket:
                    self.list_of_cells[i].configure(image=self.musket)
                elif type(self.bf.battlefield[i]) is Halb:
                    self.list_of_cells[i].configure(image=self.halbadier)
                elif type(self.bf.battlefield[i]) is Cav:
                    self.list_of_cells[i].configure(image=self.knight)
                elif type(self.bf.battlefield[i]) is type(None):
                    self.list_of_cells[i].configure(image='')
                self.update_status(i,self.bf.battlefield[i].action_points,self.bf.battlefield[i].current_hp)
            else :
                self.list_of_cells[i].configure(image = "")

    def update_status(self, pos, ap, hp):
       self.list_of_status[pos]['text'] = "AP : " + str(ap) + "\nHP : " + str(hp) + ""
       #self.list_of_status[pos]['text'] = "AP : asdsadqweqweasdasdas" + str(ap) + "\nHP : " + str(hp) + "wefwefwef"

    def get_status(self,pos):
        return self.list_of_status[pos]['text']

    def self_play(self):
        # self.attack(0, 1)
        # self.attack(4, 5)
        print(self.e1.get() + " " + self.e2.get())
        self.attack(int(self.e1.get()), int(self.e2.get()))

        # .after(2000, self.delete_canvas())
        # self.attack(5, 6)
        # root.after(2000, self.delete_canvas())

        # self.update_status(4,5,5)

    def play_move(self):

        x = self.moves[self.counter][0]
        y = self.moves[self.counter][1]

        if x == 4 and y == 5 :
             self.attack(x,y)
        elif x != -1 :
             self.swap(x,y)

        self.bf.action(x, y)

        self.counter = self.counter + 1

        self.refresh_cells()


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
