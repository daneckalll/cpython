```python
import tkinter as tk
from tkinter import messagebox

class Account:
    def __init__(self, account_number, owner):
        self.account_number = account_number
        self.owner = owner
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            raise ValueError("Недостаточно средств.")

    def get_balance(self):
        return self.balance

class GBankApp:
    def __init__(self, root):
        self.root = root
        self.root.title("G-Банк")
        self.accounts = {}
        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.root, text="Имя владельца:").grid(row=0, column=0)
        self.owner_entry = tk.Entry(self.root)
        self.owner_entry.grid(row=0, column=1)

        tk.Button(self.root, text="Открыть аккаунт", command=self.open_account).grid(row=1, column=0, columnspan=2)

        tk.Label(self.root, text="Номер аккаунта:").grid(row=2, column=0)
        self.acc_number_entry = tk.Entry(self.root)
        self.acc_number_entry.grid(row=2, column=1)

        tk.Label(self.root, text="Сумма:").grid(row=3, column=0)
        self.amount_entry = tk.Entry(self.root)
        self.amount_entry.grid(row=3, column=1)

        tk.Button(self.root, text="Внести средства", command=self.deposit).grid(row=4, column=0)
        tk.Button(self.root, text="Снять средства", command=self.withdraw).grid(row=4, column=1)
        tk.Button(self.root, text="Проверить баланс", command=self.check_balance).grid(row=5, column=0, columnspan=2)

    def open_account(self):
        owner = self.owner_entry.get()
        if owner:
            account_number = len(self.accounts) + 1
            self.accounts[account_number] = Account(account_number, owner)
            messagebox.showinfo("Успех", f"Аккаунт открыт. Номер аккаунта: {account_number}")
        else:
            messagebox.showwarning("Ошибка", "Введите имя владельца.")

    def deposit(self):
        acc_number = int(self.acc_number_entry.get())
        amount = float(self.amount_entry.get())
        if acc_number in self.accounts:
            self.accounts[acc_number].deposit(amount)
            messagebox.showinfo("Успех", f"Внесено: {amount}. Текущий баланс: {self.accounts[acc_number].get_balance()}.")
        else:
            messagebox.showwarning("Ошибка", "Аккаунт не найден.")

    def withdraw(self):
        acc_number = int(self.acc_number_entry.get())
        amount = float(self.amount_entry.get())
        if acc_number in self.accounts:
            try:
                self.accounts[acc_number].withdraw(amount)
                messagebox.showinfo("Успех", f"Снято: {amount}. Текущий баланс: {self.accounts[acc_number].get_balance()}.")
            except ValueError as e:
                messagebox.showwarning("Ошибка", str(e))
        else:
            messagebox.showwarning("Ошибка", "Аккаунт не найден.")

    def check_balance(self):
        acc_number = int(self.acc_number_entry.get())
        if acc_number in self.accounts:
            balance = self.accounts[acc_number].get_balance()
            messagebox.showinfo("Баланс", f"Баланс аккаунта {acc_number}: {balance}.")
        else:
            messagebox.showwarning("Ошибка", "Аккаунт не найден.")

if __name__ == "__main__":
    root = tk.Tk()
    app = GBankApp(root)
    root.mainloop()
```
