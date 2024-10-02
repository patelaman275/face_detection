import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import subprocess

def start_face_recognition():
    """
    Function to start the face recognition script.
    """
    try:
        subprocess.run(["python", "face_recognizer.py"])
    except Exception as e:
        messagebox.showerror("Error", f"Failed to start face recognition.\n{e}")

def on_closing():
    """
    Function to handle the window closing event.
    """
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        root.destroy()

root = tk.Tk()
root.title("Windows-like Face Recognition Lock Screen")

root.geometry("800x600")  

root.resizable(False, False)

frame = tk.Frame(root)
frame.pack(fill="both", expand=True)


bg_image = Image.open(r"C:\Users\patel\Downloads\FDS\real-time-face-recognition-master\real-time-face-recognition-master\bg.jpg")
bg_image = bg_image.resize((800, 600), Image.Resampling.LANCZOS)  
bg_image = ImageTk.PhotoImage(bg_image)

bg_label = tk.Label(frame, image=bg_image)
bg_label.place(relwidth=1, relheight=1)

title_label = tk.Label(frame, text="Welcome", font=("Segoe UI", 28), bg="#000000", fg="#FFFFFF")
title_label.place(relx=0.5, rely=0.2, anchor="center")

start_button = tk.Button(frame, text="Start Face Detection", font=("Segoe UI", 16), command=start_face_recognition, bg="#0078D7", fg="#FFFFFF", relief="flat", width=20, height=2)
start_button.place(relx=0.5, rely=0.5, anchor="center")

quit_button = tk.Button(frame, text="Quit", font=("Segoe UI", 14), command=on_closing, bg="#333333", fg="#FFFFFF", relief="flat", width=15, height=1)
quit_button.place(relx=0.5, rely=0.7, anchor="center")

root.protocol("WM_DELETE_WINDOW", on_closing)

root.mainloop()
