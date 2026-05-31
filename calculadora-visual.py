# Autor: Gabriela Souza
# Projeto Calculadora de IMC
# Data 2026-05-31

# Importações
import customtkinter as ctk

# Configurações da janela
ctk.set_appearance_mode('dark')
ctk.set_default_color_theme('dark-blue')
ctk.set_widget_scaling(0.5)
ctk.set_window_scaling(1.2)

app = ctk.CTk()
app.geometry('300x400')
app.title('Calculadora de IMC')
app.iconbitmap('assets/ico/calc.ico')
app.resizable(False, False)

# Lógica
def calcular():
    nome_usuario = nome.get()
    altura_usuario = float(altura.get())
    peso_usuario = float(peso.get())

    imc = peso_usuario / (altura_usuario ** 2)

    resultado.configure(text=f'Olá, {nome_usuario}\n seu IMC é: {imc:.2f}')

# Configurações dos elementos da tela
titulo1 = ctk.CTkLabel(app,
                       text='CALCULADORA',
                       font=('Arial', 40, 'bold'),
                       text_color="#FFFFFF")
titulo1.pack(pady=(40, 0))

titulo2 = ctk.CTkLabel(app,
                       text='IMC',
                       font=('Arial', 50, 'bold'),
                       text_color="#A431D1")
titulo2.pack(pady=(0, 40))

nome = ctk.CTkEntry(app,
                     placeholder_text='Digite seu nome',
                     font=('Arial', 20),
                     width=250,
                     height=50)
nome.pack(pady=20)

altura = ctk.CTkEntry(app,
                       placeholder_text='Digite sua altura (m)',
                       font=('Arial', 20),
                       width=250,
                       height=50)
altura.pack(pady=20)

peso = ctk.CTkEntry(app,
                     placeholder_text='Digite seu peso (kg)',
                     font=('Arial', 20),
                     width=250,
                     height=50)
peso.pack(pady=20)

botao = ctk.CTkButton(app,
                      text='Calcular',
                      command=calcular,
                      corner_radius=10,
                      fg_color='#A431D1',
                      hover_color='#7A1E9C',
                      font=('Arial', 20, 'bold'),
                      width=250,
                      height=50)
botao.pack(pady=20)

resultado = ctk.CTkLabel(app,
                          text='',
                          font=('Arial', 30, 'bold'),
                          text_color="#FFFFFF")
resultado.pack(pady=20)

app.mainloop()