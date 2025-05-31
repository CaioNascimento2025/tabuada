import customtkinter

janela = customtkinter.CTk()
janela.title('Seja bem vindo')
janela.geometry('400x300')
label = customtkinter.CTkLabel(janela,text = 'De Qual Número quer ver a tabuada')
label.pack(padx=10,pady=10)
input_numero = customtkinter.CTkEntry(janela,placeholder_text = 'Escolha um número inteiro')
input_numero.pack(padx=10,pady=10)

janela_resposta = customtkinter.CTk(fg_color='#000000')
janela_resposta.title('Tabuada')
janela_resposta.geometry('300x300')
def iniciar_tabuada():
    try:
        numero = int(input_numero.get())
        tabuada = ''
        for contador in range(1,11):
            tabuada += f'{numero:>2} x {contador:>2} = {numero * contador:>10}\n'

        mensagem = customtkinter.CTkLabel(janela_resposta,text=tabuada,text_color='#ffffff')
        mensagem.pack(padx=10,pady=10)
        janela_resposta.mainloop()
    except:
        mensagem = customtkinter.CTkLabel(janela_resposta,text='Precisa ser um número!')
        mensagem.pack(padx=10,pady=10)
        janela_resposta.mainloop()

button = customtkinter.CTkButton(janela,text='Iniciar',command=iniciar_tabuada)
button.pack(padx=10,pady=10)


janela.mainloop()
