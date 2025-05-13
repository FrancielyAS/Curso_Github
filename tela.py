import tkinter as tk

janela = tk.Tk()

janela.title("Python")

janela.geometry("300x200")
mensagem = tk.Label(janela, text="Olá! Bem-vindo ao Curso de Git e Github da UNIFAVIP WYDEN 😊")

mensagem.pack()
janela.mainloop()
