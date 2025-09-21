import tkinter as tk
from tkinter import ttk
from melody_generator import get_scale, root_to_midi, scales_intervals



# ---------------------------
# Tkinter UI
# ---------------------------
def show_scale():
    root_note = root_var.get()
    scale_type = scale_var.get()
    midi, names = get_scale(root_note, scale_type)

    result_text.set(f"MIDI: {midi}\nNotes: {', '.join(names)}")

# main window
win = tk.Tk()
win.title("Scale Explorer")
win.geometry("400x250")

# root note dropdown
tk.Label(win, text="Root Note:").pack(pady=5)
root_var = tk.StringVar(value="C")
root_menu = ttk.Combobox(win, textvariable=root_var, values=list(root_to_midi.keys()), state="readonly")
root_menu.pack(pady=5)

# scale type dropdown
tk.Label(win, text="Scale:").pack(pady=5)
scale_var = tk.StringVar(value="Major")
scale_menu = ttk.Combobox(win, textvariable=scale_var, values=list(scales_intervals.keys()), state="readonly")
scale_menu.pack(pady=5)

# button
tk.Button(win, text="Show Scale", command=show_scale).pack(pady=10)

# result
result_text = tk.StringVar()
result_label = tk.Label(win, textvariable=result_text, justify="left")
result_label.pack(pady=10)

win.mainloop()
