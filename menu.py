import tkinter as tk
import webbrowser
import os
import threading

def play_game():
    threading.Thread(target=os.system, args=("python game.py",)).start()
    root.destroy()

def open_github():
    webbrowser.open('https://github.com/gghj31621')

root = tk.Tk()
root.title("Меню")
root.geometry("920x432")
root.resizable(width=False, height=False)  # Запрет изменения размера
root.iconbitmap("home.ico")

background_image = tk.PhotoImage(file="background.png")
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)

title_label = tk.Label(root, text="САПЁР", font=("Tahoma", 36), fg="black")
title_label.place(relx=0.5, rely=0.2, anchor="center")

play_button = tk.Button(root, text="Play", font=("Tahoma", 18), command=play_game, bg="white", padx=20, pady=10, bd=0, cursor="hand2")
play_button.place(relx=0.5, rely=0.4, anchor="center", width=160, height=60)

github_button = tk.Button(root, text="GitHub", font=("Tahoma", 18), command=open_github, bg="white", padx=20, pady=10, bd=0, cursor="hand2")
github_button.place(relx=0.5, rely=0.6, anchor="center", width=160, height=60)

root.mainloop()
