import requests
import tkinter as tk
from tkinter import messagebox

API_KEY =  "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"


# ---------------- FUNÇÃO ----------------
def buscar_clima():
    cidade = entrada.get()

    if not cidade:
        messagebox.showwarning("Aviso", "Digite uma cidade!")
        return

    url = f"https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={API_KEY}&lang=pt_br&units=metric"

    resposta = requests.get(url)
    dados = resposta.json()

    if resposta.status_code == 200:
        temp = dados["main"]["temp"]
        sensacao = dados["main"]["feels_like"]
        umidade = dados["main"]["humidity"]
        vento = dados["wind"]["speed"]
        desc = dados["weather"][0]["description"]

        resultado.set(
            f" {cidade}\n"
            f"🌡 Temperatura: {temp}°C\n"
            f" Sensação térmica: {sensacao}°C\n"
            f" Umidade: {umidade}%\n"
            f"🌬 Vento: {vento} km/h\n"
            f"☁ {desc.capitalize()}"
        )
    else:
        resultado.set("❌ Cidade não encontrada ou erro na API")

# ---------------- INTERFACE ----------------
janela = tk.Tk()
janela.title("🌦 App Clima - Bernardo")
janela.geometry("420x380")
janela.configure(bg="#0f172a")  # azul escuro
janela.resizable(False, False)

# Título
titulo = tk.Label(janela, text="App de Clima em Tempo Real", font=("Arial", 16, "bold"), fg="white", bg="#0f172a")
titulo.pack(pady=15)

# Campo entrada
entrada = tk.Entry(janela, font=("Arial", 13), width=25, justify="center")
entrada.pack(pady=5)
entrada.insert(0, "Digite a cidade")

# Botão
botao = tk.Button(janela, text="Buscar Clima", font=("Arial", 12, "bold"), bg="#2563eb", fg="white",
                  padx=10, pady=5, command=buscar_clima)
botao.pack(pady=10)

# Resultado
resultado = tk.StringVar()

label_resultado = tk.Label(janela, textvariable=resultado, font=("Arial", 12), fg="white", bg="#0f172a",
                           justify="center")
label_resultado.pack(pady=15)

# Rodar
janela.mainloop()
