import random
import tkinter as tk
from tkinter import messagebox

def generate_secret_number(length):
    """生成指定位數的隨機不重複數字"""
    digits = list(range(10))
    random.shuffle(digits)
    return ''.join(map(str, digits[:length]))

def calculate_result(secret, guess):
    """計算猜測結果，返回A和B的數量"""
    A = sum(1 for s, g in zip(secret, guess) if s == g)
    B = sum(1 for g in guess if g in secret) - A
    return A, B

class ABGameApp:
    def __init__(self, root):
        self.root = root
        self.root.title("1A2B 遊戲")

        self.secret_number = ""
        self.attempts = 0
        
        self.setup_ui()

    def setup_ui(self):
        """設置遊戲的界面"""
        tk.Label(self.root, text="歡迎來到1A2B遊戲！", font=("Arial", 16)).pack(pady=10)

        tk.Label(self.root, text="請輸入想玩的數字位數 (2-9):").pack()
        self.length_entry = tk.Entry(self.root)
        self.length_entry.pack()

        self.start_button = tk.Button(self.root, text="開始遊戲", command=self.start_game)
        self.start_button.pack(pady=10)

        self.guess_label = tk.Label(self.root, text="")
        self.guess_label.pack()

        self.guess_entry = tk.Entry(self.root)
        self.guess_entry.pack()

        self.submit_button = tk.Button(self.root, text="提交猜測", command=self.submit_guess, state=tk.DISABLED)
        self.submit_button.pack(pady=10)

    def start_game(self):
        """開始遊戲並初始化設定"""
        try:
            length = int(self.length_entry.get())
            if 2 <= length <= 9:
                self.secret_number = generate_secret_number(length)
                self.attempts = 0
                self.guess_label.config(text=f"已生成一個 {length} 位數的隨機數字，請開始猜測！")
                self.submit_button.config(state=tk.NORMAL)
                self.length_entry.config(state=tk.DISABLED)
                self.start_button.config(state=tk.DISABLED)
            else:
                messagebox.showerror("錯誤", "請輸入2到9之間的數字！")
        except ValueError:
            messagebox.showerror("錯誤", "請輸入有效的數字！")

    def submit_guess(self):
        """處理玩家的猜測"""
        guess = self.guess_entry.get()
        length = len(self.secret_number)

        if len(guess) != length or not guess.isdigit() or len(set(guess)) != length:
            messagebox.showerror("錯誤", "輸入不合法，請輸入不重複的數字且長度正確。")
            return

        self.attempts += 1
        A, B = calculate_result(self.secret_number, guess)
        self.guess_label.config(text=f"結果: {A}A{B}B")

        if A == length:
            messagebox.showinfo("恭喜！", f"恭喜你猜對了！總共嘗試了 {self.attempts} 次。")
            self.reset_game()

    def reset_game(self):
        """重置遊戲狀態"""
        self.secret_number = ""
        self.attempts = 0
        self.guess_label.config(text="")
        self.length_entry.config(state=tk.NORMAL)
        self.start_button.config(state=tk.NORMAL)
        self.submit_button.config(state=tk.DISABLED)
        self.guess_entry.delete(0, tk.END)
        self.length_entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = ABGameApp(root)
    root.mainloop()
