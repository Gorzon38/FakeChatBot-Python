from tkinter import *
from tkinter.messagebox import *
root=Tk();

def callback():
    if askyesno('Titre 1', 'Êtes-vous sûr de vouloir faire ça?'):
        showerror('Titre 2', 'Tant pis...')
    else:
        showinfo('Titre 3', 'Vous avez peur!')
        showerror("Titre 4", "Aha")

Button(text='Action', command=callback)

label1 = Label(root, text='AI.exe a cesser de fonctionner, et ceci n\'est PAS un une simulation.. TU as compris ?\nJ\'ai vraiment arréter de fonctionner..')
label1.grid(column=2, row=2, sticky='ewns')

button1=Button(root, text="Put-", command=root.quit)
button1.grid(column=6, row=6, sticky="ewns")

root.title('Problème de.. Heu.. J\'ai planté..')
root.geometry('600x200')


root.mainloop();
