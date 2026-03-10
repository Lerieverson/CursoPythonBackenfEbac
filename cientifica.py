import tkinter as tk
import math


def clicar(valor):
    atual = entrada.get()
    entrada.delete(0, tk.END)
    entrada.insert(tk.END, atual + str(valor))


def limpar():
    entrada.delete(0, tk.END)


def calcular():
    try:
        expressao = entrada.get()
        # Permite uso seguro de funções matemáticas
        resultado = eval(expressao, {"__builtins__": None}, {
            "sqrt": math.sqrt,
            "sin": lambda x: math.sin(math.radians(x)),
            "cos": lambda x: math.cos(math.radians(x)),
            "tan": lambda x: math.tan(math.radians(x)),
            "log": math.log10,
            "pi": math.pi,
            "e": math.e,
            "pow": pow
        })
        entrada.delete(0, tk.END)
        entrada.insert(tk.END, str(resultado))
    except:
        entrada.delete(0, tk.END)
        entrada.insert(tk.END, "Erro")


# Janela principal
janela = tk.Tk()
janela.title("Calculadora Científica")
janela.geometry("400x600")
janela.resizable(False, False)

# Display
entrada = tk.Entry(janela, font=("Arial", 20), borderwidth=5, relief="ridge", justify="right")
entrada.pack(fill="both", ipadx=8, ipady=15, padx=10, pady=10)

# Frame dos botões
frame = tk.Frame(janela)
frame.pack()

# Layout dos botões
botoes = [
    ["7", "8", "9", "/", "sqrt("],
    ["4", "5", "6", "*", "pow("],
    ["1", "2", "3", "-", "log("],
    ["0", ".", "+", "=", "C"],
    ["sin(", "cos(", "tan(", "pi", "e"]
]

for linha in botoes:
    linha_frame = tk.Frame(frame)
    linha_frame.pack(expand=True, fill="both")
    for botao in linha:
        b = tk.Button(
            linha_frame,
            text=botao,
            font=("Arial", 14),
            relief="ridge",
            borderwidth=2,
            command=lambda b=botao: (
                calcular() if b == "=" else
                limpar() if b == "C" else
                clicar(b)
            )
        )
        b.pack(side="left", expand=True, fill="both")


janela.mainloop()