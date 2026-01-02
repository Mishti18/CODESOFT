import tkinter as tk
from tkinter import messagebox
import winsound  # For sound effects (Windows only; remove if on other OS)

class PlayfulTicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("🎉 Playful Tic-Tac-Toe! 🎉")
        self.root.geometry("400x500")
        self.root.configure(bg="#C0C0C0")  # Silver background
        self.board = [[" " for _ in range(3)] for _ in range(3)]
        self.current_player = "X"
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        self.create_ui()

    def create_ui(self):
        # Title label
        title = tk.Label(self.root, text="Tic-Tac-Toe GO!", font=("PRINCETOWN", 24, "bold"), bg="#EDDA74", fg="#800000")
        title.pack(pady=10)
        
        # Game grid frame
        frame = tk.Frame(self.root, bg="#800517")
        frame.pack()
        
        for i in range(3):
            for j in range(3):
                self.buttons[i][j] = tk.Button(frame, text=" ", font=("Arial", 40, "bold"), width=3, height=1,
                                               bg="#FFFACD", fg="#000", relief="raised", bd=5,
                                               command=lambda row=i, col=j: self.make_move(row, col))
                self.buttons[i][j].bind("<Enter>", lambda e, btn=self.buttons[i][j]: btn.config(bg="#FFFF00"))  # Yellow on hover
                self.buttons[i][j].bind("<Leave>", lambda e, btn=self.buttons[i][j]: btn.config(bg="#FFFACD"))  # Back to cream
                self.buttons[i][j].grid(row=i, column=j, padx=5, pady=5)
        
        # Reset button
        reset_btn = tk.Button(self.root, text="🔄 Reset Game", font=("Comic Sans MS", 14), bg="#98FB98", fg="#000",
                              command=self.reset_game)
        reset_btn.pack(pady=20)

    def make_move(self, row, col):
        if self.board[row][col] == " ":
            self.board[row][col] = self.current_player
            emoji = "❌" if self.current_player == "X" else "⭕"
            self.buttons[row][col].config(text=emoji, bg="#ADFF2F" if self.current_player == "X" else "#FFA07A")  # Green for X, light salmon for O
            winsound.Beep(800, 200) if self.current_player == "X" else winsound.Beep(600, 200)  # Fun beeps
            
            if self.check_winner(self.current_player):
                messagebox.showinfo("🎉 Yay!", f"{emoji} Player Wins! 🎊")
                winsound.Beep(1000, 500)  # Win sound
                self.reset_game()
            elif self.is_draw():
                messagebox.showinfo("🤝 Oops!", "It's a Draw! 🤷‍♂️")
                winsound.Beep(400, 500)  # Draw sound
                self.reset_game()
            else:
                self.current_player = "O" if self.current_player == "X" else "X"

    def check_winner(self, player):
        for i in range(3):
            if all(self.board[i][j] == player for j in range(3)) or all(self.board[j][i] == player for j in range(3)):
                return True
        if all(self.board[i][i] == player for i in range(3)) or all(self.board[i][2-i] == player for i in range(3)):
            return True
        return False

    def is_draw(self):
        return all(cell != " " for row in self.board for cell in row)

    def reset_game(self):
        self.board = [[" " for _ in range(3)] for _ in range(3)]
        self.current_player = "X"
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].config(text=" ", bg="#FFFACD")

if __name__ == "__main__":
    root = tk.Tk()
    game = PlayfulTicTacToe(root)
    root.mainloop()
