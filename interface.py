# importando dependencias do Tkinter
from tkinter.ttk import *
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog as fd

# importando pillow
from PIL import ImageTk, Image

# tk calendar
from tkcalendar import Calendar, DateEntry
from datetime import date

# cores
co0 = "#2e2d2b"  # Preta
co1 = "#feffff"  # Branca
co2 = "#e5e5e5"  # grey
co3 = "#00a095"  # Verde
co4 = "#403d3d"  # letra
co6 = "#003452"  # azul
co7 = "#ef5350"  # vermelha

co6 = "#146C94"  # azul
co8 = "#263238"  # + verde
co9 = "#e9edf5"  # + verde


janela = Tk()
janela.title("")
janela.geometry("810x535")
janela.configure(background=co1)
janela.resizable(width=FALSE, height=FALSE)

style = Style(janela)
style.theme_use("clam")


# Criando Frames

frame_logo = Frame(janela, width=850, height=52, bg=co6)
frame_logo.grid(row=0, column=0, pady=0, padx=0, sticky=NSEW, columnspan=5)


frame_buttons = Frame(janela, width=100, height=200, bg=co2, relief=RAISED)
frame_buttons.grid(row=1, column=0, pady=1, padx=0, sticky=NSEW)

frame_details = Frame(janela, width=800, height=100, bg=co2, relief=SOLID)
frame_details.grid(row=1, column=1, pady=1, padx=10, sticky=NSEW)

frame_tabela = Frame(janela, width=800, height=100, bg=co2, relief=SOLID)
frame_tabela.grid(row=3, column=0, pady=0, padx=10, sticky=NSEW, columnspan=5)


# frame logo

global imagem, imagem_string, l_imagem

app_lg = Image.open("logo.jpg")
app_lg = app_lg.resize((50, 50))
app_lg = ImageTk.PhotoImage(app_lg)
app_logo = Label(
    frame_logo,
    image=app_lg,
    text=" Sistema de Registro de Alunos",
    width=850,
    compound=LEFT,
    anchor=NW,
    font=("Verdana 15"),
    bg=co6,
    fg=co1,
)
app_logo.place(x=5, y=0)


# Creating inputs

l_nome = Label(frame_details, text="Nome", anchor=NW, font=("Ivy 10"), bg=co1, fg=co4)
l_nome.place(x=4, y=10)
e_nome = Entry(frame_details, width=30, justify="left", relief="solid")
e_nome.place(x=7, y=40)

l_email = Label(frame_details, text="Email", anchor=NW, font=("Ivy 10"), bg=co1, fg=co4)
l_email.place(x=4, y=70)
e_email = Entry(frame_details, width=30, justify="left", relief="solid")
e_email.place(x=7, y=100)

l_phone = Label(
    frame_details, text="Telefone", anchor=NW, font=("Ivy 10"), bg=co1, fg=co4
)
l_phone.place(x=4, y=130)
e_phone = Entry(frame_details, width=15, justify="left", relief="solid")
e_phone.place(x=7, y=160)

l_gender = Label(frame_details, text="Sexo", anchor=NW, font=("Ivy 10"), bg=co1, fg=co4)
l_gender.place(x=127, y=130)
c_gender = ttk.Combobox(frame_details, width=7, font=("Ivy 8 bold"), justify="center")
c_gender["values"] = ("M", "F", "Prefiro Não Dizer")
c_gender.place(x=130, y=160)

l_birthday = Label(
    frame_details, text="Data de Nascimento", anchor=NW, font=("Ivy 10"), bg=co1, fg=co4
)
l_birthday.place(x=220, y=10)
birthday = DateEntry(
    frame_details,
    width=18,
    justify="center",
    backgroud="darkblue",
    foreground="white",
    borderwidth=2,
    year=2026,
)
birthday.place(x=224, y=40)

l_adress = Label(
    frame_details, text="Endereço", anchor=NW, font=("Ivy 10"), bg=co1, fg=co4
)
l_adress.place(x=220, y=70)
e_adress = Entry(frame_details, width=20, justify="left", relief="solid")
e_adress.place(x=224, y=100)

cursos = ["Engenharia", "Medicina", "Sociais"]

l_curso = Label(
    frame_details, text="Cursos", anchor=NW, font=("Ivy 10"), bg=co1, fg=co4
)
l_curso.place(x=220, y=130)
c_curso = ttk.Combobox(frame_details, width=20, font=("Ivy 8 bold"), justify="center")
c_curso["values"] = cursos
c_curso.place(x=224, y=160)

# funcao para escolher imagem


def escolher_imagem():
    global imagem, imagem_string, l_imagem

    imagem = fd.askopenfilename()
    imagem_string = imagem

    imagem = Image.open(imagem)
    imagem = imagem.resize((130, 130))
    imagem = imageTk.photoImage(imagem)
    l_imagem = Label(
        frame_details,
        image=imagem,
        bg=co1,
        fg=co4,
    )
    l_imagem.place(x=390, y=10)


botao_carregar = Button(
    frame_details,
    command=escolher_imagem,
    text="Carregar foto".upper(),
    width=20,
    compound=CENTER,
    anchor=CENTER,
    overrelief=RIDGE,
    font="Ivy 7 bold",
    bg=co1,
    fg=co0,
)
botao_carregar.place(x=390, y=160)

janela.mainloop()
