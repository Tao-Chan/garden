# -*- coding: utf-8 -*-
#L-System(Lindenmayer system)是一种用字符串替代产生分形图形的算法
from math import sin, cos, pi
import matplotlib.pyplot as pl
from matplotlib import collections
import tkinter as tk
from tkinter import ttk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from random import choice
class L_System(object):
    def __init__(self, rule):
        info = rule['S']
        for i in range(rule['iter']):
            ninfo = []
            for c in info:
                if c in rule:
                    ninfo.append(rule[c])
                else:
                    ninfo.append(c)
            info = "".join(ninfo)
        self.rule = rule
        self.info = info

    def get_lines(self):
        d = self.rule['direct']
        a = self.rule['angle']
        p = (0.0, 0.0)
        l = 1.0
        lines = []
        stack = []
        for c in self.info:
            if c in "Ff":
                r = d * pi / 180
                t = p[0] + l * cos(r), p[1] + l * sin(r)
                lines.append(((p[0], p[1]), (t[0], t[1])))
                p = t
            elif c == "+":
                d += a
            elif c == "-":
                d -= a
            elif c == "[":
                stack.append((p, d))
            elif c == "]":
                p, d = stack[-1]
                del stack[-1]
        return lines


'''

    F ,f: 向前走固定单位
    + : 正方向旋转固定单位
    - : 负方向旋转固定单位
    [ : 将当前的位置入堆栈
    ] : 从堆栈中读取坐标，修改当前位置
    S : 初始迭代符号
    direct : 是绘图的初始角度，通过指定不同的值可以旋转整个图案
    angle : 定义符号+,-旋转时的角度，不同的值能产生完全不同的图案
    iter : 迭代次数

'''
rules = [

    {
        "X": "F-[[X]+X]+F[+FX]-X", "F": "FF", "S": "X",
        "direct": -90,
        "angle": 25,
        "iter": 6,
        "title": "Plant0"
    },
    {
        "S": "F", "F": "F[+F]F[-F]F",
        "direct": -90,
        "angle": 25,
        "iter": 4,
        "title": "Plant1"
    },
    {
        "S": "F", "F": "F[+F][-F]F",
        "direct": -90,
        "angle": 25,
        "iter": 4,
        "title": "Plant2"
    },
    {
        "S": "F", "F": "FF+[+F-F-F]-[-F+F+F]",
        "direct": -90,
        "angle": 25,
        "iter": 4,
        "title": "Plant3"
    },

]


def draw(ax, rule, iter=None):
    if iter != None:
        rule["iter"] = iter
    lines = L_System(rule).get_lines()
    linecollections = collections.LineCollection(lines)
    ax.add_collection(linecollections, autolim=True)
    ax.axis("equal")
    ax.set_axis_off()
    ax.set_xlim(ax.dataLim.xmin, ax.dataLim.xmax)
    ax.invert_yaxis()


def drawPic():
    drawPic.f.clf()
    ax = drawPic.f.add_subplot(111)
    draw(ax, rules[int(numberchose.get()) - 1])
    #drawPic.subplots_adjust(left=0, right=1, bottom=0, top=1, wspace=0, hspace=0)
    drawPic.canvas.show()


if __name__ == '__main__':
    top = tk.Tk()
    top.title('植物图形生成')
    #在GUI上放置画布
    drawPic.f = Figure(figsize=(5, 5), dpi=100)
    drawPic.canvas = FigureCanvasTkAgg(drawPic.f, master=top)
    drawPic.canvas.show()
    drawPic.canvas.get_tk_widget().grid(row=0, column=0)
    #按钮及下拉框部件
    number = tk.StringVar()
    numberchose = ttk.Combobox(top, textvariable=number, state='readonly')
    numberchose['values'] = (1, 2, 3, 4)
    action = ttk.Button(top, text='确定', command=drawPic)
    action.grid(row=0, column=2)
    numberchose.grid(row=0, column=1)
    top.mainloop()
    # fig = pl.figure(figsize=(3, 3))
    # fig.patch.set_facecolor("w")
    # ax = drawPic.add_subplot(111)
    # draw(ax, rules[0])
    # drawPic.subplots_adjust(left=0, right=1, bottom=0, top=1, wspace=0, hspace=0)
    #pl.show()
# for i in range(4):
#     ax = fig.add_subplot(231 + i)
#     draw(ax, rules[i])

