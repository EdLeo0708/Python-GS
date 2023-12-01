import tkinter as tk
from tkinter import messagebox
import webbrowser

def obter_numeros_do_usuario():
    "Uma lista de números do usuário."
    try:
        numeros = entrada_numeros.get()
        numeros = [float(numero) for numero in numeros.split()]
        return numeros
    except ValueError:
        messagebox.showerror("Erro", "Certifique-se de inserir apenas números.")
        return []

def calcular_media():
    "Verificação de Código do Produto."
    numeros_usuario = obter_numeros_do_usuario()
    media_resultado = sum(numeros_usuario) / len(numeros_usuario) if numeros_usuario else 0
    resultado_label.config(text=f"O N°:{media_resultado:.2f} do produto foi aceito")

def abrir_gmail():
    webbrowser.open("https://mail.google.com")

# Criar a janela principal
janela = tk.Tk()
janela.title("Inserir Código")

# Criar widgets
tk.Label(janela, text="Insira uma lista de números separados por espaços:").pack(pady=10)
entrada_numeros = tk.Entry(janela, width=50)
entrada_numeros.pack(pady=10)

calcular_botao = tk.Button(janela, text="Inserir Código", command=calcular_media)
calcular_botao.pack(pady=10)

resultado_label = tk.Label(janela, text="")
resultado_label.pack(pady=10)

abrir_gmail_botao = tk.Button(janela, text="Abrir Gmail", command=abrir_gmail)
abrir_gmail_botao.pack(pady=10)

# Iniciar o loop principal
janela.mainloop()
