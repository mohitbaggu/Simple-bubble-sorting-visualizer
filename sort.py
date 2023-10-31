import tkinter as tk
import random
import time

def bubble_sort(arr, canvas, label):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                draw_bars(arr, canvas)
                update_label(arr, label)
                canvas.update_idletasks()
                time.sleep(0.1)

def draw_bars(arr, canvas):
    canvas.delete("all")
    canvas_width = 400
    canvas_height = 200
    bar_width = canvas_width / len(arr)
    max_val = max(arr)

    for i, val in enumerate(arr):
        bar_height = (val / max_val) * (canvas_height - 20)
        x1 = i * bar_width
        y1 = canvas_height - bar_height
        x2 = (i + 1) * bar_width
        y2 = canvas_height
        canvas.create_rectangle(x1, y1, x2, y2, fill="cyan")

def update_label(arr, label):
    label.config(text="Sorted Array: " + " ".join(map(str, arr)))

def start_sorting():
    input_arr = entry.get()
    try:
        arr = [int(x) for x in input_arr.split()]
    except ValueError:
        info_label.config(text="Invalid input.")
        return
    bubble_sort(arr, canvas, sorted_label)
    info_label.config(text="Sorting completed")

root = tk.Tk()
root.title("Bubble Sorting Visualizer")
root.geometry("500x400")

canvas = tk.Canvas(root, width=400, height=200)
canvas.pack()

entry_label = tk.Label(root, text="Enter numbers separated by spaces:")
entry_label.pack()
entry = tk.Entry(root)
entry.pack()

start_button = tk.Button(root, text="Start Sorting", command=start_sorting)
start_button.pack()

info_label = tk.Label(root, text="")
info_label.pack()

sorted_label = tk.Label(root, text="Sorted Array: ")
sorted_label.pack()

root.mainloop()
