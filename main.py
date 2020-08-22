from tkinter import *
from tkinter import ttk
import random
from algorithms import bubble_sort, merge_sort

#window
root = Tk()
root.title('Sorting Algorithm Visualizer')
root.maxsize(900, 600)
root.config(bg='black')

data = []
canvas_height = 380
canvas_width = 600
selected_alg = StringVar()

#functions
def drawData(data, colorArray):
    canvas.delete('all') 
    bar_w = canvas_width / len(data)
    scaleBars = [i / max(data) for i in data]
    for i, height in enumerate(scaleBars):
        x0 = i * bar_w 
        y0 = canvas_height - height * (canvas_height - 20)
        x1 = (i + 1) * bar_w
        y1 = canvas_height
        canvas.create_rectangle(x0, y0, x1, y1, fill=colorArray[i], outline='')
    root.update_idletasks()
    
def generate():
    global data
    data = []
    size = int(sizeEntry.get())
    for _ in range(size):
        data.append(random.randrange(1, size + 1))
    drawData(data, ['red' for x in range(len(data))])

def startAlgo():
    global data
    if algoMenu.get() == 'Bubble Sort':
        bubble_sort(data, drawData)
    elif algoMenu.get() == 'Merge Sort':
        merge_sort(data, drawData)
    
#UI
UI_frame = Frame(root, width=600, height=200, bg='grey')
UI_frame.grid(row=0, column=0, padx=10, pady=5)

Label(UI_frame, text="Algorithm: ", bg='grey').grid(row=0, column=0, padx=5, pady=5, sticky=W)
algoMenu = ttk.Combobox(UI_frame, textvariable=selected_alg, values=['Bubble Sort', 'Merge Sort'])
algoMenu.grid(row=0, column=1, padx=5, pady=5)
algoMenu.current(0)

Label(UI_frame, text='Size', bg='grey').grid(row=1, column=0, padx=5, pady=5, sticky=W)
sizeEntry = Entry(UI_frame)
sizeEntry.grid(row=1, column=1, padx=5, pady=5, sticky=W)
Button(UI_frame, text='Generate', command=generate, bg='red').grid(row=0, column=2, padx=5, pady=5)
Button(UI_frame, text='Start', command=startAlgo, bg='red').grid(row=1, column=2, padx=5, pady=5)

#canvas
canvas = Canvas(root, width=canvas_width, height=canvas_height, bg='white')
center = canvas_width / 2
canvas.grid(row=1, column=0, padx=10, pady=5)

root.mainloop()