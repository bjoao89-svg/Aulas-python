import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox

# ---------------- FUNÇÃO PRINCIPAL ----------------

def organizar_pasta():
    pasta = filedialog.askdirectory()

    if not pasta:
        return

    tipos = {
        "Imagens": [".jpg", ".jpeg", ".png", ".gif"],
        "Documentos": [".pdf", ".docx", ".txt", ".xlsx"],
        "Vídeos": [".mp4", ".avi", ".mkv"],
        "Músicas": [".mp3", ".wav"],
        "Compactados": [".zip", ".rar"]
    }

    for arquivo in os.listdir(pasta):
        caminho_arquivo = os.path.join(pasta, arquivo)

        if os.path.isfile(caminho_arquivo):
            extensao = os.path.splitext(arquivo)[1].lower()

            for pasta_nome, extensoes in tipos.items():
                if extensao in extensoes:
                    pasta_destino = os.path.join(pasta, pasta_nome)

                    if not os.path.exists(pasta_destino):
                        os.mkdir(pasta_destino)

                    shutil.move(caminho_arquivo, pasta_destino)

    messagebox.showinfo("Sucesso", "Organização concluída com sucesso!")

# ---------------- INTERFACE ----------------

janela = tk.Tk()
janela.title("🗂 Organizador de Arquivos - Bernardo")
janela.geometry("420x250")
janela.configure(bg="#0f172a")
janela.resizable(False, False)

titulo = tk.Label(
    janela,
    text="Organizador Automático de Arquivos",
    font=("Arial", 16, "bold"),
    fg="white",
    bg="#0f172a"
)
titulo.pack(pady=20)

botao = tk.Button(
    janela,
    text="Selecionar Pasta e Organizar",
    font=("Arial", 12, "bold"),
    bg="#2563eb",
    fg="white",
    padx=15,
    pady=8,
    command=organizar_pasta
)
botao.pack(pady=30)

rodape = tk.Label(
    janela,
    text="Criado por Bernardo 👨‍💻",
    font=("Arial", 9),
    fg="#94a3b8",
    bg="#0f172a"
)
rodape.pack(side="bottom", pady=10)

janela.mainloop()
