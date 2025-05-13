import tkinter as tk


def responder():
    nome = entrada.get()
    resposta.config(text=f"Olá, {nome}!")

janela = tk.Tk()
janela.title("Pergunta ao Usuário")
janela.geometry("300x200")


pergunta = tk.Label(janela, text="Qual é o seu nome?")
pergunta.pack(pady=10)

entrada = tk.Entry(janela)
entrada.pack()


botao = tk.Button(janela, text="Responder", command=responder)
botao.pack(pady=10)

resposta = tk.Label(janela, text="")
resposta.pack()

janela.mainloop()
