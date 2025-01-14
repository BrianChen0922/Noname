import tkinter as tk
from tkinter import messagebox

def calculate_result(secret, guess):
    """計算猜測結果，返回A和B的數量"""
    A = sum(1 for s, g in zip(secret, guess) if s == g)
    B = sum(1 for g in guess if g in secret) - A
    return A, B

class TwoPlayerABGameApp:
    def __init__(self, root):
        self.root = root
        self.root.title("1A2B 雙人遊戲")

        self.secret_number_p1 = ""
        self.secret_number_p2 = ""
        self.current_turn = "Player 1"
        self.attempts_p1 = 0
        self.attempts_p2 = 0

        self.setup_ui()

    def setup_ui(self):
        """設置遊戲的界面"""
        tk.Label(self.root, text="歡迎來到1A2B 雙人遊戲！", font=("Arial", 16)).pack(pady=10)

        tk.Label(self.root, text="請輸入想玩的數字位數 (2-9):").pack()
        self.length_entry = tk.Entry(self.root)
        self.length_entry.pack()

        self.start_button = tk.Button(self.root, text="開始遊戲", command=self.start_game)
        self.start_button.pack(pady=10)

        self.info_label = tk.Label(self.root, text="")
        self.info_label.pack()

        tk.Label(self.root, text="請輸入秘密數字 (玩家1):").pack()
        self.secret_entry_p1 = tk.Entry(self.root)
        self.secret_entry_p1.pack()

        tk.Label(self.root, text="請輸入秘密數字 (玩家2):").pack()
        self.secret_entry_p2 = tk.Entry(self.root)
        self.secret_entry_p2.pack()

        self.confirm_secrets_button = tk.Button(self.root, text="確認秘密數字", command=self.confirm_secrets, state=tk.DISABLED)
        self.confirm_secrets_button.pack(pady=10)

        self.guess_label = tk.Label(self.root, text="")
        self.guess_label.pack()

        self.guess_entry = tk.Entry(self.root)
        self.guess_entry.pack()

        self.submit_button = tk.Button(self.root, text="提交猜測", command=self.submit_guess, state=tk.DISABLED)
        self.submit_button.pack(pady=10)

    def start_game(self):
        """開始遊戲並初始化設定"""
        try:
            self.length = int(self.length_entry.get())
            if 2 <= self.length <= 9:
                self.info_label.config(text=f"已選擇 {self.length} 位數，請玩家1和玩家2輸入秘密數字。")
                self.confirm_secrets_button.config(state=tk.NORMAL)
                self.length_entry.config(state=tk.DISABLED)
                self.start_button.config(state=tk.DISABLED)
            else:
                messagebox.showerror("錯誤", "請輸入2到9之間的數字！")
        except ValueError:
            messagebox.showerror("錯誤", "請輸入有效的數字！")

    def confirm_secrets(self):
        """確認雙方的秘密數字"""
        secret_p1 = self.secret_entry_p1.get()
        secret_p2 = self.secret_entry_p2.get()

        if len(secret_p1) != self.length or not secret_p1.isdigit():
            messagebox.showerror("錯誤", "玩家1的秘密數字不合法，請重新輸入。")
            return

        if len(secret_p2) != self.length or not secret_p2.isdigit():
            messagebox.showerror("錯誤", "玩家2的秘密數字不合法，請重新輸入。")
            return

        self.secret_number_p1 = secret_p1
        self.secret_number_p2 = secret_p2
        self.info_label.config(text=f"秘密數字已確認，輪到 {self.current_turn} 猜測。")
        self.confirm_secrets_button.config(state=tk.DISABLED)
        self.secret_entry_p1.config(state=tk.DISABLED)
        self.secret_entry_p2.config(state=tk.DISABLED)
        self.submit_button.config(state=tk.NORMAL)

    def submit_guess(self):
        """處理玩家的猜測"""
        guess = self.guess_entry.get()

        if len(guess) != self.length or not guess.isdigit():
            messagebox.showerror("錯誤", "輸入不合法，請輸入正確長度的數字。")
            return

        if self.current_turn == "Player 1":
            self.attempts_p1 += 1
            A, B = calculate_result(self.secret_number_p2, guess)
            self.guess_label.config(text=f"玩家1的結果: {A}A{B}B")
            if A == self.length:
                messagebox.showinfo("恭喜！", f"玩家1獲勝！共嘗試了 {self.attempts_p1} 次。")
                self.reset_game()
                return
            self.current_turn = "Player 2"

        elif self.current_turn == "Player 2":
            self.attempts_p2 += 1
            A, B = calculate_result(self.secret_number_p1, guess)
            self.guess_label.config(text=f"玩家2的結果: {A}A{B}B")
            if A == self.length:
                messagebox.showinfo("恭喜！", f"玩家2獲勝！共嘗試了 {self.attempts_p2} 次。")
                self.reset_game()
                return
            self.current_turn = "Player 1"

        self.info_label.config(text=f"輪到 {self.current_turn} 猜測。")
        self.guess_entry.delete(0, tk.END)

    def reset_game(self):
        """重置遊戲狀態"""
        self.secret_number_p1 = ""
        self.secret_number_p2 = ""
        self.current_turn = "Player 1"
        self.attempts_p1 = 0
        self.attempts_p2 = 0
        self.info_label.config(text="")
        self.guess_label.config(text="")
        self.length_entry.config(state=tk.NORMAL)
        self.start_button.config(state=tk.NORMAL)
        self.confirm_secrets_button.config(state=tk.DISABLED)
        self.secret_entry_p1.config(state=tk.NORMAL)
        self.secret_entry_p2.config(state=tk.NORMAL)
        self.submit_button.config(state=tk.DISABLED)
        self.guess_entry.delete(0, tk.END)
        self.secret_entry_p1.delete(0, tk.END)
        self.secret_entry_p2.delete(0, tk.END)
        self.length_entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = TwoPlayerABGameApp(root)
    root.mainloop()

