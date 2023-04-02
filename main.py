import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Calculadora")
root.geometry("400x700")

# estilo dos botoões
pd_x = 10
pd_y = 3
bg_color = "white"
fg_color = "black"
# ------

containerPri = tk.Frame(root, width=150, padx=10)
containerPri.place(rely=0.26)
containerDisplay = tk.Frame(root, width=150)
containerDisplay.place(rely=0.1)

container1 = tk.Frame(root, width=150, padx=10)
container1.place(rely=0.4)
container2 = tk.Frame(root, width=150, padx=10)
container2.place(rely=0.54)
container3 = tk.Frame(root, width=150, padx=10)
container3.place(rely=0.68)
container4 = tk.Frame(root, width=150, padx=10)
container4.place(rely=0.82)

math_var = tk.StringVar()
display = tk.Label(containerDisplay, width=45, height=2, bg="white", fg="black", textvariable=math_var, anchor="w",
                   font=("Arial", 20))
display.pack()


def adicionar_clear():
    math_var.set("")


def adicionar_geral(num):
    valor_atual = math_var.get()
    novo_valor = str(valor_atual) + str(num)
    math_var.set(str(novo_valor))


def adicionar_back():
    math_var.set(math_var.get()[:-1])


def adicionar_igual():
    try:
        resul = eval(math_var.get())
        math_var.set("")
        math_var.set(resul)
    except:
        messagebox.showerror("Erro", "expressão invalida")


def adicionar_paren():
    strin = math_var.get()
    cont_ini = strin.count("(")
    cont_fim = strin.count(")")
    if cont_ini == 0 or cont_ini == cont_fim:
        valor_atual = math_var.get()
        novo_valor = str(valor_atual) + "("
        math_var.set(str(novo_valor))
    elif cont_ini < cont_fim:
        valor_atual = math_var.get()
        novo_valor = str(valor_atual) + "("
        math_var.set(str(novo_valor))
    elif cont_ini > cont_fim:
        valor_atual = math_var.get()
        novo_valor = str(valor_atual) + ")"
        math_var.set(str(novo_valor))
    else:
        pass


bot_1 = tk.Button(container1, text="1", height=2, width=3, justify="center", padx=pd_x, pady=pd_y, bg=bg_color,
                  fg=fg_color, font=("Arial", 20), command=lambda: adicionar_geral("1"))
bot_1.pack(side="left", padx=pd_x, pady=pd_y)
bot_2 = tk.Button(container1, text="2", height=2, width=3, justify="center", padx=pd_x, pady=pd_y, bg=bg_color,
                  fg=fg_color, font=("Arial", 20), command=lambda: adicionar_geral("2"))
bot_2.pack(side="left", padx=pd_x, pady=pd_y)
bot_3 = tk.Button(container1, text="3", height=2, width=3, justify="center", padx=pd_x, pady=pd_y, bg=bg_color,
                  fg=fg_color, font=("Arial", 20), command=lambda: adicionar_geral("3"))
bot_3.pack(side="left", padx=pd_x, pady=pd_y)
bot_vezes = tk.Button(container1, text="x", height=2, width=3, justify="center", padx=pd_x, pady=pd_y, bg=bg_color,
                      fg=fg_color, font=("Arial", 20), command=lambda: adicionar_geral("*"))
bot_vezes.pack(side="left", padx=pd_x, pady=pd_y)

bot_4 = tk.Button(container2, text="4", height=2, width=3, justify="center", padx=pd_x, pady=pd_y, bg=bg_color,
                  fg=fg_color, font=("Arial", 20), command=lambda: adicionar_geral("4"))
bot_4.pack(side="left", padx=pd_x, pady=pd_y)
bot_5 = tk.Button(container2, text="5", height=2, width=3, justify="center", padx=pd_x, pady=pd_y, bg=bg_color,
                  fg=fg_color, font=("Arial", 20), command=lambda: adicionar_geral("5"))
bot_5.pack(side="left", padx=pd_x, pady=pd_y)
bot_6 = tk.Button(container2, text="6", height=2, width=3, justify="center", padx=pd_x, pady=pd_y, bg=bg_color,
                  fg=fg_color, font=("Arial", 20), command=lambda: adicionar_geral("6"))
bot_6.pack(side="left", padx=pd_x, pady=pd_y)
bot_menos = tk.Button(container2, text="-", height=2, width=3, justify="center", padx=pd_x, pady=pd_y, bg=bg_color,
                      fg=fg_color, font=("Arial", 20), command=lambda: adicionar_geral("-"))
bot_menos.pack(side="left", padx=pd_x, pady=pd_y)

bot_7 = tk.Button(container3, text="7", height=2, width=3, justify="center", padx=pd_x, pady=pd_y, bg=bg_color,
                  fg=fg_color, font=("Arial", 20), command=lambda: adicionar_geral("7"))
bot_7.pack(side="left", padx=pd_x, pady=pd_y)
bot_8 = tk.Button(container3, text="8", height=2, width=3, justify="center", padx=pd_x, pady=pd_y, bg=bg_color,
                  fg=fg_color, font=("Arial", 20), command=lambda: adicionar_geral("8"))
bot_8.pack(side="left", padx=pd_x, pady=pd_y)
bot_9 = tk.Button(container3, text="9", height=2, width=3, justify="center", padx=pd_x, pady=pd_y, bg=bg_color,
                  fg=fg_color, font=("Arial", 20), command=lambda: adicionar_geral("9"))
bot_9.pack(side="left", padx=pd_x, pady=pd_y)
bot_mais = tk.Button(container3, text="+", height=2, width=3, justify="center", padx=pd_x, pady=pd_y, bg=bg_color,
                     fg=fg_color, font=("Arial", 20), command=lambda: adicionar_geral("+"))
bot_mais.pack(side="left", padx=pd_x, pady=pd_y)

bot_0 = tk.Button(container4, text="0", height=2, width=3, justify="center", padx=pd_x, pady=pd_y, bg=bg_color,
                  fg=fg_color, font=("Arial", 20), command=lambda: adicionar_geral("0"))
bot_0.pack(side="left", padx=pd_x, pady=pd_y)
bot_pon = tk.Button(container4, text=".", height=2, width=3, justify="center", padx=pd_x, pady=pd_y, bg=bg_color,
                    fg=fg_color, font=("Arial", 20), command=lambda: adicionar_geral("."))
bot_pon.pack(side="left", padx=pd_x, pady=pd_y)
bot_del = tk.Button(container4, text="<<", height=2, width=3, justify="center", padx=pd_x, pady=pd_y, bg=bg_color,
                    fg=fg_color, font=("Arial", 20), command=adicionar_back)
bot_del.pack(side="left", padx=pd_x, pady=pd_y)
bot_igual = tk.Button(container4, text="=", height=2, width=3, justify="center", padx=pd_x, pady=pd_y, bg=bg_color,
                      fg=fg_color, font=("Arial", 20), command=adicionar_igual)
bot_igual.pack(side="left", padx=pd_x, pady=pd_y)

bot_clear = tk.Button(containerPri, text="AC", height=2, width=3, justify="center", padx=pd_x, pady=pd_y, bg=bg_color,
                      fg=fg_color, font=("Arial", 20), command=adicionar_clear)
bot_clear.pack(side="left", padx=pd_x, pady=pd_y)
bot_paren = tk.Button(containerPri, text="( )", height=2, width=3, justify="center", padx=pd_x, pady=pd_y, bg=bg_color,
                      fg=fg_color, font=("Arial", 20), command=adicionar_paren)
bot_paren.pack(side="left", padx=pd_x, pady=pd_y)
bot_porcen = tk.Button(containerPri, text="%", height=2, width=3, justify="center", padx=pd_x, pady=pd_y, bg=bg_color,
                       fg=fg_color, font=("Arial", 20), command=lambda: adicionar_geral("%"))
bot_porcen.pack(side="left", padx=pd_x, pady=pd_y)
bot_div = tk.Button(containerPri, text="÷", height=2, width=3, justify="center", padx=pd_x, pady=pd_y, bg=bg_color,
                    fg=fg_color, font=("Arial", 20), command=lambda: adicionar_geral("/"))
bot_div.pack(side="left", padx=pd_x, pady=pd_y)

root.mainloop()