
from tkinter import *
from calculs import calculs, Instruments
from sigfig import round

window = Tk()
window.title('Incertitude')
window.geometry('720x480')

appareil_calcul = ''
type_calcul = ''
range_calcul = ''

def type_appareil(num):
    global appareil_calcul
    appareil_calcul = num

def type_type(type):
    global type_calcul
    type_calcul = type

def reset():
    global appareil_calcul, type_calcul
    appareil_calcul = ''
    type_calcul = ''

def appeler_calculs(valeur,range):
    global appareil_calcul, type_calcul
    range = str(range)
    valeur = str(valeur)
    try:
        incertitude = round(calculs(appareil_calcul, type_calcul, range, valeur),sigfigs = 1)
        rep = Tk()
        rep_text = Label(rep,font=('arial', 20), text=str(incertitude))
        rep_text.pack(expand=True)
        rep.mainloop()
    except Exception:
        rep = Tk()
        rep_text = Label(rep,font=('arial', 20), text='Erreur')
        rep_text.pack(expand=True)
        rep.mainloop()


appareil = Frame()
appareil_text = Label(window,font=('arial', 20), text="Entrez l'appareil (4,5 ou 6,5)")
appareil_text.pack(expand=True)
appareil1_button = Button(appareil, text='6,5',command= lambda : type_appareil('6,5'))
appareil1_button.pack(side=LEFT)
appareil2_button = Button(appareil, text='4,5',command= lambda : type_appareil('4,5'))
appareil2_button.pack(side=RIGHT)
appareil.pack(expand=True)
Type = Frame()
Type_text = Label(window,font=('arial', 20), text="Entrez le type de mesure ")
Type_text.pack(expand=True)
Type1_button = Button(Type, text='Tension',command= lambda : type_type('Tension'))
Type1_button.grid(row=0,column=0)
Type1_button = Button(Type, text='Résistance',command= lambda : type_type('Résistance'))
Type1_button.grid(row=0,column=1)
Type1_button = Button(Type, text='Courant',command= lambda : type_type('Courant'))
Type1_button.grid(row=0,column=2)
Type.pack(expand=True)
Range = Frame()
Range_text = Label(window,font=('arial', 20), text="Entrez le range de votre mesure")
Range_text.pack(expand=True)
Range_entry = Entry(Range, bd=0)
Range_entry.grid(row=0,column=0)
Range.pack(expand=True)
Valeur = Frame()
Valeur_text = Label(window,font=('arial', 20), text="Entrez votre mesure")
Valeur_text.pack(expand=True)
Valeur_entry = Entry(Valeur, bd=0)
Valeur_entry.grid(row=0,column=0)
Valeur.pack(expand=True)
Boutton = Frame()
Type1_button = Button(Boutton, text='Calculez',command= lambda : appeler_calculs(Valeur_entry.get(), Range_entry.get()))
Type1_button.grid(row=0,column=0)
Type1_button = Button(Boutton, text='Reset',command=reset)
Type1_button.grid(row=0,column=1)
Boutton.pack(expand=True)
window.mainloop()