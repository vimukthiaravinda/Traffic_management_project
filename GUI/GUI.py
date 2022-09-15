import tkinter as tk
from tkinter import ttk

numberofVehicals = 0
numberofBuses = 0
numberofCars = 0
numberofThreeWheels = 0
densityofTraffic = 0
types = ("Car", "Bus", "Three wheel")


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.option_variables = tk.StringVar(self)
        self.title('Traffic simulator')
        self.geometry('1920x1080')
        self.label = ttk.Label(self, text='Total Number of Vehicles :', font=13)
        self.label.place(x=1580, y=30)
        self.label2 = ttk.Label(self, text=numberofVehicals, font=('Helvetica', 13))
        self.label2.place(x=1800, y=30)
        self.label3 = ttk.Label(self, text="Number of Bus :", font=('Helvetica', 13))
        self.label3.place(x=1600, y=80)
        self.label4 = ttk.Label(self, text=numberofBuses, font=('Helvetica', 13))
        self.label4.place(x=1800, y=80)
        self.label5 = ttk.Label(self, text="Number of Car :", font=('Helvetica', 13))
        self.label5.place(x=1600, y=120)
        self.label5 = ttk.Label(self, text=numberofCars, font=('Helvetica', 13))
        self.label5.place(x=1800, y=120)
        self.label6 = ttk.Label(self, text="Number of Three wheel :", font=('Helvetica', 13))
        self.label6.place(x=1600, y=160)
        self.label6 = ttk.Label(self, text=numberofThreeWheels, font=('Helvetica', 13))
        self.label6.place(x=1800, y=160)
        self.label6 = ttk.Label(self, text="Density of Traffic:", font=('Helvetica', 13))
        self.label6.place(x=1600, y=200)
        self.label6 = ttk.Label(self, text=densityofTraffic, font=('Helvetica', 13))
        self.label6.place(x=1800, y=200)
        self.option = ttk.OptionMenu(self, self.option_variables, types[0], *types)
        self.option.place(x=1600, y=240)
        curretvalue = tk.StringVar(value=0)
        self.spinbox = ttk.Spinbox(self, from_=0, to=20, textvariable=curretvalue, wrap=0)
        self.spinbox.place(x=1700, y=240)
        self.addVEHICLES = ttk.Button(self, text="ADD VEHICLES")
        self.addVEHICLES.place(x=1650, y=280)
        self.label7 = ttk.Label(self, text="Density of Traffic", font=13)
        self.label7.place(x=1650, y=320)
        self.slider = ttk.Scale(self, from_=0, to=100, orient='horizontal')
        self.slider.place(x=1650, y=350)
        self.label8 = ttk.Label(self, text=densityofTraffic, font=13)
        self.label8.place(x=1800, y=320)
        self.canvas = tk.Canvas(self, background='white', height=100, width=200)
        self.canvas.place(x=1630, y=380)
        self.addLane = ttk.Button(self, text="+")
        self.addLane.place(x=1650, y=520)
        self.reLane = ttk.Button(self, text="-")
        self.reLane.place(x=1750, y=520)


if __name__ == "__main__":
    app = App()
    app.mainloop()
