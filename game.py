import tkinter as tk
from tkinter import messagebox
import random
import os

GRID_SIZE = 10
NUM_MINES = 10

class MinesweeperGame:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Сапёр")
        self.root.iconbitmap("game.ico")
        self.root.geometry("300x400")  # Фиксированный размер окна
        self.root.resizable(False, False)  # Запрет изменения размера окна
        self.center_window()

        self.buttons = [[None for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
        self.grid = [[0 for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]

        self.result_label = tk.Label(self.root, text="", font=("Helvetica", 16))
        self.result_label.grid(row=0, column=0, columnspan=GRID_SIZE)

        self.menu_button = tk.Button(self.root, text="В меню", command=self.go_to_menu, state="disabled")
        self.menu_button.grid(row=1, column=0, columnspan=GRID_SIZE//2, pady=(10, 0))

        self.quit_button = tk.Button(self.root, text="Выйти из игры", command=self.quit_game, state="disabled")
        self.quit_button.grid(row=1, column=GRID_SIZE//2, columnspan=GRID_SIZE//2, pady=(10, 0))

        self.create_grid()

    def center_window(self):
        w = 300
        h = 400

        ws = self.root.winfo_screenwidth()
        hs = self.root.winfo_screenheight()

        x = (ws/2) - (w/2)
        y = (hs/2) - (h/2)

        self.root.geometry('%dx%d+%d+%d' % (w, h, x, y))

    def create_grid(self):
        for i in range(GRID_SIZE):
            for j in range(GRID_SIZE):
                btn = tk.Button(self.root, width=3, height=1, command=lambda i=i, j=j: self.click(i, j))
                btn.grid(row=i+2, column=j)
                self.buttons[i][j] = btn

        mines = random.sample(range(GRID_SIZE**2), NUM_MINES)
        for mine in mines:
            row = mine // GRID_SIZE
            col = mine % GRID_SIZE
            self.grid[row][col] = -1

        for i in range(GRID_SIZE):
            for j in range(GRID_SIZE):
                if self.grid[i][j] != -1:
                    for x in range(max(0, i-1), min(GRID_SIZE, i+2)):
                        for y in range(max(0, j-1), min(GRID_SIZE, j+2)):
                            if self.grid[x][y] == -1:
                                self.grid[i][j] += 1

    def click(self, i, j):
        if self.result_label.cget("text") == "Проигрыш" or self.result_label.cget("text") == "Победа":
            return

        if self.grid[i][j] == -1:
            self.result_label.config(text="Проигрыш", fg="red")
            self.reveal_mines()
            self.disable_buttons()
            self.menu_button.config(state="normal")
            self.quit_button.config(state="normal")
        else:
            self.buttons[i][j].config(text=str(self.grid[i][j]), state="disabled")
            if self.grid[i][j] == 0:
                for x in range(max(0, i-1), min(GRID_SIZE, i+2)):
                    for y in range(max(0, j-1), min(GRID_SIZE, j+2)):
                        if self.grid[x][y] != -1 and self.buttons[x][y]["state"] == "normal":
                            self.click(x, y)

    def reveal_mines(self):
        for i in range(GRID_SIZE):
            for j in range(GRID_SIZE):
                if self.grid[i][j] == -1:
                    self.buttons[i][j].config(text="*", state="disabled", bg="red")

    def go_to_menu(self):
        self.root.destroy()
        os.system('python menu.py')

    def quit_game(self):
        self.root.destroy()

    def disable_buttons(self):
        for i in range(GRID_SIZE):
            for j in range(GRID_SIZE):
                self.buttons[i][j].config(state="disabled")

if __name__ == "__main__":
    game = MinesweeperGame()
    game.root.mainloop()
