import tkinter as tk
from calcu.main import calculate

class CalculatorUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Calcu")
        self.geometry("300x400")
        self.resizable(False, False)
        
        self.display_var = tk.StringVar()
        
        display = tk.Entry(self, textvariable=self.display_var, font=('Arial', 24), bd=10, insertwidth=2, width=14, borderwidth=4, justify='right')
        display.grid(row=0, column=0, columnspan=4)
        
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            'C', '0', '=', '+'
        ]
        
        row_val = 1
        col_val = 0
        
        for button in buttons:
            action = lambda x=button: self.on_button_click(x)
            tk.Button(self, text=button, padx=20, pady=20, font=('Arial', 18), command=action).grid(row=row_val, column=col_val, sticky="nsew")
            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1
                
        for i in range(4):
            self.grid_columnconfigure(i, weight=1)
        for i in range(1, 5):
            self.grid_rowconfigure(i, weight=1)

    def on_button_click(self, char):
        if char == 'C':
            self.display_var.set("")
        elif char == '=':
            try:
                result = str(calculate(self.display_var.get()))
                if result.startswith("Error"):
                    self.display_var.set("Error")
                else:
                    self.display_var.set(result)
            except Exception:
                self.display_var.set("Error")
        else:
            current_text = self.display_var.get()
            if current_text == "Error":
                current_text = ""
            self.display_var.set(current_text + char)

def run_ui():
    app = CalculatorUI()
    app.mainloop()
