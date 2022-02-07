import I_A
from tkinter import *

class Incertitude_intelligente:

    def __init__(self):
        self.appareil_calcul = ''

        self.window = Tk()
        self.window.title('Incertitude')
        self.window.geometry('720x480')
        self.appareil = Frame()
        self.appareil_text = Label(self.window,font=('arial', 20),text="Entrez l'appareil (4,5 ou 6,5)")
        self.appareil_text.pack(expand=True)
        self.appareil1_button = Button(self.appareil, text='6,5' ,command= lambda : self.type_appareil('6.5'))
        self.appareil1_button.pack(side=LEFT)
        self.appareil2_button = Button(self.appareil, text='4,5',command= lambda : self.type_appareil('4.5'))
        self.appareil2_button.pack(side=RIGHT)
        self.appareil.pack(expand=True)
        self.Valeur = Frame()
        self.Valeur_text = Label(self.window,font=('arial', 20), text="Entrez votre mesure")
        self.Valeur_text.pack(expand=True)
        self.Valeur_entry = Entry(self.Valeur, bd=0)
        self.Valeur_entry.grid(row=0,column=0)
        self.Valeur.pack(expand=True)
        self.réponse = Frame()
        self.réponse_text = Label(self.window,font=('arial', 20), text="Votre incertitude est : ")
        self.réponse_text.pack(expand=True)
        self.range_text = Label(self.window,font=('arial', 20), text="Le range déterminé est : ")
        self.range_text.pack(expand=True)
        self.Boutton = Frame()
        self.Type4_button = Button(self.Boutton, text='Calculez',command= lambda : self.appeler_calculs(self.Valeur_entry.get()))
        self.Type4_button.grid(row=0,column=0)
        self.Type5_button = Button(self.Boutton, text='Reset',command=self.reset)
        self.Type5_button.grid(row=0,column=1)
        self.Boutton.pack(expand=True)

        self.window.mainloop()

    def type_appareil(self,num):
        self.appareil_calcul = num
        if num == '6.5':
            self.appareil1_button.config(foreground="red")
            self.appareil2_button.config(foreground="black")
        elif num == '4.5':
            self.appareil2_button.config(foreground="red")
            self.appareil1_button.config(foreground="black")

    def appeler_calculs(self, valeur):
        try:
            a = I_A.calcul_intelligent(str(valeur),self.appareil_calcul)
        except Exception:
            rep = Tk()
            rep_text = Label(rep,font=('arial', 20), text='Erreur')
            rep_text.pack(expand=True)
            rep.mainloop()
        self.réponse_text.config(text=f"Votre incertitude est : {a[0]}")
        self.range_text.config(text=f"Le range déterminé est : {a[1]}")

    def reset(self):
        self.appareil_calcul = ''
        self.appareil2_button.config(foreground="black")
        self.appareil1_button.config(foreground="black")
