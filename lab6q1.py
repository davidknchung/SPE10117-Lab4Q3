from tkinter import Tk, Canvas
frame=Tk()
canvas=Canvas(height=250,width=600)
canvas.create_rectangle(10, 10, 250, 150, fill='red', outline='blue')
canvas.create_text(100, 100, text='David Chung')
canvas.create_line(50, 110, 150, 110)
canvas.pack()
frame.mainloop()
