import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self, master):
        self.master = master
        self.master.title("Tic Tac Toe - Human vs Human")
        
        self.current_player = "X"  # X starts the game
        self.board = [" " for _ in range(9)]
        self.buttons = []
        
        self.create_buttons()
        self.create_menu()
        
    def create_buttons(self):
        for i in range(9):
            button = tk.Button(self.master, text=" ", font=('Arial', 20), width=5, height=2,
                               command=lambda i=i: self.make_move(i))
            button.grid(row=i // 3, column=i % 3)
            self.buttons.append(button)

    def create_menu(self):
        menu = tk.Menu(self.master)
        self.master.config(menu=menu)
        
        game_menu = tk.Menu(menu)
        menu.add_cascade(label="Game", menu=game_menu)
        game_menu.add_command(label="Reset Game", command=self.reset_game)

    def make_move(self, index):
        if self.board[index] == " ":
            self.board[index] = self.current_player
            self.buttons[index].config(text=self.current_player)
            if self.check_winner():
                messagebox.showinfo("Game Over", f"Player {self.current_player} wins!")
                self.reset_game()
            elif " " not in self.board:
                messagebox.showinfo("Game Over", "It's a tie!")
                self.reset_game()
            else:
                self.current_player = "O" if self.current_player == "X" else "X"

    def check_winner(self):
        winning_combinations = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),  # horizontal
            (0, 3, 6), (1, 4, 7), (2, 5, 8),  # vertical
            (0, 4, 8), (2, 4, 6)               # diagonal
        ]
        for combo in winning_combinations:
            if self.board[combo[0]] == self.board[combo[1]] == self.board[combo[2]] != " ":
                return True
        return False

    def reset_game(self):
        self.current_player = "X"
        self.board = [" " for _ in range(9)]
        for button in self.buttons:
            button.config(text=" ")

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()