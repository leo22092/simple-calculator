import tkinter as tk


class CalculatorUI:
    def __init__(self, calculator):
        self.calculator = calculator

        self.root = tk.Tk()
        self.root.title("Simple Calculator")

        # Input fields
        self.entry1 = tk.Entry(self.root)
        self.entry1.pack()

        self.entry2 = tk.Entry(self.root)
        self.entry2.pack()

        # Result label
        self.result_label = tk.Label(self.root, text="Result: ")
        self.result_label.pack()

        # Buttons
        tk.Button(self.root, text="Add",
                  command=self.add).pack()

        tk.Button(self.root, text="Subtract",
                  command=self.subtract).pack()

        tk.Button(self.root, text="Multiply",
                  command=self.multiply).pack()

        tk.Button(self.root, text="Divide",
                  command=self.divide).pack()

    def get_inputs(self):
        try:
            a = float(self.entry1.get())
            b = float(self.entry2.get())
            return a, b
        except ValueError:
            self.result_label.config(text="Invalid input")
            return None, None

    def add(self):
        a, b = self.get_inputs()
        if a is not None:
            result = self.calculator.add(a, b)
            self.result_label.config(text=f"Result: {result}")

    def subtract(self):
        a, b = self.get_inputs()
        if a is not None:
            result = self.calculator.subtract(a, b)
            self.result_label.config(text=f"Result: {result}")

    def multiply(self):
        a, b = self.get_inputs()
        if a is not None:
            result = self.calculator.multiply(a, b)
            self.result_label.config(text=f"Result: {result}")

    def divide(self):
        a, b = self.get_inputs()
        if a is not None:
            result = self.calculator.divide(a, b)
            self.result_label.config(text=f"Result: {result}")

    def run(self):
        self.root.mainloop()
