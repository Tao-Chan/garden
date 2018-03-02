import tkinter as tk
from tkinter import ttk
import garden
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


def drawPic():
    drawPic.f.clf()
    drawPic.a = drawPic.f.add_subplot(233)
    garden.drawGarden(numberchose.get())
    action.configure(state='disabled')

top = tk.Tk()
top.title('植物图形生成')
drawPic.f = Figure(figsize=(5, 5), dpi=100)
drawPic.canvas = FigureCanvasTkAgg(drawPic.f, master=top)
drawPic.canvas.show()
drawPic.canvas.get_tk_widget().grid(row=0, column=0)
action = ttk.Button(top, text='确定', command=drawPic)
number = tk.StringVar()
numberchose = ttk.Combobox(top, textvariable=number, state='readonly')
numberchose['values'] = (1, 2, 3, 4)
action.grid(row=0, column=2)
numberchose.grid(row=0, column=1)
tk.mainloop()

