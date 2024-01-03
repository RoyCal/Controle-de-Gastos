from database import *

from pathlib import Path

from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, ttk, messagebox

window = Tk()

window.geometry("1280x960")
window.configure(bg = "#FFFFFF")
window.resizable(False, False)

def clearPage():
    for item in window.winfo_children():
        item.destroy()

def route(page):
    clearPage()

    match page:
        case "home":
            homePage()
        case "settings":
            settingsPage()

gastos = 0
renda = 0
saldo = 0
nomeUsuario = ''

def update_assets():
    global gastos
    global renda
    global saldo

    gastos = 0

    lines = linhas()
    for linha in lines:
        gastos += linha[2]

    gastos = round(gastos, 2)

    renda = renda_mensal()
    saldo = renda - gastos

    saldo = round(saldo, 2)

def update_user_name():
    global nomeUsuario

    nomeUsuario = user_name()

colunas_da_tabela = ["IdGasto", "Nome", "Valor"]
dados_da_tabela = []

def update_table_data():
    global dados_da_tabela

    dados_da_tabela = [list(tupla) for tupla in linhas()]

update_assets()
update_user_name()
update_table_data()

def homePage():
    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / Path(r"D:\Codigos\Controle_de_gastos\build\assets\frame0")

    def relative_to_assets(path: str) -> Path:
        return ASSETS_PATH / Path(path)

    canvas = Canvas(
        window,
        bg = "#FFFFFF",
        height = 960,
        width = 1280,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )

    def update_assets_labels(new_renda, new_gasto, new_saldo):
        canvas.itemconfig(tagOrId=renda_text, text=f'R$ {new_renda}')
        canvas.itemconfig(tagOrId=gastos_text, text=f'R$ {new_gasto}')
        canvas.itemconfig(tagOrId=saldo_text, text=f'R$ {new_saldo}')

    def mudar_renda_handler():
        new_income = entry_1.get()

        try:
            float(new_income)
        except:
            print("A entrada nao eh um numero!")
            return()

        mudarRendaMensal(float(new_income))

        update_assets()

        update_assets_labels(renda, gastos, saldo)

    def adicionar_gasto_handler():
        new_nome = entry_3.get()
        new_valor = entry_4.get()

        if new_nome == "":
            print("Por favor, insira um nome!")
            return
        
        try:
            float(new_valor)
        except:
            print("A entrada nao eh um numero!")
            return
        
        adicionar_gasto(new_nome, float(new_valor))

        update_assets()

        update_assets_labels(renda, gastos, saldo)

        update_table_data()

        update_table()

    def remover_gasto_handler():
        id_remove = entry_2.get()
        
        try:
            float(id_remove)
        except:
            print("A entrada nao eh um numero!")
            return
        
        remover_gasto(float(id_remove))

        update_assets()

        update_assets_labels(renda, gastos, saldo)

        update_table_data()

        update_table()

    def limpar_tabela_handler():
        if messagebox.askyesno(title="Confirmar", message="Deseja mesmo limpar a tabela?", icon='question'):
            
            limpar_tabela()

            update_assets()

            update_assets_labels(renda, gastos, saldo)

            update_table_data()

            update_table()

        else:
            return

    canvas.place(x = 0, y = 0)
    canvas.create_rectangle(
        0.0,
        0.0,
        1280.0,
        182.0,
        fill="#0047FF",
        outline="")

    canvas.create_text(
        43.0,
        53.0,
        anchor="nw",
        text="Controle de gastos",
        fill="#FFFFFF",
        font=("Inter", 64 * -1)
    )

    canvas.create_rectangle(
        639.0,
        181.0,
        640.0,
        960.0,
        fill="#000000",
        outline="")

    canvas.create_rectangle(
        639.0,
        649.0,
        1280.0,
        650.0000001728358,
        fill="#000000",
        outline="")

    canvas.create_rectangle(
        639.0,
        817.0,
        1280.0,
        818.0000001728358,
        fill="#000000",
        outline="")

    canvas.create_rectangle(
        639.0,
        342.0,
        1280.0,
        343.0000001728358,
        fill="#000000",
        outline="")

    image_image_1 = PhotoImage(
        file=relative_to_assets("image_1.png"))
    image_1 = canvas.create_image(
        318.0,
        248.0,
        image=image_image_1
    )

    entry_image_1 = PhotoImage(
        file=relative_to_assets("entry_1.png"))
    entry_bg_1 = canvas.create_image(
        840.0,
        289.5,
        image=entry_image_1
    )
    entry_1 = Entry(
        font="Inter 24",
        bd=0,
        bg="#c0c0c0",
        fg="#000716",
        highlightthickness=0
    )
    entry_1.place(
        x=674.0,
        y=259.0,
        width=332.0,
        height=63.0
    )

    canvas.create_text(
        43.0,
        208.0,
        anchor="nw",
        text="Renda mensal",
        fill="#000000",
        font=("Inter", 16 * -1)
    )

    renda_text = canvas.create_text(
        38.0,
        238.0,
        anchor="nw",
        text=f"R$ {renda}",
        fill="#000000",
        font=("Inter", 36 * -1)
    )

    image_image_2 = PhotoImage(
        file=relative_to_assets("image_2.png"))
    image_2 = canvas.create_image(
        318.0,
        464.0,
        image=image_image_2
    )

    canvas.create_text(
        43.0,
        424.0,
        anchor="nw",
        text="Saldo",
        fill="#000000",
        font=("Inter", 16 * -1)
    )

    canvas.create_text(
        38.0,
        523.0,
        anchor="nw",
        text="Despesas",
        fill="#000000",
        font=("Inter", 16 * -1)
    )

    canvas.create_text(
        454.0,
        523.0,
        anchor="nw",
        text="Limpar despesas",
        fill="#000000",
        font=("Inter", 16 * -1)
    )

    saldo_text = canvas.create_text(
        38.0,
        454.0,
        anchor="nw",
        text=f"R$ {saldo}",
        fill="#000000",
        font=("Inter", 36 * -1)
    )

    image_image_3 = PhotoImage(
        file=relative_to_assets("image_3.png"))
    image_3 = canvas.create_image(
        318.0,
        356.0,
        image=image_image_3
    )

    canvas.create_text(
        43.0,
        316.0,
        anchor="nw",
        text="Valor das despesas",
        fill="#000000",
        font=("Inter", 16 * -1)
    )

    gastos_text = canvas.create_text(
        38.0,
        346.0,
        anchor="nw",
        text=f"R$ {gastos}",
        fill="#000000",
        font=("Inter", 36 * -1)
    )

    image_image_4 = PhotoImage(
        file=relative_to_assets("image_4.png"))
    image_4 = canvas.create_image(
        318.0,
        749.0,
        image=image_image_4
    )

    tabela = ttk.Treeview(master=window, columns=colunas_da_tabela, show="headings")

    for coluna in colunas_da_tabela:
        tabela.heading(column=coluna, text=coluna)
        tabela.column(column=coluna, width=188)

    for linha in dados_da_tabela:
        tabela.insert(parent='', index='end', values=linha)

    tabela.place(x=38, y=570, height=358)

    def update_table():
        ids = tabela.get_children()
        for id in ids:
            tabela.delete(id)

        update_table_data()

        for coluna in colunas_da_tabela:
            tabela.heading(column=coluna, text=coluna)
            tabela.column(column=coluna, width=188)

        for linha in dados_da_tabela:
            tabela.insert(parent='', index='end', values=linha)

    canvas.create_text(
        654.0,
        186.0,
        anchor="nw",
        text="Mudar renda mensal",
        fill="#000000",
        font=("Inter", 24 * -1)
    )

    canvas.create_text(
        654.0,
        230.0,
        anchor="nw",
        text="Nova renda",
        fill="#000000",
        font=("Inter", 20 * -1)
    )

    button_image_1 = PhotoImage(
        file=relative_to_assets("button_1.png"))
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: mudar_renda_handler(),
        relief="flat"
    )
    button_1.place(
        x=1053.0,
        y=257.0,
        width=204.0,
        height=65.0
    )

    entry_image_2 = PhotoImage(
        file=relative_to_assets("entry_2.png"))
    entry_bg_2 = canvas.create_image(
        840.0,
        763.5,
        image=entry_image_2
    )
    entry_2 = Entry(
        font="Inter 24",
        bd=0,
        bg="#c0c0c0",
        fg="#000716",
        highlightthickness=0
    )
    entry_2.place(
        x=674.0,
        y=733.0,
        width=332.0,
        height=63.0
    )

    canvas.create_text(
        654.0,
        656.0,
        anchor="nw",
        text="Remover despesa",
        fill="#000000",
        font=("Inter", 24 * -1)
    )

    canvas.create_text(
        654.0,
        704.0,
        anchor="nw",
        text="Id do gasto",
        fill="#000000",
        font=("Inter", 20 * -1)
    )

    button_image_2 = PhotoImage(
        file=relative_to_assets("button_2.png"))
    button_2 = Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: remover_gasto_handler(),
        relief="flat"
    )
    button_2.place(
        x=1054.0,
        y=731.0,
        width=203.0,
        height=65.0
    )

    entry_image_3 = PhotoImage(
        file=relative_to_assets("entry_3.png"))
    entry_bg_3 = canvas.create_image(
        840.0,
        453.5,
        image=entry_image_3
    )
    entry_3 = Entry(
        font="Inter 24",
        bd=0,
        bg="#c0c0c0",
        fg="#000716",
        highlightthickness=0
    )
    entry_3.place(
        x=674.0,
        y=423.0,
        width=332.0,
        height=63.0
    )

    canvas.create_text(
        654.0,
        346.0,
        anchor="nw",
        text="Adicionar despesa",
        fill="#000000",
        font=("Inter", 24 * -1)
    )

    canvas.create_text(
        654.0,
        394.0,
        anchor="nw",
        text="Nome",
        fill="#000000",
        font=("Inter", 20 * -1)
    )

    entry_image_4 = PhotoImage(
        file=relative_to_assets("entry_4.png"))
    entry_bg_4 = canvas.create_image(
        840.0,
        584.5,
        image=entry_image_4
    )
    entry_4 = Entry(
        font="Inter 24",
        bd=0,
        bg="#c0c0c0",
        fg="#000000",
        highlightthickness=0
    )
    entry_4.place(
        x=674.0,
        y=554.0,
        width=332.0,
        height=63.0
    )

    canvas.create_text(
        654.0,
        525.0,
        anchor="nw",
        text="Valor",
        fill="#000000",
        font=("Inter", 20 * -1)
    )

    button_image_3 = PhotoImage(
        file=relative_to_assets("button_3.png"))
    button_3 = Button(
        image=button_image_3,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: adicionar_gasto_handler(),
        relief="flat"
    )
    button_3.place(
        x=1054.0,
        y=552.0,
        width=203.0,
        height=65.0
    )

    canvas.create_text(
        686.0,
        865.0,
        anchor="nw",
        text="Configurar usuario",
        fill="#000000",
        font=("Inter", 40 * -1)
    )

    button_image_4 = PhotoImage(
        file=relative_to_assets("button_4.png"))
    button_4 = Button(
        image=button_image_4,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: route("settings"),
        relief="flat"
    )
    button_4.place(
        x=1112.0,
        y=844.0,
        width=91.0,
        height=90.0
    )

    nomeUsuario_text = canvas.create_text(
        686.0,
        75.0,
        anchor="nw",
        text=f"Bem vindo, {nomeUsuario}",
        fill="#FFFFFF",
        font=("Inter", 40 * -1)
    )

    button_image_5 = PhotoImage(
        file=relative_to_assets("button_5.png"))
    button_5 = Button(
        image=button_image_5,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: limpar_tabela_handler(),
        relief="flat"
    )
    button_5.place(
        x=588.0,
        y=516.0,
        width=30.0,
        height=30.0
    )
    
    window.mainloop()

def settingsPage():
    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / Path(r"D:\Codigos\Controle_de_gastos\build\assets\frame1")

    def relative_to_assets(path: str) -> Path:
        return ASSETS_PATH / Path(path)

    canvas = Canvas(
        window,
        bg = "#FFFFFF",
        height = 960,
        width = 1280,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )

    def mudarUsuario_handler():
        new_user = entry_1.get()

        if new_user == "":
            print("Por favor, insira um nome!")
            return
        
        mudarUsuario(new_user)

        update_user_name()

        messagebox.showinfo(title="Aviso", message="Nome de usuario alterado com sucesso!")

    canvas.place(x = 0, y = 0)
    canvas.create_rectangle(
        0.0,
        0.0,
        1280.0,
        182.0,
        fill="#0047FF",
        outline="")

    canvas.create_text(
        45.0,
        53.0,
        anchor="nw",
        text="Configurar usuario",
        fill="#FFFFFF",
        font=("Inter", 64 * -1)
    )

    button_image_1 = PhotoImage(
        file=relative_to_assets("button_1.png"))
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: route("home"),
        relief="flat"
    )
    button_1.place(
        x=23.0,
        y=203.0,
        width=91.0,
        height=90.0
    )

    canvas.create_text(
        139.0,
        209.0,
        anchor="nw",
        text="Voltar",
        fill="#000000",
        font=("Inter", 36 * -1)
    )

    entry_image_1 = PhotoImage(
        file=relative_to_assets("entry_1.png"))
    entry_bg_1 = canvas.create_image(
        640.0,
        480.5,
        image=entry_image_1
    )
    entry_1 = Entry(
        font="Inter 24",
        bd=0,
        bg="#D9D9D9",
        fg="#000716",
        highlightthickness=0
    )
    entry_1.place(
        x=295.0,
        y=439.0,
        width=690.0,
        height=81.0
    )

    canvas.create_text(
        275.0,
        379.0,
        anchor="nw",
        text="Nome do usuario",
        fill="#000000",
        font=("Inter", 36 * -1)
    )

    button_image_2 = PhotoImage(
        file=relative_to_assets("button_2.png"))
    button_2 = Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: mudarUsuario_handler(),
        relief="flat"
    )
    button_2.place(
        x=518.0,
        y=576.0,
        width=204.0,
        height=65.0
    )
    
    window.mainloop()